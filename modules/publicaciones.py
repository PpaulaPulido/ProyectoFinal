from flask import Blueprint, request, render_template, redirect, url_for, flash,current_app,send_from_directory,abort,session,jsonify
from werkzeug.utils import secure_filename
from datetime import datetime
from db import get_db, get_cursor
import os

publicacionDash = Blueprint('publicacionDash', __name__)
db = get_db()
cursor = get_cursor(db)

#******************************************Index del admin dashboard*****************************************************************
def dashboardPublicacion(entidad):
    
    db = get_db()
    cursor = db.cursor()
    codadmin = session.get('admin_id')

    # Seleccionamos los campos comunes y específicos según el tipo de entidad
    if entidad == 'restaurante':
        table_name = 'restaurantes'
        entity_fields = 'idresta as id, nombreresta as nombre, logo, tiporesta as tipo, fecha_publicacion'
        
    elif entidad == 'emprendimiento':
        table_name = 'emprendimientos'
        entity_fields = 'idempre as id, nombreempre as nombre, logo, tipoempre as tipo, fecha_publicacion'
    
    elif entidad == 'evento':
        table_name = 'eventos'
        entity_fields = 'ideven as id, nombreeven as nombre, logo, tipoevento as tipo, fecha_publicacion'
    
    else:
        return jsonify({'error': 'Tipo de entidad no soportado'}), 400

    querySelect = f"SELECT {entity_fields} FROM {table_name} WHERE codadmin = %s ORDER BY fecha_publicacion DESC"
    cursor.execute(querySelect, (codadmin,))
    publicaciones = cursor.fetchall()

    publicaciones_list = []

    for publicacion in publicaciones:
        id, nombre, logo_filename, tipo, fecha_publicacion = publicacion

        # Normalizamos la URL del logo
        if logo_filename:
            normalized_logo_filename = logo_filename.replace('\\', '/')
            logo_url = url_for('static', filename=normalized_logo_filename)
        else:
            logo_url = url_for('static', filename='img/notFound.png')

        # Agregamos la publicación formateada a la lista
        publicaciones_list.append({
            'id': id,
            'nombre': nombre,
            'logo': logo_url,
            'tipo': tipo,
            'fecha_publicacion': fecha_publicacion
        })

    return jsonify(publicaciones_list)


@publicacionDash.route('/dashboard/restaurante')
def dashRes():
    return dashboardPublicacion("restaurante")

@publicacionDash.route('/dashboard/emprendimiento')
def dashEmmprendimiento():
    return dashboardPublicacion("emprendimiento")

@publicacionDash.route('/dashboard/evento')
def dashEventos():
    return dashboardPublicacion("evento")

#****************************************funcion para traer datos de los formularios************************************************************

def publicacionesPublica(entidad, tipo):
    db = get_db()
    cursor = db.cursor()

    if entidad == 'restaurante':
        tabla = 'restaurantes'
        campos = 'idresta as id, nombreresta as nombre, logo, tiporesta as tipo, fecha_publicacion'
        tipo_columna = 'tiporesta'
        
    elif entidad == 'emprendimiento':
        tabla = 'emprendimientos'
        campos = 'idempre as id, nombreempre as nombre, logo, tipoempre as tipo, fecha_publicacion'
        tipo_columna = 'tipoempre'
        
    elif entidad == 'evento':
        tabla = 'eventos'
        campos = 'ideven as id, nombreeven as nombre, logo, tipoevento as tipo, fecha_publicacion'
        tipo_columna = 'tipoevento'
    else:
        return jsonify({'error': 'Tipo de entidad no soportado'}), 400

    querySelect = f"SELECT {campos} FROM {tabla} WHERE LOWER({tipo_columna}) = LOWER(%s) ORDER BY fecha_publicacion DESC"

    
    cursor.execute(querySelect, (tipo,))
    publicaciones = cursor.fetchall()
    
    publicaciones_list = []

    for publicacion in publicaciones:
        id, nombre, logo_filename, tipo, fecha_publicacion = publicacion

        if logo_filename:
            normalized_logo_filename = logo_filename.replace('\\', '/')
            logo_url = url_for('static', filename=normalized_logo_filename)
        else:
            logo_url = url_for('static', filename='img/notFound.png')

        publicaciones_list.append({
            'id': id,
            'nombre': nombre,
            'logo': logo_url,
            'tipo': tipo,
            'fecha_publicacion': fecha_publicacion
        })

    return jsonify(publicaciones_list)

#************************Tipos de restaurantes************************************
@publicacionDash.route('/tipoRestaurante')
def restaurantesList():
    tipo = request.args.get('tipo')  # parámetro 'tipo' de la URL
    if tipo is None:
        return jsonify({'error': 'Falta el parámetro tipo en la URL'}), 400
    
    return publicacionesPublica('restaurante', tipo)

@publicacionDash.route('/restauranteTipo')
def resTipo():
    user_id = session.get('user_id')
    admin_id = session.get('admin_id')
    return render_template('tipo_restaurante.html',user_id=user_id,admin_id = admin_id)

@publicacionDash.route('/restauranteTipoAdmin')
def resTipoAdmin():
    admin_id = session.get('admin_id')
    return render_template('tipo_restaurante_admin.html',admin_id = admin_id)


#****************************tipos de eventos **************************
@publicacionDash.route('/tipoEvento')
def eventoList():
    tipo = request.args.get('tipo')  # parámetro 'tipo' de la URL
    if tipo is None:
        return jsonify({'error': 'Falta el parámetro tipo en la URL'}), 400
    
    return publicacionesPublica('evento', tipo)

@publicacionDash.route('/eventoTipo')
def eventoTipo():
    user_id = session.get('user_id')
    admin_id = session.get('admin_id')
    return render_template('tipo_evento.html',user_id = user_id,admin_id = admin_id)

@publicacionDash.route('/eventoTipoAdmin')
def eventoTipoAdmin():
    admin_id = session.get('admin_id')
    return render_template('tipo_evento_admin.html',admin_id = admin_id)

#****************************tipos de emprendimientos **************************
@publicacionDash.route('/tipoEmprendimiento')
def emprendimientoList():
    tipo = request.args.get('tipo')  # parámetro 'tipo' de la URL
    if tipo is None:
        return jsonify({'error': 'Falta el parámetro tipo en la URL'}), 400
    
    return publicacionesPublica('emprendimiento', tipo)

@publicacionDash.route('/emprendimientoTipo')
def emprendeTipo():
    user_id = session.get('user_id')
    admin_id = session.get('admin_id')
    return render_template('tipo_emprendimiento.html',user_id = user_id,admin_id = admin_id)

@publicacionDash.route('/emprendimientoTipoAdmin')
def emprendeTipoAdmin():
    admin_id = session.get('admin_id')
    return render_template('tipo_emprendimiento_admin.html',admin_id = admin_id)
#***************************Galeria de imagenes funcion******************************
def galeriaImagenesPublicacion(id,entidad):
    
    db = get_db()
    cursor = get_cursor(db)
    
    if entidad == 'restaurante':
        table_name = 'galeriaresta'
        fields = 'imagenresta as imagenGaleria'
        id_table = 'idresta'
        folder = 'galeriaRes'
    
    elif entidad == 'evento':
        table_name = 'galeriaeven'
        fields = ' urlImagen as imagenGaleria'
        id_table = 'ideven'
        folder = 'galeriaEventos'
    
    elif entidad == 'emprendimiento':
        table_name = 'galeriaempre'
        fields = 'imagenempre as imagenGaleria'
        id_table = 'idempre'
        folder = 'galeriaEmprende'
    
    else:
        return jsonify({'error': 'Tipo de entidad no soportado'}), 400
    
    query = f"SELECT {fields} FROM {table_name} WHERE {id_table} = %s"
    cursor.execute(query, (id,))
    imagenes = cursor.fetchall()
    
    cursor.close()
    db.close()
    
    directory_path = os.path.join(current_app.root_path, 'static', folder)
    
    imagenes_encontradas = []
    for imagen in imagenes:
        file_name = imagen[0] 
        file_name = file_name.split(f"{folder}\\")[-1]
        full_file_path = os.path.join(directory_path, file_name)
        
        if os.path.isfile(full_file_path):
            imagenes_encontradas.append(url_for('static', filename=f'{folder}/{file_name}'))
        else:
            print(f"Archivo no encontrado: {full_file_path}")  # Log para depuración

    # Si no se encontraron imágenes válidas, se añade una imagen por defecto
    if not imagenes_encontradas:
        default_file_name = 'bogota.jpg'  # Nombre de la imagen por defecto
        default_directory_path = os.path.join(current_app.root_path, 'static', 'img')
        default_full_file_path = os.path.join(default_directory_path, default_file_name)
        
        if os.path.isfile(default_full_file_path):
            imagenes_encontradas.append(url_for('static', filename=f'img/{default_file_name}'))  # Ajustar la ruta para devolver la imagen por defecto
        else:
            print(f"Imagen por defecto no encontrada: {default_full_file_path}")  # Log para depuración
            # Manejar el caso en que ni siquiera la imagen por defecto existe
            flash('No se encontraron imágenes para esta galería y la imagen por defecto no está disponible.', 'error')
            return redirect(url_for('some_default_route'))  # Redirige a una ruta por defecto si no hay imágenes

    return jsonify(imagenes=imagenes_encontradas)

@publicacionDash.route('/galeriaImagenes/restaurante/<int:id>')
def galeriaImagenesRes(id):
    return galeriaImagenesPublicacion(id,'restaurante')

@publicacionDash.route('/galeriaImagenes/evento/<int:id>')
def galeriaImagenesEventos(id):
    return galeriaImagenesPublicacion(id,'evento')


@publicacionDash.route('/galeriaImagenes/Emprendimiento/<int:id>')
def galeriaImagenesEmprende(id):
    return galeriaImagenesPublicacion(id,'emprendimiento')
#**********************************************funcion para traer ubicaciones de la base de datos*****************************************************************
    
def ubicacionesPublicacion(entidad, id):
    db = get_db()
    cursor = db.cursor()
   
    # Seleccionamos los campos comunes y específicos según el tipo de entidad
    if entidad == 'restaurante':
        table_name = 'ubicacionresta'
        entity_fields = 'idresta as id, ubicacion'
        columna_id = 'idresta'
        
    elif entidad == 'emprendimiento':
        table_name = 'ubicacionempre'
        entity_fields = 'idempre as id, ubicacion'
        columna_id = 'idempre'
    
    elif entidad == 'evento':
        table_name = 'ubicacioneven'
        entity_fields = 'ideven as id, ubicacion'
        columna_id = 'ideven'
    
    else:
        return jsonify({'error': 'Tipo de entidad no soportado'}), 400

    querySelect = f"SELECT {entity_fields} FROM {table_name} WHERE {columna_id} = %s"
    cursor.execute(querySelect, (id,))
    publicaciones = cursor.fetchall()

    cursor.close()  # Cerrar el cursor

    publicaciones_list = [
        {'id': id, 'ubicacion': ubicacion} for (id, ubicacion) in publicaciones
    ]

    return jsonify(publicaciones_list)

@publicacionDash.route('/restaurante/ubicacion/<int:id>')
def resUbicacion(id):
    return ubicacionesPublicacion('restaurante', id)

@publicacionDash.route('/emprendimiento/ubicacion/<int:id>')
def empUbicacion(id):
    return ubicacionesPublicacion('emprendimiento', id)

@publicacionDash.route('/evento/ubicacion/<int:id>')
def evenUbicacion(id):
    return ubicacionesPublicacion('evento', id)

#***********************Ruta del buscador****************************
def buscador(entidad):
    tipo = request.args.get('tipo')
    db = get_db()
    cursor = db.cursor(dictionary=True)
    
    if entidad == 'restaurante':
        table_name = 'restaurantes'
        entity_fields = 'idresta, nombreresta,tiporesta'
        tipo_field = 'tiporesta'
    
    elif entidad == 'evento':
        table_name = 'eventos'
        entity_fields = 'ideven , nombreeven ,tipoevento'
        tipo_field = 'tipoevento'
        
    elif entidad == 'emprendimiento':
        table_name = 'emprendimientos'
        entity_fields = 'idempre, nombreempre,tipoempre'
        tipo_field = 'tipoempre'
        
    else:
        return jsonify({'error': 'Tipo de entidad no soportado'}), 400
    
    
    try:
        if tipo:
            sql = f"SELECT {entity_fields} FROM {table_name} WHERE {tipo_field}=%s"
            
            cursor.execute(sql,(tipo,))
        else:
            sql = f"SELECT {entity_fields} FROM {table_name}"
            cursor.execute(sql)
        
        busqueda = cursor.fetchall()
        cursor.close()
        
        return jsonify(busqueda)
    except Exception as e:
        # En caso de error, devolver un mensaje de error y el código de estado HTTP 500 
        return jsonify({'error': 'Error en el servidor: {}'.format(e)}), 500

@publicacionDash.route('/buscar_restaurante')
def buscarRes():
    return buscador('restaurante')

@publicacionDash.route('/buscar_evento')
def buscarEven():
    return buscador('evento')

@publicacionDash.route('/buscar_emprendimiento')
def buscarEmprende():
    return buscador('emprendimiento')

