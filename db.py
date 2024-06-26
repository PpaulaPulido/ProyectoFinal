import mysql.connector

def get_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='emprenesy'
    )
   

def get_cursor(db):
    return db.cursor()
