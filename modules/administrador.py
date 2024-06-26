from flask import Blueprint, request, render_template, redirect, url_for, flash,current_app,send_from_directory,abort,jsonify,session
from werkzeug.utils import secure_filename
#from werkzeug.security import generate_password_hashz
from db import get_db, get_cursor
import os

admin = Blueprint('admin', __name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

db = get_db()
cursor = get_cursor(db)

#***********************************************Ruta de formulario contacto***********************************************
@admin.route('/enviar', methods=['POST'])
def enviar():
    
    db = get_db()  # Obtener la conexión a la base de datos
    cursor = db.cursor()  # Crear un cursor
    
    nombre = request.form.get('nombreContacto')
    email = request.form.get('emailContacto')
    tema = request.form.get('tema')
    mensaje = request.form.get('mensaje')
    
    # Almacenar en la base de datos
    try:
        cursor.execute("""
            INSERT INTO mensajes_contacto (nombre, email, tema, mensaje)
            VALUES (%s, %s, %s, %s)
        """, (nombre, email, tema, mensaje))
        db.commit()
        return redirect(url_for('admin.indexPrincipal'))
    except Exception as e:
        print(f"Error al insertar en la base de datos: {e}")
        db.rollback()  # En caso de error, hacer rollback para deshacer cambios
        return "Error al enviar el mensaje"

#*********************************Funcion para permitir tipo de extensiones para las img********************************
''' se utiliza para verificar si el nombre de un archivo tiene una extensión permitida según una lista de extensiones '''
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@admin.route('/index_admin')
def index_admin():
    admin_id = session.get('admin_id')
    return render_template('index_admin.html',admin_id=admin_id)


#***********************************Ruta para perfil de administrador************************************
@admin.route('/perfil_admin')
def perfil_admin():
    
    admin_id = session.get('admin_id')
    
    if not admin_id:
        flash('No está autenticado.', 'error')
        return redirect(url_for('usuarios.inicio_sesion')) 
    db = get_db()  # Obtener la conexión a la base de datos
    cursor = db.cursor()  # Crear un cursor

    default_portada = '/static/img/Portada-Bogota.jpg'
    default_perfil = '/static/img/perfil_user.png'

    try:
        cursor.execute("SELECT nombreadmin,apellidoadmin,correoadmin FROM administrador WHERE codadmin = %s", (admin_id,))
        admin_datos= cursor.fetchone()
        if admin_datos:
            nombre_admin, apellido_admin, correo_admin = admin_datos
        else:
            nombre_admin = apellido_admin = correo_admin = "Información no disponible"
        
        cursor.execute("SELECT direccion,ciudad,descripcionAcerca,sitioWeb,blog FROM datosAdmin WHERE cod_admin = %s",(admin_id,))
        admin_datosDetalles = cursor.fetchone()
        
        if admin_datosDetalles:
            direccion, ciudad, descripcionAcerca, sitioWeb, blog = admin_datosDetalles
        else:
            direccion = ciudad = descripcionAcerca = sitioWeb = blog = "No disponible"
        
        def obtenerImagen(image_type, default_image):
            cursor.execute("SELECT ruta_foto FROM fotos_admin WHERE cod_admin = %s AND tipo_foto = %s ORDER BY id_foto DESC LIMIT 1", (admin_id, image_type))
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

    return render_template('perfil_admin.html',admin_id = admin_id ,nombre_admin = nombre_admin, apellido_admin = apellido_admin, correo_admin = correo_admin, foto_portada=fotoPortada, foto_perfil=fotoPerfil,direccion = direccion, ciudad = ciudad,sitioWeb = sitioWeb,blog = blog,descripcionAcerca = descripcionAcerca)

#******************************************Ruta para mis fotos de perfil admin*****************************************************************
@admin.route('/MisFotos')
def photos():
    
    user_id = session.get('admin_id')
    if not user_id:
        flash('No está autenticado.', 'error')
        return redirect(url_for('usuarios.inicio_sesion')) 
    
    db = get_db()
    cursor = db.cursor()
    
    try:
        cursor.execute("""
            SELECT ruta_foto, tipo_foto FROM fotos_admin
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

#******************************************Galeria de fotos del admin*******************************************************
@admin.route('/galeriaAdmin')
def galeria_admin():
    
    user_id = session.get('admin_id')
    
    if not user_id:
        flash('No está autenticado.', 'error')
        return redirect(url_for('usuarios.inicio_sesion')) 
    
    db = get_db()
    cursor = db.cursor()
    
    try:
        cursor.execute("""
            SELECT ruta_foto, tipo_foto FROM fotos_admin
    
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

#*********************************************Ruta para las reseñas del administrador******************************
@admin.route('/reseñasAdmin')
def resena_admin():
    admin_id = session.get('admin_id')
    
    if not admin_id:
        flash('No está autenticado.', 'error')
        return redirect(url_for('usuarios.inicio_sesion')) 
    
    db = get_db()
    cursor = db.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT R.calificacion, R.comentario, R.entidad_tipo, R.entidad_id FROM Resenas AS R WHERE R.autor_tipo = 'administrador' AND R.autor_id = %s ORDER BY R.id_resena DESC LIMIT 5", (admin_id,))
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

    
#****************************Ruta para la imagen de perfil************************************************************
@admin.route('/perfil_imagen')
def perfil_imagen():
    
    user_id = session.get('admin_id')
    
    if not user_id:
        flash('No está autenticado.', 'error')
        return redirect(url_for('usuarios.inicio_sesion')) 
    
    db = get_db()
    cursor = get_cursor(db)
    
    cursor.execute("SELECT ruta_foto FROM fotos_admin  WHERE cod_admin= %s AND tipo_foto = 'perfil' ORDER BY id_foto DESC LIMIT 1", (user_id,))
    foto_perfil = cursor.fetchone()
    
    if foto_perfil:
        foto_perfil_path = foto_perfil[0] 
    else:
        foto_perfil_path = None
    
    if foto_perfil_path:
        directory_path = os.path.join(current_app.root_path, 'static', 'uploads') 
        file_name = os.path.basename(foto_perfil_path)  # Extrae el nombre del archivo
    else:
        # Manejar el caso en que no hay foto de perfil configurada
        directory_path = os.path.join(current_app.root_path, 'static', 'img')  # Ruta al directorio de imágenes por defecto
        file_name = 'perfil_user.png'  # Nombre de una imagen por defecto

    # Verificar si el archivo realmente existe
    full_file_path = os.path.join(directory_path, file_name)
    if not os.path.isfile(full_file_path):
        print(f"Archivo no encontrado: {full_file_path}")  # Log para depuración
        abort(404)  # Si el archivo no existe, devuelve un error 404
    
    cursor.close()
    db.close()
    
    return send_from_directory(directory_path, file_name)

#*******************************Ruta para subir la foto de perfil ********************************************************************************
@admin.route('/subir_fotoPerfil', methods=['POST'])
def subir_fotoperfil():
    
    user_id = session.get('admin_id')
    cursor = db.cursor()

    if not user_id:
        flash('No está autenticado.', 'error')
        return redirect(url_for('usuarios.inicio_sesion')) 
    
    file = request.files.get('fotoPerfil')
    
    if file and allowed_file(file.filename):
        
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        cursor.execute("""
            INSERT INTO fotos_admin (cod_admin, ruta_foto, tipo_foto)
            VALUES (%s, %s, 'perfil')
            ON DUPLICATE KEY UPDATE ruta_foto = VALUES(ruta_foto)
        """, (user_id, file_path))
        
        db.commit()

        flash('Foto de portada actualizada con éxito.')
        cursor.close()
        return redirect(url_for('admin.perfil_admin'))
    
    else:
        flash('No se seleccionó archivo o el tipo de archivo no está permitido.')
        return redirect(url_for('admin.perfil_admin'))

#*******************************Ruta para subir la foto de Portada********************************************************************************
@admin.route('/subir_portada', methods=['POST'])
def subir_portada():
    
    user_id = session.get('admin_id')
    cursor = db.cursor()
    
    if not user_id:
        flash('No está autenticado.', 'error')
        return redirect(url_for('usuarios.inicio_sesion')) 
    
    # Intenta obtener el archivo con el nombre 'fotoPortada' del formulario enviado. Si no hay archivo, 'file' será None.
    file = request.files.get('fotoPortada')
    
    # Verifica primero si se obtuvo un archivo y luego si el archivo tiene una extensión permitida.
    if file and allowed_file(file.filename):
        # 'secure_filename' sanea el nombre del archivo para asegurarse de que es seguro de usar en el sistema de archivos.
        filename = secure_filename(file.filename)
        
        # Construye una ruta completa donde se guardará el archivo, usando el directorio configurado para subidas.
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        
        # Guarda el archivo en el sistema de archivos del servidor.
        file.save(file_path)

        # Ejecuta una consulta SQL para insertar o actualizar la ruta de la foto de portada en la base de datos.
        cursor.execute("""
            INSERT INTO fotos_admin (cod_admin, ruta_foto, tipo_foto)
            VALUES (%s, %s, 'portada')
            ON DUPLICATE KEY UPDATE ruta_foto = VALUES(ruta_foto)
        """, (user_id, file_path))
        
        # Confirma los cambios en la base de datos.
        db.commit()
        
        # Muestra un mensaje al usuario indicando que la foto de portada ha sido actualizada con éxito.
        flash('Foto de portada actualizada con éxito.')
        
        # Redirecciona al usuario de vuelta a la página 'perfil_admin'.
        return redirect(url_for('admin.perfil_admin'))
    
    else:
        # Si no se subió un archivo o el tipo de archivo no es permitido, muestra un mensaje de error.
        flash('No se seleccionó archivo o el tipo de archivo no está permitido.')
        
        # Redirecciona al usuario de vuelta a la página 'perfil_admin' para mantenerlo en la misma página en caso de error.
        return redirect(url_for('admin.perfil_admin'))

#***********************************************Ruta de editar perfil administrador**********************************************************
@admin.route('/editarPerfilAdmin/<int:id>', methods=['POST', 'GET'])
def editarPerfilAdmin(id):
    
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        nombreAdmin = request.form.get('nombreAdmin')
        apellidosAdmin = request.form.get('apellidosAdmin')
        correoAdmin = request.form.get('correoAdmin')
        telefonoAdmin = request.form.get('telefonoAdmin')
        fechaNacAdmin = request.form.get('fechaNacAdmin')
        
        direccionAdmin = request.form.get('direccion')
        ciudadAdmin = request.form.get('ciudad')
        descripcionAcerca = request.form.get('acerca')
        sitioWeb = request.form.get('sitioWeb')
        blog = request.form.get('blog')

        sql = "UPDATE administrador SET nombreadmin = %s, apellidoadmin = %s, telfadmin = %s, correoadmin = %s, fechanac_admin = %s WHERE codadmin = %s"
        cursor.execute(sql, (nombreAdmin, apellidosAdmin, telefonoAdmin, correoAdmin, fechaNacAdmin, id))
        db.commit()
        
        cursor.execute("SELECT id_datosAdmin FROM datosAdmin WHERE cod_admin = %s", (id,))
        datosConsulta = cursor.fetchone()
        
        if datosConsulta is None:
            sqlDatos = "INSERT INTO datosAdmin (direccion, ciudad, descripcionAcerca, sitioWeb, blog, cod_admin) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sqlDatos, (direccionAdmin, ciudadAdmin, descripcionAcerca, sitioWeb, blog, id))
            db.commit()
        else:
            sqlDatos = "UPDATE datosAdmin SET direccion = %s, ciudad = %s, descripcionAcerca = %s, sitioWeb = %s, blog = %s WHERE cod_admin = %s"
            cursor.execute(sqlDatos, (direccionAdmin, ciudadAdmin, descripcionAcerca, sitioWeb, blog, id))
            db.commit()
        
        flash('Datos actualizados correctamente', 'success') 
        cursor.close()
        return redirect(url_for('admin.perfil_admin'))
    else:
        
        cursor.execute('SELECT nombreadmin, apellidoadmin, telfadmin, correoadmin, fechanac_admin FROM administrador WHERE codadmin = %s', (id,))
        data = cursor.fetchone()
        
        # Obtener la ruta de la foto de perfil desde la base de datos
        cursor.execute('SELECT ruta_foto FROM fotos_admin WHERE cod_admin = %s AND tipo_foto = "perfil" ORDER BY id_foto DESC LIMIT 1', (id,))
        foto_perfil_data = cursor.fetchone()
        
        foto_perfil = normalize_path(foto_perfil_data[0]) if foto_perfil_data else "/static/img/perfil_user.png"
        
        cursor.execute('SELECT direccion,ciudad,descripcionAcerca,sitioWeb,blog FROM datosAdmin WHERE cod_admin = %s',(id,))
        datos = cursor.fetchone()
        
        if datos is None:
            datos = {}
       
 
        return render_template('editarPerfil_admin.html',foto_perfil = foto_perfil, admin=data, admin_id=id, datos = datos)


@admin.route('/tipo_publicacion')
def tipoPublicacion():
    admin_id = session.get('admin_id')
    return render_template('tipo_publicacion.html',admin_id = admin_id)

#Formatear los slashes para las imagenes
def normalize_path(path):
    """Convierte backslashes a slashes en una ruta y asegura que empieza con '/'."""
    normalized_path = path.replace('\\', '/')
    if not normalized_path.startswith('/'):
        normalized_path = '/' + normalized_path
    return normalized_path


#*********************************************ruta de favoritos********************************************************
@admin.route('/favoritosAdmin')
def favoritosAdmin():
    admin_id = session.get('admin_id')
    return render_template('favoritosAdmin.html',admin_id = admin_id)

@admin.route('/agregar_favorito/admin', methods=['POST'])
def agregar_favorito_admin():
    admin_id = session.get('admin_id')
    
    if not admin_id:
        return jsonify({'success': False, 'message': 'Administrador no autenticado'})
    
    fav_id = request.form['id']
    fav_type = request.form['tipo']

    # Verificar si el favorito ya existe
    sql_existente = 'SELECT idfavorito FROM favoritosAdmin WHERE codadmin = %s AND entidad_id = %s AND entidad_tipo = %s'
    cursor.execute(sql_existente, (admin_id, fav_id, fav_type))
    favoritoExiste = cursor.fetchone()
    
    if favoritoExiste:
        return jsonify({'success': False, 'message': 'El favorito ya existe'})
    
    # Agrega el favorito a la sesión
    if 'favoritesAdmin' not in session:
        session['favoritesAdmin'] = []
        
    session['favoritesAdmin'].append({'id': fav_id, 'type': fav_type})
    session.modified = True
    print("sesion agregar: " , session['favoritesAdmin'])
    
    # Inserta el favorito en la base de datos
    cursor.execute('INSERT INTO favoritosAdmin  (codadmin, entidad_id, entidad_tipo) VALUES (%s, %s, %s)', (admin_id, fav_id, fav_type))
    db.commit()
    
    return jsonify({'success': True, 'message': 'Favorito agregado'})



@admin.route('/remover_favorito/admin', methods=['POST'])
def remover_favorito_admin():
    
    admin_id = session.get('admin_id')
    if not admin_id:
        return jsonify({'success': False, 'message': 'Administrador no autenticado'})
    
    fav_id = request.form['id']
    fav_type = request.form['tipo']

    # Elimina el favorito de la sesión
    if 'favoritesAdmin' in session:
        session['favoritesAdmin'] = [fav for fav in session['favoritesAdmin'] if not (fav['id'] == fav_id and fav['type'] == fav_type)]
        session.modified = True
    
    print("sesion eliminar: " , session['favoritesUser'])
    
    # Elimina el favorito de la base de datos
    cursor.execute('DELETE FROM favoritosAdmin WHERE codadmin = %s AND entidad_id = %s AND entidad_tipo = %s', (admin_id, fav_id, fav_type))
    db.commit()

    return jsonify({'success': True, 'message': 'Favorito eliminado'})


@admin.route('/obtener_favoritosAdmin', methods=['GET'])
def obtener_favoritos_admin():

    admin_id = session.get('admin_id')

    if not admin_id:
        return jsonify({'success': False, 'message': 'Administrador no autenticado'})

    cursor.execute('SELECT entidad_id, entidad_tipo FROM favoritosAdmin WHERE codadmin = %s', (admin_id,))
    
    favoritos = cursor.fetchall()

    # Convertir las filas en una lista de diccionarios
    favoritos_list = [{'entidad_id': fav[0], 'entidad_tipo': fav[1]} for fav in favoritos]
    
    return jsonify(favoritos_list)



def favoritos_admin(entidad_tipo):
    try:
        db = get_db()
        cursor = db.cursor()

        if entidad_tipo == 'restaurante':
            query = """
            SELECT DISTINCT
                fa.idfavorito, fa.codadmin, fa.entidad_id, fa.entidad_tipo, fa.fecha_agregado, 
                res.idresta, res.nombreresta, res.logo AS logo_res, res.tiporesta
            FROM favoritosAdmin fa
            LEFT JOIN restaurantes res ON fa.entidad_id = res.idresta
            WHERE fa.codadmin = %s AND fa.entidad_tipo = %s
            ORDER BY fa.fecha_agregado DESC;
            """
        elif entidad_tipo == 'emprendimiento':
            query = """
            SELECT DISTINCT
                fa.idfavorito, fa.codadmin, fa.entidad_id, fa.entidad_tipo, fa.fecha_agregado, 
                em.idempre, em.nombreempre, em.logo AS logo_empre, em.tipoempre
            FROM favoritosAdmin fa
            LEFT JOIN emprendimientos em ON fa.entidad_id = em.idempre
            WHERE fa.codadmin = %s AND fa.entidad_tipo = %s
            ORDER BY fa.fecha_agregado DESC;
            """
        elif entidad_tipo == 'evento':
            query = """
            SELECT DISTINCT
                fa.idfavorito, fa.codadmin, fa.entidad_id, fa.entidad_tipo, fa.fecha_agregado, 
                eve.ideven, eve.nombreeven, eve.logo AS logo_evento, eve.tipoevento 
            FROM favoritosAdmin fa
            LEFT JOIN eventos eve ON fa.entidad_id = eve.ideven
            WHERE fa.codadmin = %s AND fa.entidad_tipo = %s
            ORDER BY fa.fecha_agregado DESC;
            """
        else:
            return jsonify({'error': 'Tipo de entidad no soportado'}), 400

        
        admin_id = session.get('admin_id')

        if not admin_id:
            return jsonify({'success': False, 'message': 'Administrador no autenticado'})
        
        cursor.execute(query, (admin_id, entidad_tipo))
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

@admin.route('/Listafavoritos_admin/restaurantes', methods=['GET'])
def obtener_favoritos_restaurantes():
    return favoritos_admin('restaurante')

@admin.route('/Listafavoritos_admin/emprendimientos', methods=['GET'])
def obtener_favoritos_emprendimientos():
    return favoritos_admin('emprendimiento')

@admin.route('/Listafavoritos_admin/eventos', methods=['GET'])
def obtener_favoritos_eventos():
    return favoritos_admin('evento')

#************************************Rutas estaticas********************************************
@admin.route('/indexAdmin')
def indexPrincipal():
    admin_id = session.get('admin_id')
    return render_template('principal_admin.html',admin_id = admin_id)

@admin.route('/nosotros/administrador')
def nosotrosEmprenesy():
    admin_id = session.get('admin_id')
    return render_template('MVQ_admin.html',admin_id = admin_id)


