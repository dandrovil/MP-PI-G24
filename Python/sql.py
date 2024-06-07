import mysql.connector

def conectar_bd(anf, usuario, contra, bd):
    try:
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
            host=anf,
            user=usuario,
            password=contra,
            database=bd,
        )
        print("Conexión exitosa")
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectarse a MySQL: {err}")
        return None

def consulta_bd(conexion, consulta):
    try:
        # Consultar la base de datos
        cursor = conexion.cursor()
        cursor.execute(consulta)
        resultados = cursor.fetchall()  
        cursor.close()  
        return resultados
    except mysql.connector.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        return None

def cerrar_bd(conexion):
    try:
        # Cerrar la base de datos
        if conexion.is_connected():
            conexion.close()
            print("Conexión cerrada")
    except mysql.connector.Error as err:
        print(f"Error al cerrar la conexión: {err}")

