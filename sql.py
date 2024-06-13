import mysql.connector

HOST = "localhost"
USER = "root"
PASS = "root"
BD = "taller"

        # Conexión a la base de datos
conexion = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASS,
    database=BD,
    )
    
# Crear un cursor
cursor = conexion.cursor()

def cerrar_bd():
    cursor.close()
    conexion.close()

    
            