from flask import Blueprint, request, render_template, redirect, url_for, flash,current_app,send_from_directory,abort,session,jsonify
from werkzeug.utils import secure_filename
from datetime import datetime,timedelta
from db import get_db, get_cursor
import os

emprende = Blueprint('emprende', __name__)
db = get_db()
cursor = get_cursor(db)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#***************************************Restaurar formulario de emprendimiento*********************************************************
@emprende.route('/resetEmprende')
def resetEmprendimiento():
    session.pop('emprende_id', None)
    session.pop('form_data', None)
    return redirect(url_for('emprende.publicar_emprendimiento'))

#************************************************Registro de publicacion de emprendimiento parte 1***************************************************************************
@emprende.route('/publicacionEmprende',methods=['GET', 'POST'])
def publicar_emprendimiento():
    
    current_app.config['FOLDER_EMPREN'] = os.path.join(current_app.root_path, 'static', 'galeriaEmprende')
    codadmin = session.get('admin_id')
    
    if request.method == 'GET' and request.args.get('nuevo', '0') == '1':
        # Si se especifica que es un nuevo emprendimiento, resetear la sesión
        session.pop('emprende_id', None)
        session.pop('form_data', None)
        #return redirect(url_for('emprende.publicar_emprendimiento'))
    
    emprende_id = session.get('emprende_id')
    form_data = session.get('form_data', {})
    relativePath = None 
    
    if request.method == 'POST':
        
        galeria  = request.files.getlist('galeria[]')
        logoEmprende = request.files.get("logoEmprende")
        
        if logoEmprende and allowed_file(logoEmprende.filename):
            filename = secure_filename(logoEmprende.filename)
            path = os.path.join(current_app.config['FOLDER_EMPREN'], filename)
            logoEmprende.save(path) 
            relativePath =  os.path.join('galeriaEmprende',filename)
            
        diccionarioEm = {
            "nombreEm": request.form.get("nombreEmprende"),
            "tipoEm": request.form.get("typeEmprende"),
            "descripcionEm": request.form.get("descripcionEmprende"),
            "horarioEm": request.form.get("horarioEmprende"),
            "horarioE": request.form.get("horarioE"),
            "horarioS": request.form.get("horarioS"),
            "paginaEm": request.form.get("paginaEmprende"),
            "productosEm": request.form.get("producempre"),
            "correoEm": request.form.get("correoempre"),
            "contactoEm": request.form.get("telempre"),
            "redInstagram": request.form.get("redInstagram"),
            "redTiktok": request.form.get("redTiktok")
        }
        
        if relativePath:
            diccionarioEm["logo"] = relativePath
        
        form_data.update(diccionarioEm)
        session['form_data'] = form_data
        
        codadmin = session.get('admin_id') 
        cursor = db.cursor()
        
        if not emprende_id:
            fechaPublicacion = datetime.now().date()
            cursor.execute("INSERT INTO emprendimientos (nombreempre,logo,tipoempre,descripempre,horarioempre,horarioApertura,horarioCierre,paginaempre,producempre,correoempre,telempre,fecha_publicacion,codadmin) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(form_data["nombreEm"],form_data['logo'],form_data["tipoEm"],form_data["descripcionEm"],form_data["horarioEm"],form_data["horarioE"],form_data["horarioS"],form_data["paginaEm"],form_data["productosEm"],form_data["correoEm"],form_data["contactoEm"],fechaPublicacion,codadmin))
            
            #recuperar el id del emprendimiento
            emprende_id = cursor.lastrowid
            session['emprende_id'] = emprende_id
            
            #galeria de imagenes
            upload_folder = current_app.config['FOLDER_EMPREN']
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            for imagen in galeria:
                if imagen and allowed_file(imagen.filename):
                    filename = secure_filename(imagen.filename)
                    path = os.path.join(upload_folder, filename)
                    imagen.save(path)
                    relative_path = os.path.join('galeriaEmprende',filename)
                    cursor.execute("INSERT INTO galeriaempre (idempre, imagenempre, descripcion) VALUES (%s, %s, %s)", (emprende_id, relative_path, "Imágen de emprendimiento"))
            
            # Insertar redes sociales
            if form_data["redInstagram"]:
                cursor.execute("INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) VALUES (%s, %s, %s, %s)", 
                   (emprende_id, 'emprendimiento', 'instagram', form_data["redInstagram"]))
                
            if form_data["redTiktok"]:
                cursor.execute("INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) VALUES (%s, %s, %s, %s)", 
                   (emprende_id, 'emprendimiento', 'tiktok', form_data["redTiktok"]))
            
            db.commit()
            cursor.close()
            
        else:
            # Actualiza el evento existente
            cursor = db.cursor()
            cursor.execute("UPDATE emprendimientos SET nombreempre = %s, logo = %s, tipoempre = %s, descripempre = %s, horarioempre = %s, horarioApertura = %s, horarioCierre = %s, paginaempre = %s, producempre = %s, correoempre = %s, telempre = %s WHERE idempre = %s",(form_data["nombreEm"],relativePath,form_data["tipoEm"],form_data["descripcionEm"],form_data["horarioEm"],form_data["horarioE"],form_data["horarioS"],form_data["paginaEm"],form_data["productosEm"],form_data["correoEm"],form_data["contactoEm"],emprende_id))
            
            if form_data["redInstagram"]:
                cursor.execute("UPDATE redes_sociales SET url = %s WHERE entidad_id = %s AND entidad_tipo = %s AND red = %s", 
                   (form_data["redInstagram"], emprende_id, 'emprendimiento', 'instagram'))
            if form_data["redTiktok"]:
                cursor.execute("UPDATE redes_sociales SET url = %s WHERE entidad_id = %s AND entidad_tipo = %s AND red = %s", 
                   (form_data["redTiktok"], emprende_id, 'emprendimiento', 'tiktok'))
            db.commit()
            cursor.close()
        
        flash('Emprendimiento registrado correctamente', 'success')
        return redirect(url_for("emprende.publicar_emprendimientoLocation"))
    
    return render_template('formularioempren.html', datos = form_data, emprende_id = emprende_id, admin_id = codadmin)

#************************************************Registro de publicacion de emprendimiento parte 2***********************************
@emprende.route('/EmprendeLocation',methods=['GET', 'POST'])
def publicar_emprendimientoLocation():
    
    emprende_id = session.get('emprende_id')
    admin_id = session.get('admin_id')
    
    if request.method == 'POST':
        ubicaciones = request.form.getlist('direcciones[]')
        for ubicacion in ubicaciones:
            if ubicacion:  # Comprobar que la ubicación no este vacía
                cursor.execute("INSERT INTO ubicacionempre (idempre, ubicacion) VALUES (%s, %s)", (emprende_id, ubicacion))
        db.commit()
        flash('Ubicaciones guardadas correctamente')
        return redirect(url_for('admin.index_admin'))
    return render_template('formularioEmprende2.html',admin_id = admin_id)


#********************************************************Editar emprendimiento*************************************************************
@emprende.route('/editarEmprendimiento/<int:id>', methods=['GET', 'POST'])
def editarEmprende(id):
    db = get_db()  # Asegúrate de tener la función get_db() adecuada para obtener la conexión a la base de datos
    cursor = db.cursor()
    
    current_app.config['FOLDER_EMPREN'] = os.path.join(current_app.root_path, 'static', 'galeriaEmprende')
    
    codadmin = session.get('admin_id')
    
    if request.method == 'POST':
        emprende_id = cursor.lastrowid
        session['emprende_id'] = emprende_id
        
        logoEmprende = request.files.get("logo_Emprende")
        relativePath = None
        
        if logoEmprende and allowed_file(logoEmprende.filename):
            filename = secure_filename(logoEmprende.filename)
            path = os.path.join(current_app.config['FOLDER_EMPREN'], filename)
            logoEmprende.save(path) 
            relativePath =  os.path.join('galeriaEmprende', filename)
        
        nombre_Emprende = request.form.get('nombre_Emprende')
        type_Emprende = request.form.get('type_Emprende')
        descripcion_Emprende = request.form.get('descripcion_Emprende')
        pagina_Emprende = request.form.get('pagina_Emprende')
        produc_empre = request.form.get('produc_empre')
        horario_Emprende = request.form.get('horario_Emprende')
        horarioEntrada = request.form.get('horarioEntrada')
        horarioSalida = request.form.get('horarioSalida')
        correo_empre = request.form.get('correo_empre')
        tel_empre = request.form.get('tel_empre')
        red_Instagram = request.form.get('red_Instagram')
        red_Tiktok = request.form.get('red_Tiktok')
        fechaPublicacion = datetime.now().date()
        galeria = request.files.getlist('galeria_emprende[]')
        
        # Actualización de la tabla emprendimientos
        sql_emprendimiento = """
            UPDATE emprendimientos SET 
            nombreempre = %s, logo = %s, tipoempre = %s, descripempre = %s, horarioempre = %s, horarioApertura = %s, 
            horarioCierre = %s, paginaempre = %s, producempre = %s, correoempre = %s, telempre = %s, fecha_publicacion = %s
            WHERE idempre = %s
        """
        cursor.execute(sql_emprendimiento, (nombre_Emprende, relativePath, type_Emprende, descripcion_Emprende, horario_Emprende, horarioEntrada, horarioSalida, pagina_Emprende, produc_empre, correo_empre, tel_empre, fechaPublicacion, id))
        db.commit()
        
        # Actualización de la tabla redes_sociales
        sql_redes = """
            UPDATE redes_sociales SET 
            url = %s 
            WHERE entidad_id = %s AND entidad_tipo = %s AND red = %s
        """
        
        # Actualizar Instagram
        entidad_tipo = 'emprendimiento'
        cursor.execute(sql_redes, (red_Instagram, id, entidad_tipo, 'Instagram'))
        db.commit()

        # Actualizar Tiktok
        cursor.execute(sql_redes, (red_Tiktok, id, entidad_tipo, 'Tiktok'))
        db.commit()
        
        # Manejo de galería de imágenes
        cursor.execute("DELETE FROM galeriaempre WHERE idempre = %s", (id,))
        
        upload_folder = current_app.config['FOLDER_EMPREN']
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
            
        for imagen in galeria:
            if imagen and allowed_file(imagen.filename):
                filename = secure_filename(imagen.filename)
                path = os.path.join(upload_folder, filename)
                imagen.save(path)
                relative_path = os.path.join('galeriaEmprende', filename)
                cursor.execute("INSERT INTO galeriaempre (idempre, imagenempre, descripcion) VALUES (%s, %s, %s)", (id, relative_path, "Imagen de emprendimiento"))
        
        db.commit()
        
        return redirect(url_for('emprende.editarEmprendeUbicacion', id=id))  # Redirige a la siguiente parte del formulario o a donde sea necesario
    
    else:
        # Obtener datos existentes del emprendimiento y redes sociales para mostrar en el formulario
        sql_select_emprende = "SELECT * FROM emprendimientos WHERE idempre = %s"
        cursor.execute(sql_select_emprende, (id,))
        emprendimiento = cursor.fetchone()
 
        sql_select_redes = "SELECT red, url FROM redes_sociales WHERE entidad_id = %s AND entidad_tipo = 'emprendimiento'"  
        cursor.execute(sql_select_redes, (id,))
        redes = cursor.fetchall()
        redes_sociales = {red: url for red, url in redes}
        
        cursor.close()
        
        # Preparar datos para enviar al template
        datos_emprende = {
            'nombre_emprende': emprendimiento[1],
            'tipo_emprende': emprendimiento[3],
            'contacto_emprende': emprendimiento[11],
            'correo_emprende': emprendimiento[10],
            'descripcion_emprende': emprendimiento[4],
            'horario_emprende': emprendimiento[5],
            'horarioEntrada': emprendimiento[6],
            'horarioSalida': emprendimiento[7],
            'pagina_emprende': emprendimiento[8],
            'productos_emprende': emprendimiento[9],
            'red_Instagram': redes_sociales.get('instagram', ''),
            'red_Tiktok': redes_sociales.get('tiktok', ''),
        }

        return render_template('editarEmprende1.html', emprende=datos_emprende, emprende_id=id, admin_id=codadmin)
            
@emprende.route('/editarEmprendeUbicacion/<int:id>/', methods=['GET', 'POST'])
def editarEmprendeUbicacion(id):   
    
    db = get_db()
    cursor = db.cursor()   
    codadmin = session.get('admin_id')
    
    sql_select_emprende = "SELECT * FROM emprendimientos WHERE idempre = %s"
    cursor.execute(sql_select_emprende, (id,))
    emprendimiento = cursor.fetchone()
    
    if not emprendimiento:
        flash('El evento especificado no existe', 'error')
        return redirect(url_for('admin.index_admin'))
    
    if request.method == 'POST':
        ubicaciones = request.form.getlist('direccionesEditar[]')
        
        try:
            # Eliminar las ubicaciones actuales del evento
            cursor.execute("DELETE FROM ubicacionempre WHERE idempre = %s", (id,))
            
            # Insertar las nuevas ubicaciones
            for ubicacion in ubicaciones:
                if ubicacion:  # Comprobar que la ubicación no esté vacía
                    cursor.execute("INSERT INTO ubicacionempre (idempre, ubicacion) VALUES (%s, %s)", (id, ubicacion))
            
            db.commit()
            flash('Ubicaciones actualizadas correctamente', 'success')
            return redirect(url_for('admin.index_admin'))
        
        except Exception as e:
            db.rollback()
            flash(f'Error al actualizar las ubicaciones: {str(e)}', 'error')
            return redirect(url_for('emprende.editarEmprende', id=id))
    
    sql_select_ubicaciones = "SELECT ubicacion FROM ubicacionempre WHERE idempre = %s"
    cursor.execute(sql_select_ubicaciones, (id,))
    ubicaciones = [ubicacion[0] for ubicacion in cursor.fetchall()]
    cursor.close()

    return render_template('editarEmprende2.html', admin_id=codadmin, emprende_id = id)
        
#*****************************************************************************ruta para eliminar un emprendimiento******************
@emprende.route('/eliminarEmprendimiento/<int:id>', methods=['GET', 'POST'])
def eliminarEmprendimiento(id):
    db = get_db()
    cursor = db.cursor()

    try:
        # Eliminar entradas de la tabla galeriaempre
        cursor.execute("DELETE FROM galeriaempre WHERE idempre = %s", (id,))
        
        # Eliminar entradas de la tabla ubicacionempre
        cursor.execute("DELETE FROM ubicacionempre WHERE idempre = %s", (id,))
        
        # Eliminar entradas de la tabla redes_sociales
        cursor.execute("DELETE FROM redes_sociales WHERE entidad_id = %s AND entidad_tipo = 'emprendimiento'", (id,))
        
        # Eliminar el emprendimiento
        cursor.execute("DELETE FROM emprendimientos WHERE idempre = %s", (id,))
        
        db.commit()
        flash('Emprendimiento eliminado con éxito', 'success')
    except Exception as e:
        db.rollback()
        flash(f'Error al eliminar el emprendimiento: {str(e)}', 'error')
    finally:
        cursor.close()

    return redirect(url_for('admin.index_admin'))

#********************************************************Ruta para json de detalles******************************************************************
@emprende.route('/emprendimientoDetalleJson/<int:id>', methods=['GET'])
def detallesEmprendeJson(id):
    
    db = get_db()
    cursor = db.cursor(dictionary=True)
    
    try:
        if request.method == 'GET':
            sql = '''
                SELECT em.idempre,
                    em.nombreempre,
                    em.logo AS logo_filename,
                    em.tipoempre,
                    em.descripempre,
                    em.horarioempre,
                    em.horarioApertura,
                    em.horarioCierre,
                    em.paginaempre,
                    em.producempre,
                    em.correoempre,
                    em.telempre,
                    em.fecha_publicacion,
                    adm.nombreadmin AS administrador,
                    adm.apellidoadmin AS apellidoAdm,
                    GROUP_CONCAT(DISTINCT  ga.imagenempre SEPARATOR '; ') AS imagenes_emprende,
                    GROUP_CONCAT(DISTINCT ga.descripcion SEPARATOR '; ') AS descripcion_imagenes,
                    GROUP_CONCAT(DISTINCT ub.ubicacion SEPARATOR '; ') AS ubicaciones_emprende,
                    GROUP_CONCAT(DISTINCT CONCAT(rs.red, ': ', rs.url) SEPARATOR '; ') AS redes_sociales
                FROM 
                    emprendimientos em
                LEFT JOIN administrador adm ON em.codadmin = adm.codadmin
                LEFT JOIN galeriaempre ga ON em.idempre = ga.idempre
                LEFT JOIN ubicacionempre ub ON em.idempre = ub.idempre
                LEFT JOIN redes_sociales rs ON em.idempre = rs.entidad_id AND rs.entidad_tipo = 'emprendimiento'
                WHERE
                    em.idempre = %s
                GROUP BY
                    em.idempre
                ORDER BY
                    em.fecha_publicacion DESC;
       
            '''
            cursor.execute(sql, (id,))
            emprendimiento = cursor.fetchone()
            if emprendimiento:
                
                if emprendimiento['logo_filename']:
                    normalized_logo_filename = emprendimiento['logo_filename'].replace('\\', '/')
                    logo_url = url_for('static', filename=normalized_logo_filename)
                else:
                    logo_url = url_for('static', filename='img/notFound.png')
                    
                emprendimiento['logo'] = logo_url
                
                # Convertir objetos timedelta a string si es necesario
                for key, value in emprendimiento.items():
                    if isinstance(value, timedelta):  # Revisar si el valor es de tipo timedelta
                        # Convertir timedelta a string en formato HH:MM:SS
                        emprendimiento[key] = str(value)
                    elif isinstance(value, str):  # Revisar si el valor es una cadena
                        # Corregir caracteres de escape en la cadena
                        emprendimiento[key] = value.replace('\\', '/')
                return jsonify(emprendimiento)
            else:
                # No se encontró ningún restaurante con el idresta dado
                return jsonify({'error': 'Restaurante no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': 'Error en el servidor: {}'.format(e)}), 500
    finally:
        cursor.close()
        db.close()

@emprende.route('/EmprendeDetalleServidor')
def EmprendeDetalleServidor():
    user_id = session.get('user_id')
    admin_id = session.get('admin_id')
    return render_template('detalleServidorEmprende.html',user_id = user_id,admin_id = admin_id)

@emprende.route('/EmprendeDetalleServidorAdmin')
def EmprendeDetalleServidorAdmin():
    admin_id = session.get('admin_id')
    return render_template('detalleServidorEmprendeAdmin.html',admin_id = admin_id)
#********************************************Rutas para html estaticos*************************************
@emprende.route('/sectionEmprende')
def sectionEmprende():
    user_id = session.get('user_id')
    admin_id = session.get('admin_id')
    return render_template('seccion_empren.html',user_id = user_id, admin_id = admin_id)

@emprende.route('/sectionEmprendeAdmin')
def sectionEmprendeAdmin():
    admin_id = session.get('admin_id')
    return render_template('seccion_empren_admin.html',admin_id = admin_id)

@emprende.route('/detalleEmprende/administrador')
def detalleEmprendeAdmin():
    admin_id = session.get('admin_id')
    return render_template('detalle_emprende_admin.html',admin_id = admin_id)

@emprende.route('/emprendeDetalle')
def emprendeDetalle():
    user_id = session.get('user_id')
    admin_id = session.get('admin_id')
    return render_template('detalle_empren.html',user_id = user_id,admin_id = admin_id)