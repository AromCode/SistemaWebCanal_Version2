import mysql.connector

def Obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="usuarios_bd"
        )
        return conexion
    except mysql.connector.Error as err:
        return None