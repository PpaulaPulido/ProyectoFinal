from flask import Blueprint, request, render_template, redirect, url_for, flash,current_app,send_from_directory,abort,session,jsonify
from werkzeug.utils import secure_filename
from datetime import datetime,timedelta
from db import get_db, get_cursor
import os


res = Blueprint('res', __name__)
db = get_db()
cursor = get_cursor(db)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#*********************************Resetear la publicaicon de emprendimiento para registrar uno nuevo*******************************************
@res.route('/resetRestaurante')
def resetRestaurante():
    session.pop('res_id', None)
    session.pop('form_data', None)
    return redirect(url_for('res.publicacionRes'))

#*********************************Ruta para el formualrio de restaurantes parte 1************************************************
@res.route('/publicacionRes',methods=['GET', 'POST'])
def publicacionRes():
    
    current_app.config['FOLDER_RES'] = os.path.join(current_app.root_path, 'static', 'galeriaRes')
    codadmin = session.get('admin_id') 
    
    if request.method == 'GET' and request.args.get('nuevo', '0') == '1':
        # Si se especifica que es un nuevo restaurante, resetear la sesión
        session.pop('res_id', None)
        session.pop('form_data', None)
    
    res_id = session.get('res_id')
    form_data = session.get('form_data', {})
    relativePath = None 
    
    if request.method == 'POST':
        
        logoRes = request.files.get("logoRes")
        galeria = request.files.getlist('galeria[]')
        
        if logoRes and allowed_file(logoRes.filename):
            filename = secure_filename(logoRes.filename)
            path = os.path.join(current_app.config['FOLDER_RES'], filename)
            logoRes.save(path) 
            relativePath =  os.path.join('galeriaRes',filename)
        
        diccionarioRes = {
            "nombreRes": request.form.get("nombreRes"),
            "tipoRes": request.form.get("typeRes"),
            "descripcionRes": request.form.get("descripcionRes"),
            "paginaRes": request.form.get("paginaRes"),
            "menu": request.form.get("menu"),
            "horarioRes": request.form.get("horarioRes"),
            "horarioE": request.form.get("entrada"),
            "horarioS": request.form.get("salida"),
            "correoRes": request.form.get("correoRes"),
            "contactoRes": request.form.get("contactoRes"),
            "redInstagram": request.form.get("redInstagram"),
            "redTiktok": request.form.get("redTiktok"),
        }
        
        if relativePath:
            diccionarioRes["logo"] = relativePath
        
        form_data.update(diccionarioRes)
        session['form_data'] = form_data
        
        codadmin = session.get('admin_id') 
        cursor = db.cursor()
        
        if not res_id:
            fechaPublicacion = datetime.now().date()
            cursor.execute(" INSERT INTO restaurantes (nombreresta, logo, tiporesta, descripresta, paginaresta, menu, horario, horarioApertura, horarioCierre, correoresta, telresta, fecha_publicacion, codadmin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ", (form_data["nombreRes"], form_data["logo"], form_data["tipoRes"], form_data["descripcionRes"], form_data["paginaRes"], form_data["menu"], form_data["horarioRes"], form_data["horarioE"], form_data["horarioS"], form_data["correoRes"], form_data["contactoRes"], fechaPublicacion, codadmin))
            
            res_id = cursor.lastrowid
            session['res_id'] = res_id
            
            
            #galeria de imagenes
            upload_folder = current_app.config['FOLDER_RES']
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            for imagen in galeria:
                if imagen and allowed_file(imagen.filename):
                    filename = secure_filename(imagen.filename)
                    path = os.path.join(current_app.config['FOLDER_RES'], filename)
                    imagen.save(path)
                    relative_path = os.path.join('galeriaRes', filename)  # Ruta relativa de la imagen
                    cursor.execute("INSERT INTO galeriaresta (idresta, imagenresta, descripcion) VALUES (%s, %s, %s)",
                                   (res_id, relative_path, "Imagen de la galería del restaurante"))
            
            # Insertar redes sociales
            if form_data["redInstagram"]:
                cursor.execute("INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) VALUES (%s, %s, %s, %s)", 
                   (res_id, 'restaurante', 'instagram', form_data["redInstagram"]))
                
            if form_data["redTiktok"]:
                cursor.execute("INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) VALUES (%s, %s, %s, %s)", 
                   (res_id, 'restaurante', 'tiktok', form_data["redTiktok"]))
            
            db.commit()
            cursor.close()
        
        else:
            cursor = db.cursor()
            cursor.execute("UPDATE restaurantes SET nombreresta = %s, logo = %s, tiporesta = %s, descripresta = %s, paginaresta = %s, menu = %s, horario = %s, horarioApertura = %s, horarioCierre = %s, correoresta = %s, telresta = %s WHERE idresta = %s ",(form_data["nombreRes"],form_data["logo"],form_data["tipoRes"],form_data["descripcionRes"],form_data["paginaRes"],form_data["menu"],form_data["horarioRes"],form_data["horarioE"],form_data["horarioS"],form_data["correoRes"],form_data["contactoRes"],res_id))
            
            if form_data["redInstagram"]:
                cursor.execute("UPDATE redes_sociales SET url = %s WHERE entidad_id = %s AND entidad_tipo = %s AND red = %s", (form_data["redInstagram"], res_id, 'restaurante', 'instagram'))
            if form_data["redTiktok"]:
                cursor.execute("UPDATE redes_sociales SET url = %s WHERE entidad_id = %s AND entidad_tipo = %s AND red = %s", (form_data["redTiktok"], res_id, 'restaurante', 'tiktok'))
                
            db.commit()
            cursor.close()
        
        flash('Restaurante registrado correctamente', 'success')
        return redirect(url_for("res.restauranteLocation"))
        
    return render_template('publicacionRes.html',datos = form_data,res_id = res_id,admin_id = codadmin)

#*************************************Ruta de registro de restaurante parte 2***********************************************
@res.route('/restauranteLocation',methods=['GET', 'POST'])
def restauranteLocation():
    
    res_id = session.get('res_id')
    admin_id = session.get('admin_id')
    if request.method == 'POST':
        ubicaciones = request.form.getlist('direcciones[]')
        for ubicacion in ubicaciones:
            if ubicacion:  # Comprobar que la ubicación no este vacía
                cursor.execute("INSERT INTO ubicacionresta (idresta, ubicacion) VALUES (%s, %s)", (res_id, ubicacion))
        db.commit()
        flash('Ubicaciones guardadas correctamente')
        return redirect(url_for('admin.index_admin'))
    return render_template('publicacionRes2.html',admin_id = admin_id)


#**************************************************Editar restaurante**************************************************************
@res.route('/editarRestaurante/<int:id>', methods=['GET', 'POST'])
def editarRes(id):
    db = get_db()
    cursor = db.cursor()
    
    codadmin = session.get('admin_id')
    
    if request.method == 'POST':
        # Manejo de logo_Res
        logoRes = request.files.get("logo_Res")
        relativePath = None
        
        if logoRes and allowed_file(logoRes.filename):
            filename = secure_filename(logoRes.filename)
            path = os.path.join(current_app.config['FOLDER_RES'], filename)
            logoRes.save(path)
            relativePath = os.path.join('galeriaRes', filename)

        # Resto de los datos del formulario
        nombre_Res = request.form.get('nombre_Res')
        type_Res = request.form.get('type_Res')
        horario_Res = request.form.get('horario_Res')
        horarioEntradaRes = request.form.get('horarioEntradaRes')
        horarioSalidaRes = request.form.get('horarioSalidaRes')
        pagina_Res = request.form.get('pagina_Res')
        menu_Res = request.form.get('menu_Res')
        descripcion_Res = request.form.get('descripcion_Res')
        red_Instagram = request.form.get('red_Instagram')
        red_Tiktok = request.form.get('red_Tiktok')
        correo_Res = request.form.get('correo_Res')
        contacto_Res = request.form.get('contacto_Res')
        fechaPublicacion = datetime.now().date()

        # Actualización de la tabla restaurantes
        sql_res = """
            UPDATE restaurantes SET 
            nombreresta = %s, logo = %s, tiporesta = %s, descripresta = %s, paginaresta = %s, menu = %s, horario = %s, 
            horarioApertura = %s, horarioCierre = %s, correoresta = %s, telresta = %s, fecha_publicacion = %s 
            WHERE idresta = %s AND codadmin = %s
        """
        cursor.execute(sql_res, (nombre_Res, relativePath, type_Res, descripcion_Res, pagina_Res, menu_Res, horario_Res,
                                 horarioEntradaRes, horarioSalidaRes, correo_Res, contacto_Res, fechaPublicacion, id, codadmin))

        # Actualización de redes sociales (Instagram y Tiktok)
        sql_redes = """
            UPDATE redes_sociales SET 
            url = %s 
            WHERE entidad_id = %s AND entidad_tipo = %s AND red = %s
        """
        # Actualizar Instagram
        entidad_tipo = 'restaurante'
        cursor.execute(sql_redes, (red_Instagram, id, entidad_tipo, 'Instagram'))
        
        # Actualizar Tiktok
        cursor.execute(sql_redes, (red_Tiktok, id, entidad_tipo, 'Tiktok'))

        # Eliminar galería existente y subir nueva galería
        cursor.execute("DELETE FROM galeriaresta WHERE idresta = %s", (id,))
        galeria = request.files.getlist('galeriaRes[]')
        for imagen in galeria:
            if imagen and allowed_file(imagen.filename):
                filename = secure_filename(imagen.filename)
                path = os.path.join(current_app.config['FOLDER_RES'], filename)
                imagen.save(path)
                relative_path = os.path.join('galeriaRes', filename)
                cursor.execute("INSERT INTO galeriaresta (idresta, imagenresta, descripcion) VALUES (%s, %s, %s)",
                               (id, relative_path, "Imagen de la galería del restaurante"))

        db.commit()
        cursor.close()
        return redirect(url_for('res.editarResUbicacion', id=id))
    
    else:
        # Obtener los datos actuales del restaurante para prellenar el formulario
        sql_select_restaurante = "SELECT * FROM restaurantes WHERE idresta = %s"
        cursor.execute(sql_select_restaurante, (id,))
        restaurante = cursor.fetchone()

        sql_select_redes = "SELECT red, url FROM redes_sociales WHERE entidad_id = %s AND entidad_tipo = 'restaurante'"
        cursor.execute(sql_select_redes, (id,))
        redes = cursor.fetchall()
        redes_sociales = {red.lower(): url for red, url in redes}

        cursor.close()

        # Preparar datos para enviar al template
        datos_res = {
            'nombre_res': restaurante[1],
            'tipo_res': restaurante[3],
            'contacto_res': restaurante[11],
            'correo_res': restaurante[10],
            'descripcion_res': restaurante[4],
            'pagina_res': restaurante[5],
            'horario_res': restaurante[7],
            'horarioEntradaRes': restaurante[8],
            'horarioSalidaRes': restaurante[9],
            'menu_res': restaurante[6],
            'red_Instagram': redes_sociales.get('instagram', ''),
            'red_Tiktok': redes_sociales.get('tiktok', ''),
        }

        return render_template('editarRestaurante1.html', datos_res=datos_res, res_id=id, admin_id=codadmin)

                
@res.route('/editarResUbicacion/<int:id>/', methods=['GET', 'POST'])
def editarResUbicacion(id):
    db = get_db()
    cursor = db.cursor()

    codadmin = session.get('admin_id')
    
    sql_select_res = "SELECT * FROM restaurantes WHERE idresta = %s"
    cursor.execute(sql_select_res, (id,))
    restaurante= cursor.fetchone()
    
    if not restaurante:
        flash('El restaurante especificado no existe', 'error')
        return redirect(url_for('admin.index_admin'))
    
    if request.method == 'POST':
        ubicaciones = request.form.getlist('direccionesEditar[]')
        try:
            # Eliminar las ubicaciones actuales del evento
            cursor.execute("DELETE FROM ubicacionresta WHERE idresta = %s", (id,))
            
            # Insertar las nuevas ubicaciones
            for ubicacion in ubicaciones:
                if ubicacion:  # Comprobar que la ubicación no esté vacía
                    cursor.execute("INSERT INTO  ubicacionresta(idresta, ubicacion) VALUES (%s, %s)", (id, ubicacion))
            
            db.commit()
            flash('Ubicaciones actualizadas correctamente', 'success')
            return redirect(url_for('admin.index_admin'))
        
        except Exception as e:
            db.rollback()
            flash(f'Error al actualizar las ubicaciones: {str(e)}', 'error')
            return redirect(url_for('res.editarRes', id=id))
    
    # Obtener las ubicaciones actuales del evento para prellenar el formulario
    sql_select_ubicaciones = "SELECT ubicacion FROM ubicacionresta WHERE idresta = %s"
    cursor.execute(sql_select_ubicaciones, (id,))
    ubicaciones = [ubicacion[0] for ubicacion in cursor.fetchall()]
    cursor.close()
        
    return render_template('editarRestaurante2.html', admin_id=codadmin, res_id=id)

#*************************************Ruta apra eliminar restaurante*****************************************************
@res.route('/eliminarRestaurante/<int:id>', methods=['GET', 'POST'])
def eliminarRestaurante(id):
    db = get_db()
    cursor = db.cursor()

    try:
        # Eliminar entradas de la tabla galeriaresta
        cursor.execute("DELETE FROM galeriaresta WHERE idresta = %s", (id,))
        
        # Eliminar entradas de la tabla ubicacionresta
        cursor.execute("DELETE FROM ubicacionresta WHERE idresta = %s", (id,))
        
        # Eliminar entradas de la tabla redes_sociales
        cursor.execute("DELETE FROM redes_sociales WHERE entidad_id = %s AND entidad_tipo = 'restaurante'", (id,))
        
        # Eliminar el restaurante
        cursor.execute("DELETE FROM restaurantes WHERE idresta = %s", (id,))
        
        db.commit()
        flash('Restaurante eliminado con éxito', 'success')
    except Exception as e:
        db.rollback()
        flash(f'Error al eliminar el restaurante: {str(e)}', 'error')
    finally:
        cursor.close()

    return redirect(url_for('admin.index_admin'))
#********************************************************Ruta para json de detalles******************************************************************
@res.route('/restauranteDetalleJson/<int:id>', methods=['GET'])
def detallesResJson(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    
    try:
        if request.method == 'GET':
            sql = '''
                SELECT 
                    r.idresta,
                    r.nombreresta,
                    r.logo AS logo_filename,
                    r.tiporesta,
                    r.descripresta,
                    r.paginaresta,
                    r.menu,
                    r.horario,
                    r.horarioApertura,
                    r.horarioCierre,
                    r.correoresta,
                    r.telresta,
                    r.fecha_publicacion,
                    adm.nombreadmin AS administrador,
                    adm.apellidoadmin AS apellidoAdm,
                    GROUP_CONCAT(DISTINCT  gr.imagenresta SEPARATOR '; ') AS imagenes_restaurante,
                    GROUP_CONCAT(DISTINCT gr.descripcion SEPARATOR '; ') AS descripcion_imagenes,
                    GROUP_CONCAT(DISTINCT ur.ubicacion SEPARATOR '; ') AS ubicaciones_restaurante,
                    GROUP_CONCAT(DISTINCT CONCAT(rs.red, ': ', rs.url) SEPARATOR '; ') AS redes_sociales
                FROM 
                    restaurantes r
                LEFT JOIN administrador adm ON r.codadmin = adm.codadmin
                LEFT JOIN galeriaresta gr ON r.idresta = gr.idresta
                LEFT JOIN ubicacionresta ur ON r.idresta = ur.idresta
                LEFT JOIN redes_sociales rs ON r.idresta = rs.entidad_id AND rs.entidad_tipo = 'restaurante'
                WHERE
                    r.idresta = %s
                GROUP BY
                    r.idresta
                ORDER BY
                    r.fecha_publicacion DESC
            '''
            cursor.execute(sql, (id,))
            restaurante = cursor.fetchone()
            if restaurante:
                
                if restaurante['logo_filename']:
                    normalized_logo_filename = restaurante['logo_filename'].replace('\\', '/')
                    logo_url = url_for('static', filename=normalized_logo_filename)
                else:
                    logo_url = url_for('static', filename='img/notFound.png')
                    
                restaurante['logo'] = logo_url
                
                # Convertir objetos timedelta a string si es necesario
                for key, value in restaurante.items():
                    if isinstance(value, timedelta):  # Revisar si el valor es de tipo timedelta
                        # Convertir timedelta a string en formato HH:MM:SS
                        restaurante[key] = str(value)
                    elif isinstance(value, str):  # Revisar si el valor es una cadena
                        # Corregir caracteres de escape en la cadena
                        restaurante[key] = value.replace('\\', '/')
                return jsonify(restaurante)
            else:
                # No se encontró ningún restaurante con el idresta dado
                return jsonify({'error': 'Restaurante no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': 'Error en el servidor: {}'.format(e)}), 500
    finally:
        cursor.close()
        db.close()

@res.route('/restauranteDetalleServidor')
def restauranteDetalleServidor():
    user_id = session.get('user_id')
    admin_id = session.get('admin_id')
    return render_template('detalleServidorRes.html',user_id = user_id,admin_id = admin_id)

@res.route('/restauranteDetalleServidorAdmin')
def restauranteDetalleServidorAdmin():
    admin_id = session.get('admin_id')
    return render_template('detalleServidorResAdmin.html',admin_id = admin_id)


#********************************************Rutas para html estaticos*************************************
@res.route('/restauranteDetalle')
def restauranteDetalle():
    user_id = session.get('user_id')
    return render_template('detalle_res.html',user_id = user_id)

@res.route('/detalleRestaurante/administrador')
def detalleRestauranteAdmin():
    admin_id = session.get('admin_id')
    return render_template('detalle_res_admin.html',admin_id = admin_id)

@res.route('/SeccionRestaurante')
def sectionRes():
    user_id = session.get('user_id')
    admin_id = session.get('admin_id')
    return render_template('seccion_res.html',user_id = user_id,admin_id = admin_id)

@res.route('/SeccionRestauranteAdmin')
def sectionResAdmin():
    admin_id = session.get('admin_id')
    return render_template('seccion_res_admin.html',admin_id = admin_id)


    