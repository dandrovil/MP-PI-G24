import vehiculos, mecanicos
import datetime
import sql

def crear():
    
    x=datetime.datetime.now()
    patente = input("Ingrese Patente: ")
    if (not vehiculos.consultar(patente)): 
        print(f"No se encontró ningún vehículo con la patente {patente}")
        return
    fecha = x.strftime("%Y-%m-%d")
    averia = input("Motivo: ")
    query = "INSERT INTO ordenes (patente, fecha_ingreso, averia) VALUES (%s, %s, %s)"
    values = (patente, fecha, averia)
    sql.cursor.execute(query, values)
    sql.conexion.commit() 
    print("Orden creada con exito.")
    
def consultar(id):
    query = "SELECT * FROM ordenes WHERE estado = %s"
    values = (id,)
    sql.cursor.execute(query,values)
    ordenes = sql.cursor.fetchall()
    if ordenes:
        for orden in ordenes:
            print(orden[0], orden[1], orden[2].strftime("%Y-%m-%d"), orden[3], orden[4], orden[5], orden[6])
    else:
        print("No hay ordenes con ese estado en la base de datos.")

def asignar():
    consultar("ingresado")
    nroorden = input("Ingrese N° de orden a asignar: ")
    if(buscar(nroorden)):
        mecanicos.mostrar()
        idmeca = input("Ingrese Codigo de Mecanico: ")
        if(mecanicos.consultar(idmeca)):
            query = "UPDATE ordenes SET mecanico = %s, estado = %s WHERE idOrden = %s"
            values = (idmeca, "ASIGNADO", nroorden)
            sql.cursor.execute(query, values)
            sql.conexion.commit()
            print(f"La orden N° {nroorden} fue asiganada al Mecanico Cod: {idmeca}")
        else:
            print(f'El mecanico con codigo {idmeca} NO existe.')
    else:
        print(f"El N° de Orden {nroorden} NO existe.")

def mostrar_ordenes():
    query = "SELECT * FROM ordenes"
    sql.cursor.execute(query)
    ordenes = sql.cursor.fetchall()
    if ordenes:
        for orden in ordenes:
            print(orden[0], orden[1], orden[2].strftime("%Y-%m-%d"), orden[3], orden[4], orden[5], orden[6])
    else:
        print("No hay ordenes en la base de datos.")
    
def buscar(id):
    query = "SELECT * FROM ordenes WHERE idOrden = %s"
    values = (id,)
    sql.cursor.execute(query, values)
    orden = sql.cursor.fetchone()
    if(sql.cursor.rowcount == 1):
        return True
    else:
        return False