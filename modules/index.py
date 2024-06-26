from flask import Blueprint, request, render_template, redirect, url_for, flash,current_app,send_from_directory,abort,session
from db import get_db, get_cursor
from flask_mail import Mail, Message
import os



inicio = Blueprint('inicio', __name__)
db = get_db()
cursor = get_cursor(db)

@inicio.route('/index_user')
def index():
    return render_template('index.html')

@inicio.route('/nosotros')
def nosotros():
    return render_template('MVQ.html')

    
@inicio.route('/enviar', methods=['POST'])
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
    return redirect(url_for('index'))