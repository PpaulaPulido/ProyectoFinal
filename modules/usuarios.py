from flask import Blueprint, request, render_template, redirect, url_for, flash,current_app,send_from_directory,abort,session,jsonify,json
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash 
from db import get_db, get_cursor
import os
import mysql.connector

usuarios = Blueprint('usuarios', __name__)
db = get_db()
cursor = get_cursor(db)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#*********************************************Ruta de formulario contacto*********************************************************
@usuarios.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    tema = request.form.get('tema')
    mensaje = request.form.get('mensaje')
    
    # Almacenar en la base de datos
    cursor.execute("""
        INSERT INTO mensajes_contacto (nombre, email, tema, mensaje)
        VALUES (%s, %s, %s, %s)
    """, (nombre, email, tema, mensaje))
    db.commit()
    return redirect(url_for('usuarios.index_user'))
#*******************************************Ruta de iniciar sesion****************************************************************
@usuarios.route('/login', methods=['GET', 'POST'])
def inicio_sesion():
    if request.method == 'POST':
        username = request.form.get('txtusuario')
        password = request.form.get('txtcontrasena')
        roles = request.form.get('rol')

        try:
            db = get_db()
            cursor = db.cursor(dictionary=True)  # Inicializar el cursor con dictionary=True
            
            if roles == 'usuario':
                sql = 'SELECT codusuario, correousu, contrasena FROM usuario WHERE correousu = %s'
                cursor.execute(sql, (username,))
                user = cursor.fetchone()
                if user and check_password_hash(user['contrasena'], password):
                    session['email'] = user['correousu']
                    session['user_id'] = user['codusuario']
                    cursor.close()
                    return redirect(url_for('usuarios.perfil_usuario'))
                else:
                    error = 'Credenciales inválidas. Por favor, inténtalo de nuevo.'
                    return render_template('iniciar_sesion.html', error=error)
            
            elif roles == 'Administrador':
                sql = 'SELECT codadmin, correoadmin, contrasena FROM administrador WHERE correoadmin = %s'
                cursor.execute(sql, (username,))
                admin = cursor.fetchone()
                if admin and check_password_hash(admin['contrasena'], password):
                    session['emailAdmin'] = admin['correoadmin']
                    session['admin_id'] = admin['codadmin']
                    cursor.close()
                    return redirect(url_for('admin.perfil_admin'))
                else:
                    cursor.close()
                    error = 'Credenciales inválidas. Por favor, inténtalo de nuevo.'
                    return render_template('iniciar_sesion.html', error=error)
        
        except Exception as e:
            flash(f'Error en la base de datos: {str(e)}', 'error')
            return render_template('iniciar_sesion.html', error="Ocurrió un error durante el inicio de sesión.")
        
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()  # Cerrar el cursor solo si está definido y no es None
    
    return render_template('iniciar_sesion.html')
           
#****************************************Ruta para cerrar la sesion***************************************************************
@usuarios.route('/logout')
def logout():
    if 'email' in session:
        if 'user_id' in session:
            session.pop('user_id',None)
            session.pop('email', None)
            
        if 'admin_id' in session:
            session.pop('admin_id',None)
            session.pop('emailAdmin', None)
        
    return redirect(url_for('index'))

#********************************************Ruta para recuperar contraseña***********************************************************************
@usuarios.route('/recuperarContrasena',methods=['GET','POST'])
def recuperarContrasena():
    if request.method == 'POST':
        roles = request.form.get('rolRe')
        Email = request.form.get('correoRe')
        contrasenaActual = request.form.get('txtcontrasenaActual')
        contrasenaNueva = request.form.get('txtcontrasenaNueva')
        confirmarContrasena = request.form.get('txtcontrasenaConfirmar')
    
        # Verificar si el correo está registrado como usuario
        correo_registrado_usuario = False
        correo_registrado_administrador = False
        
        # Conexión a la base de datos y cursor
        db = get_db()
        cursor = db.cursor()
        
        # Verificar si el correo está registrado como usuario
        cursor.execute('SELECT correousu FROM usuario WHERE correousu = %s', (Email,))
        resultado_usuario = cursor.fetchall()
        if len(resultado_usuario) > 0:
            correo_registrado_usuario  = True
        
        # Verificar si el correo está registrado como administrador
        cursor.execute('SELECT correoadmin FROM administrador WHERE correoadmin = %s', (Email,))
        resultado_administrador = cursor.fetchall()
        if len(resultado_administrador) > 0:
            correo_registrado_administrador = True
            
        if (roles == 'usuario' and correo_registrado_usuario == False):
            return jsonify({'success': False, 'registrado':False,'message': 'El correo electrónico no está registrado'})
        
        if( roles == 'Administrador' and correo_registrado_administrador == False):
            return jsonify({'success': False, 'registrado':False,'message': 'El correo electrónico no está registrado'})
        
        # Verificar si las contraseñas coinciden
        if (contrasenaActual == ''):
            return jsonify({'success': False, 'message': 'Por favor ingresa la última contraseña'})
        
        if (contrasenaNueva == ''):
            return jsonify({'success': False, 'message': 'Por favor ingresa la nueva contraseña'})
        
        if contrasenaNueva != confirmarContrasena:
            return jsonify({'success': False, 'message': 'Las contraseñas no coinciden'})
        
        # Encriptar la contraseña
        contrasenaEncriptada = generate_password_hash(contrasenaNueva)
        
        if roles == 'usuario':
            cursor.execute("UPDATE usuario SET contrasena = %s WHERE correousu = %s",
                (contrasenaEncriptada, Email))
            db.commit()
            return jsonify({'success': True, 'registrado': True, 'message': 'Contraseña actualizada correctamente'})
        
        elif roles == 'Administrador':
            cursor.execute("UPDATE administrador SET contrasena = %s WHERE correoadmin = %s",(contrasenaEncriptada, Email))
            db.commit()
            return jsonify({'success': True, 'registrado': True, 'message': 'Contraseña actualizada correctamente'})
        
        else:
            return jsonify({'success': False, 'message': 'Rol no válido'})
    
    return render_template('formulario_contrasena.html')
                
#*******************************************Ruta de registro de usuario****************************************************************
@usuarios.route('/registrarUser', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'POST':
        # Obtener datos del formulario
        Nombres = request.form.get('nombres')
        Apellidos = request.form.get('apellidos')
        telefono = request.form.get('tel')
        fechaNac = request.form.get('fechaNac')
        Email = request.form.get('correo')
        roles = request.form.get('rol')
        contrasena = request.form.get('contrasena')
        confirmar_contrasena = request.form.get('confirmar_contrasena')
        
        # Verificar si las contraseñas coinciden
        if contrasena != confirmar_contrasena:
            return jsonify({'success': False, 'message': 'Las contraseñas no coinciden'})
        
        if (contrasena == ''):
            return jsonify({'success': False, 'message': 'Por favor ingresa la contraseña'})

        # Encriptar la contraseña
        contrasenaEncriptada = generate_password_hash(contrasena)
        
        correo_registrado_usuario = False
        correo_registrado_administrador = False
        
        # Verificar si el correo está registrado como usuario
        cursor.execute('SELECT correousu FROM usuario WHERE correousu = %s', (Email,))
        resultado_usuario = cursor.fetchall()
        if len(resultado_usuario) > 0:
            correo_registrado_usuario = True
        
        # Verificar si el correo está registrado como administrador
        cursor.execute('SELECT correoadmin FROM administrador WHERE correoadmin = %s', (Email,))
        resultado_administrador = cursor.fetchall()
        if len(resultado_administrador) > 0:
            correo_registrado_administrador = True
        
        # Verificar si el correo está registrado 
        if (roles == 'usuario' and correo_registrado_usuario):
            return jsonify({'success': True, 'registrado':True,'message': 'El correo electrónico ya está registrado'})
        
        if( roles == 'Administrador' and correo_registrado_administrador):
            return jsonify({'success': True, 'registrado':True,'message': 'El correo electrónico ya registrado'})
        
            
        if roles == 'usuario':
            cursor.execute(
                "INSERT INTO usuario (nombreusu, apellidousu, telusu, fechanac_usu, correousu, contrasena) VALUES (%s, %s, %s, %s, %s, %s)",
                (Nombres, Apellidos, telefono, fechaNac, Email, contrasenaEncriptada)
            )
            db.commit()
            return jsonify({'success': True,'registrado':False, 'message': 'Usuario creado correctamente'})
        
        elif roles == 'Administrador':
            cursor.execute(
                "INSERT INTO administrador (nombreadmin, apellidoadmin, telfadmin, correoadmin, fechanac_admin, contrasena) VALUES (%s, %s, %s, %s, %s, %s)",
                (Nombres, Apellidos, telefono, Email, fechaNac, contrasenaEncriptada)
            )
            db.commit() 
            return jsonify({'success': True,'registrado':False, 'message': 'Administrador creado correctamente'})
        
        else:
            return jsonify({'success': False, 'message': 'Rol no válido'})
    
    return render_template('registro.html')

#*******************************************Ruta de perfil usuario****************************************************************        
@usuarios.route('/perfil_usuario')
def perfil_usuario():
    
    user_id = session.get('user_id')
    
    if not user_id:
        flash('No está autenticado.', 'error')
        return redirect(url_for('usuarios.inicio_sesion')) 
        
    db = get_db() 
    cursor = db.cursor() 
    
    default_portada = '/static/img/Portada-Bogota.jpg'
    default_perfil = '/static/img/perfil_user.png'
    
    try:
        cursor.execute("SELECT nombreusu,apellidousu,correousu FROM usuario WHERE codusuario = %s", (user_id,))
        usuDatos= cursor.fetchone()
        
        if usuDatos:
            nombreUsu, apellidoUsu, correoUsu = usuDatos
        else:
            nombreUsu, apellidoUsu, correoUsu  = "Información no disponible"
        
        cursor.execute("SELECT direccionUsu,ciudadUsu,descripcionAcercaUsu,sitioWebUsu,blogUsu FROM datosUsuario WHERE codusuario= %s",(user_id,))
        usuario_datosDetalles = cursor.fetchone()
        
        if usuario_datosDetalles:
            direccionUsu, ciudadUsu, descripcionAcercaUsu, sitioWebUsu, blogUsu = usuario_datosDetalles
        else:
            direccionUsu = ciudadUsu = descripcionAcercaUsu = sitioWebUsu = blogUsu = "No disponible"
            
        def obtenerImagen(image_type, default_image):
            cursor.execute("SELECT ruta_foto FROM fotos_usuario WHERE cod_usuario = %s AND tipo_foto = %s ORDER BY id_foto DESC LIMIT 1", (user_id, image_type))
            image = cursor.fetchone()
            if image:
                return os.path.join('/', image[0])
            else:
                return default_image

        fotoPortada = obtenerImagen('portada', default_portada)
        fotoPerfil = obtenerImagen('perfil', default_perfil)

    finally:
        cursor.close()  
        db.close()
        
    return render_template('perfil_usuario.html',nombreUsu = nombreUsu,apellidoUsu = apellidoUsu,correoUsu = correoUsu,fotoPortada = fotoPortada, fotoPerfil = fotoPerfil,direccionUsu = direccionUsu,ciudadUsu = ciudadUsu,descripcionAcercaUsu = descripcionAcercaUsu,sitioWebUsu = sitioWebUsu, blogUsu = blogUsu, user_id = user_id)

#*******************************************Ruta de imagen de perfil****************************************************************
@usuarios.route('/perfilImagen_user')
def perfilImagen_usuario():
    
    user_id = session.get('user_id')
    
    if not user_id:
        flash('No está autenticado.', 'error')
        return redirect(url_for('usuarios.inicio_sesion')) 
    
    
    db = get_db()
    cursor = get_cursor(db)
    
    cursor.execute("SELECT ruta_foto FROM fotos_usuario  WHERE cod_usuario= %s AND tipo_foto = 'perfil' ORDER BY id_foto DESC LIMIT 1", (user_id,))
    fotoPerfil = cursor.fetchone()
    
    if fotoPerfil:
        fotoPerfil_path = fotoPerfil[0]
    else:
        fotoPerfil_path = None
        

    if fotoPerfil_path:
        directory_path = os.path.join(current_app.root_path, 'static', 'uploads')
        file_name = os.path.basename(fotoPerfil_path)
    else:
        directory_path = os.path.join(current_app.root_path, 'static', 'img')
        file_name = 'perfil_user.png'  # Nombre de la imagen por defecto
    
    full_file_path = os.path.join(directory_path, file_name)
    if not os.path.isfile(full_file_path):
        print(f"Archivo no encontrado: {full_file_path}")  
        abort(404)  # Si el archivo no existe, devuelve un error 404

    return send_from_directory(directory_path, file_name)

#*******************************Ruta para subir la foto de perfil ********************************************************************************
@usuarios.route('/subirFotoPerfil_usuario', methods=['POST'])
def subirFotoperfil_usu():
    
    user_id = session.get('user_id')
    cursor = db.cursor()
    
    if not user_id:
        flash('No está autenticado.', 'error')
        return redirect(url_for('usuarios.inicio_sesion')) 
    
    
    file = request.files.get('fotoPerfilUsu')
    
    if file and allowed_file(file.filename):
        
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        cursor.execute("""
            INSERT INTO fotos_usuario(cod_usuario, ruta_foto, tipo_foto)
            VALUES (%s, %s, 'perfil')
            ON DUPLICATE KEY UPDATE ruta_foto = VALUES(ruta_foto)
        """, (user_id, file_path))
        
        db.commit()

        flash('Foto de portada actualizada con éxito.')
        return redirect(url_for('usuarios.perfil_usuario'))
    
    else:
        flash('No se seleccionó archivo o el tipo de archivo no está permitido.')
        return redirect(url_for('usuarios.perfil_usuario'))
    
#*********************************Ruta para subir la foto de portada**************************************** 
@usuarios.route('/subirPortadaUsu', methods=['POST'])
def subirportadaUsu():
    
    user_id = session.get('user_id')
    
    if not user_id:
        flash('No está autenticado.', 'error')
        return redirect(url_for('usuarios.inicio_sesion')) 
    
    file = request.files.get('fotoPortada')
    if file and allowed_file(file.filename):
        # 'secure_filename' sanea el nombre del archivo para asegurarse de que es seguro de usar en el sistema de archivos.
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        cursor.execute("""
            INSERT INTO fotos_usuario (cod_usuario, ruta_foto, tipo_foto)
            VALUES (%s, %s, 'portada')
            ON DUPLICATE KEY UPDATE ruta_foto = VALUES(ruta_foto)
        """, (user_id, file_path))
        
        db.commit()
        
        flash('Foto de portada actualizada con éxito.')
        
        return redirect(url_for('usuarios.perfil_usuario'))
    
    else:
        flash('No se seleccionó archivo o el tipo de archivo no está permitido.')
        return redirect(url_for('usuarios.perfil_usuario'))

#*********************************************Ruta para las reseñas del usuario******************************
@usuarios.route('/reseñasUsuario')
def resena_usuario():
    
    user_id = session.get('user_id')
    
    if not user_id:
        flash('No está autenticado.', 'error')
        return redirect(url_for('usuarios.inicio_sesion')) 
    
    db = get_db()
    cursor = db.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT R.calificacion, R.comentario, R.entidad_tipo, R.entidad_id FROM Resenas AS R WHERE R.autor_tipo = 'usuario' AND R.autor_id = %s ORDER BY R.id_resena DESC LIMIT 5", (user_id,))
        resenas = cursor.fetchall()
        
        resenas_list = []
        
        for resena in resenas:
            nombre_entidad = ""
            
            if resena['entidad_tipo'] == 'evento':
                cursor.execute("SELECT nombreeven FROM eventos WHERE ideven = %s", (resena['entidad_id'],))
                entidad = cursor.fetchone()
                if entidad:
                    nombre_entidad = entidad['nombreeven']
                    
            elif resena['entidad_tipo'] == 'emprendimiento':
                cursor.execute("SELECT nombreempre FROM emprendimientos WHERE idempre = %s", (resena['entidad_id'],))
                entidad = cursor.fetchone()
                if entidad:
                    nombre_entidad = entidad['nombreempre']
                    
            elif resena['entidad_tipo'] == 'restaurante':
                cursor.execute("SELECT nombreresta FROM restaurantes WHERE idresta = %s", (resena['entidad_id'],))
                entidad = cursor.fetchone()
                if entidad:
                    nombre_entidad = entidad['nombreresta']
            
            resenas_list.append({
                'calificacion': resena['calificacion'],
                'comentario': resena['comentario'],
                'nombre_entidad': nombre_entidad
            })
    finally:
        cursor.close()
        db.close()
    
    return jsonify(resenas_list)

#******************************************Galeria de fotos del usuario*******************************************************
@usuarios.route('/galeriaUsuario')
def galeria_usuario():
    
    user_id = session.get('user_id')
    
    if not user_id:
        flash('No está autenticado.', 'error')
        return redirect(url_for('usuarios.inicio_sesion')) 
    
    db = get_db()
    cursor = db.cursor()
    
    try:
        cursor.execute("""
            SELECT ruta_foto, tipo_foto FROM fotos_usuario
            WHERE tipo_foto IN ('perfil', 'portada')
            ORDER BY id_foto DESC LIMIT 9
        """)
        fotos = cursor.fetchall()
        # Formatear los resultados como una lista de diccionarios
        
        fotos_list = [{'ruta_foto': normalize_path(foto[0]), 'tipo_foto': foto[1]} for foto in fotos]
    finally:
        cursor.close()
        db.close()
    
    return jsonify(fotos_list)

#*****************************************Ruta de mis fotos de usuario **************************************************************
@usuarios.route('/MisFotosUsuario')
def photosUser():
    
    user_id = session.get('user_id')
    
    if not user_id:
        flash('No está autenticado.', 'error')
        return redirect(url_for('usuarios.inicio_sesion')) 
    
    db = get_db()
    cursor = db.cursor()
    
    try:
        cursor.execute("""
            SELECT ruta_foto, tipo_foto FROM fotos_usuario
            WHERE tipo_foto IN ('perfil', 'portada')
            ORDER BY id_foto DESC
        """)
        fotos = cursor.fetchall()
        # Formatear los resultados como una lista de diccionarios
        
        fotos_list = [{'ruta_foto': normalize_path(foto[0]), 'tipo_foto': foto[1]} for foto in fotos]
    finally:
        cursor.close()
        db.close()
    
    return jsonify(fotos_list)

#*****************************************Ruta para editar perfil usuarios**********************************************

@usuarios.route('/editarPerfilUsuario/<int:id>', methods=['POST', 'GET'])
def editarPerfilUsuario(id):
    db = get_db()
    cursor = get_cursor(db)
    
    if request.method == 'POST':
        nombreUsu = request.form.get('nombreUsu')
        apellidosUsu = request.form.get('apellidosUsu')
        correoUsu = request.form.get('correoUsu')
        telefonoUsu = request.form.get('telefonoUsu')
        fechaNacUsu = request.form.get('fechaNacUsu')
        direccionUsu = request.form.get('direccionUsu')
        ciudadUsu = request.form.get('ciudadUsu')
        descripcionAcerca = request.form.get('acercaUsu')
        sitioWeb = request.form.get('sitioWebUsu')
        blog = request.form.get('blogUsu')

        sql = "UPDATE usuario SET nombreusu = %s, apellidousu = %s, telusu = %s, fechanac_usu = %s, correousu = %s WHERE codusuario = %s"
        cursor.execute(sql, (nombreUsu, apellidosUsu, telefonoUsu, fechaNacUsu, correoUsu, id))
        db.commit()
        
        cursor.execute("SELECT id_datosUsu FROM datosUsuario WHERE codusuario = %s", (id,))
        datosConsulta = cursor.fetchone()
        
        if datosConsulta is None:
            sqlDatos = "INSERT INTO datosUsuario (direccionUsu, ciudadUsu, descripcionAcercaUsu, sitioWebUsu, blogUsu, codusuario) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sqlDatos, (direccionUsu, ciudadUsu, descripcionAcerca, sitioWeb, blog, id))
            db.commit()
        else:
            sqlDatos = "UPDATE datosUsuario SET direccionUsu = %s, ciudadUsu = %s, descripcionAcercaUsu = %s, sitioWebUsu = %s, blogUsu = %s WHERE codusuario = %s"
            cursor.execute(sqlDatos, (direccionUsu, ciudadUsu, descripcionAcerca, sitioWeb, blog, id))
            db.commit()
        
        flash('Datos actualizados correctamente', 'success')
        cursor.close()
        return redirect(url_for('usuarios.perfil_usuario'))
    else:
        cursor.execute('SELECT nombreusu, apellidousu, telusu, fechanac_usu, correousu FROM usuario WHERE codusuario = %s', (id,))
        data = cursor.fetchone()
        
        cursor.execute('SELECT ruta_foto FROM fotos_usuario WHERE cod_usuario = %s AND tipo_foto = "perfil" ORDER BY id_foto DESC LIMIT 1', (id,))
        foto_perfil_data = cursor.fetchone()
        
        foto_perfil = normalize_path(foto_perfil_data[0]) if foto_perfil_data else "/static/img/perfil_user.png"
        
        cursor.execute('SELECT direccionUsu, ciudadUsu, descripcionAcercaUsu, sitioWebUsu, blogUsu FROM datosUsuario WHERE codusuario = %s', (id,))
        datos = cursor.fetchone()
        
        if datos is None:
            datos = {}
    
    return render_template('editarPerfil_user.html', foto_perfil=foto_perfil, usuario=data, user_id=id, datos=datos)
#*****************************************Ruta del index principal de usuario **************************************************************
@usuarios.route('/index_user')
def index_user():
    user_id = session.get('user_id')
    return render_template('index_user.html', user_id = user_id)

@usuarios.route('/nosotros_user')
def nosotros_user():
    user_id = session.get('user_id')
    return render_template('MVQ_user.html',user_id = user_id)


#***********************************************Rutas para el manejo de favoritos********************************************************************
@usuarios.route('/favoritos_user')
def favoritos_user():
    user_id = session.get('user_id')
    return render_template('favoritos.html',user_id = user_id)

@usuarios.route('/agregar_favorito/usuario', methods=['POST'])
def agregar_favorito():
    user_id = session.get('user_id')
    
    if not user_id:
        return jsonify({'success': False, 'message': 'Usuario no autenticado'})
    
    fav_id = request.form['id']
    fav_type = request.form['tipo']

    # Verificar si el favorito ya existe
    sql_existente = 'SELECT idfavorito FROM favoritosUsuario WHERE codusuario = %s AND entidad_id = %s AND entidad_tipo = %s'
    cursor.execute(sql_existente, (user_id, fav_id, fav_type))
    favoritoExiste = cursor.fetchone()
    
    if favoritoExiste:
        return jsonify({'success': False, 'message': 'El favorito ya existe'})
    
    # Agrega el favorito a la sesión
    if 'favoritesUser' not in session:
        session['favoritesUser'] = []
        
    session['favoritesUser'].append({'id': fav_id, 'type': fav_type})
    session.modified = True
    print("sesion agregar: " , session['favoritesUser'])
    
    # Inserta el favorito en la base de datos
    cursor.execute('INSERT INTO favoritosUsuario (codusuario, entidad_id, entidad_tipo) VALUES (%s, %s, %s)', (user_id, fav_id, fav_type))
    db.commit()
    
    return jsonify({'success': True, 'message': 'Favorito agregado'})



@usuarios.route('/remover_favorito/usuario', methods=['POST'])
def remover_favorito():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'message': 'Usuario no autenticado'})
    
    fav_id = request.form['id']
    fav_type = request.form['tipo']

    # Elimina el favorito de la sesión
    if 'favoritesUser' in session:
        session['favoritesUser'] = [fav for fav in session['favoritesUser'] if not (fav['id'] == fav_id and fav['type'] == fav_type)]
        session.modified = True
    
    print("sesion eliminar: " , session['favoritesUser'])
    
    # Elimina el favorito de la base de datos
    cursor.execute('DELETE FROM favoritosUsuario WHERE codusuario = %s AND entidad_id = %s AND entidad_tipo = %s', (user_id, fav_id, fav_type))
    db.commit()

    return jsonify({'success': True, 'message': 'Favorito eliminado'})


@usuarios.route('/obtener_favoritos/usuario', methods=['GET'])
def obtener_favoritos():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'message': 'Usuario no autenticado'})

    cursor.execute('SELECT entidad_id, entidad_tipo FROM favoritosUsuario WHERE codusuario = %s', (user_id,))
    
    favoritos = cursor.fetchall()

    # Convertir las filas en una lista de diccionarios
    favoritos_list = [{'entidad_id': fav[0], 'entidad_tipo': fav[1]} for fav in favoritos]
    
    return jsonify(favoritos_list)

def obtener_favoritos_usuario(entidad_tipo):
    try:
        db = get_db()
        cursor = db.cursor()

        if entidad_tipo == 'restaurante':
            query = """
            SELECT DISTINCT
                fa.idfavorito, fa.codusuario, fa.entidad_id, fa.entidad_tipo, fa.fecha_agregado, 
                res.idresta, res.nombreresta, res.logo AS logo_res, res.tiporesta
            FROM favoritosUsuario fa
            LEFT JOIN restaurantes res ON fa.entidad_id = res.idresta
            WHERE fa.codusuario = %s AND fa.entidad_tipo = %s
            ORDER BY fa.fecha_agregado DESC;
            """
        elif entidad_tipo == 'emprendimiento':
            query = """
            SELECT DISTINCT
                fa.idfavorito, fa.codusuario, fa.entidad_id, fa.entidad_tipo, fa.fecha_agregado, 
                em.idempre, em.nombreempre, em.logo AS logo_empre, em.tipoempre
            FROM favoritosUsuario fa
            LEFT JOIN emprendimientos em ON fa.entidad_id = em.idempre
            WHERE fa.codusuario = %s AND fa.entidad_tipo = %s
            ORDER BY fa.fecha_agregado DESC;
            """
        elif entidad_tipo == 'evento':
            query = """
            SELECT DISTINCT
                fa.idfavorito, fa.codusuario, fa.entidad_id, fa.entidad_tipo, fa.fecha_agregado, 
                eve.ideven, eve.nombreeven, eve.logo AS logo_evento, eve.tipoevento 
            FROM favoritosUsuario fa
            LEFT JOIN eventos eve ON fa.entidad_id = eve.ideven
            WHERE fa.codusuario = %s AND fa.entidad_tipo = %s
            ORDER BY fa.fecha_agregado DESC;
            """
        else:
            return jsonify({'error': 'Tipo de entidad no soportado'}), 400

        user_id = session.get('user_id')  # Asumiendo que user_id está en la sesión
        cursor.execute(query, (user_id, entidad_tipo))
        favoritos = cursor.fetchall()

        favoritos_list = []
        for favorito in favoritos:
            logo_path = f"/static/{favorito[7].replace('\\', '/')}"
            favoritos_list.append({
                'fecha_publicacion': favorito[4],
                'idFav': favorito[0],
                'id': favorito[5],
                'logo': logo_path,
                'nombre': favorito[6],
                'tipo': favorito[3]
            })

        # Cerrar cursor y conexión
        cursor.close()
        db.close()

        # Devuelve los resultados en formato JSON
        return jsonify({"favoritos": favoritos_list})

    except Exception as e:
        return jsonify({"error": str(e)})

@usuarios.route('/Listafavoritos_usuario/restaurantes', methods=['GET'])
def obtener_favoritos_restaurantes():
    return obtener_favoritos_usuario('restaurante')

@usuarios.route('/Listafavoritos_usuario/emprendimientos', methods=['GET'])
def obtener_favoritos_emprendimientos():
    return obtener_favoritos_usuario('emprendimiento')

@usuarios.route('/Listafavoritos_usuario/eventos', methods=['GET'])
def obtener_favoritos_eventos():
    return obtener_favoritos_usuario('evento')


@usuarios.route('/limpiar_sesion_favoritos', methods=['POST'])
def limpiar_sesion_favoritos():
    # Limpia la sesión de favoritos
    session.pop('favoritesUser', None)
    return jsonify({'success': True, 'message': 'Sesión de favoritos limpiada'})

#Formatear los slashes para las imagenes
def normalize_path(path):
    """Convierte backslashes a slashes en una ruta y asegura que empieza con '/'."""
    normalized_path = path.replace('\\', '/')
    if not normalized_path.startswith('/'):
        normalized_path = '/' + normalized_path
    return normalized_path

