import vehiculos, mecanicos
import datetime
import sql

# la función crear() permite registrar una nueva orden de trabajo para un vehículo específico en una base de datos, 
# solicitando la patente del vehículo y el motivo de la avería, y luego almacenando esta información junto con la fecha actual en la tabla ordenes
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
 
#la función consultar(id) busca y muestra todas las órdenes de trabajo que tienen un estado específico (id) en la base de datos, 
# formateando y mostrando los detalles relevantes de cada orden si se encuentran.    
def consultar(id):
    query = "SELECT * FROM ordenes WHERE estado = %s"
    values = (id,)
    sql.cursor.execute(query,values)
    ordenes = sql.cursor.fetchall()
    if ordenes:
        print("Ordenes de trabajo")
        print("------------------")
        for orden in ordenes:
            print(orden[0], orden[1], orden[2].strftime("%Y-%m-%d"), orden[3], orden[4], orden[5], orden[6])
    else:
        print("No hay ordenes con ese estado en la base de datos.")

#la función asignar() facilita la asignación de una orden de trabajo a un mecánico específico en la base de datos, 
# verificando la existencia de la orden y del mecánico antes de realizar la asignación.
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

# la función mostrar_ordenes() realiza una consulta a la base de datos para recuperar todas las órdenes almacenadas
# y las muestra en la consola. Si no hay órdenes disponibles, informa al usuario de esta situación.
def mostrar_ordenes():
    query = "SELECT * FROM ordenes"
    sql.cursor.execute(query)
    ordenes = sql.cursor.fetchall()
    if ordenes:
        for orden in ordenes:
            print(orden[0], orden[1], orden[2].strftime("%Y-%m-%d"), orden[3], orden[4], orden[5], orden[6])
    else:
        print("No hay ordenes en la base de datos.")
    

#la función buscar(id) permite verificar la existencia de una orden específica en la base de datos a través de su idOrden, 
# devolviendo True si la orden existe y False si no existe.
def buscar(id):
    query = "SELECT * FROM ordenes WHERE idOrden = %s"
    values = (id,)
    sql.cursor.execute(query, values)
    sql.cursor.fetchone()
    if(sql.cursor.rowcount == 1):
        return True
    else:
        return False

#la función update(id, status) permite modificar el estado de una orden específica en la base de datos    
def update(id, status):
    query = "UPDATE ordenes SET estado = %s WHERE idOrden = %s"
    values = (status, id)
    sql.cursor.execute(query, values)
    sql.conexion.commit()
    