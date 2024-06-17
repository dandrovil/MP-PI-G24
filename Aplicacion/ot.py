import vehiculos, clientes
import datetime
import sql
import pandas as pd
from tabulate import tabulate


#La función agregar() permite agregar una nueva orden de trabajo al sistema.
#Primero, se verifica si el vehículo con la patente ingresada existe en la base de datos.
#Si el vehículo existe, se crea una nueva orden de trabajo con la fecha de ingreso actual,
#el motivo de ingreso y el estado inicial.
def agregar():
    x=datetime.datetime.now()
    patente = input("Ingrese Patente: ")
    if (not vehiculos.consultar(patente)): 
        print(f"\nNo se encontró ningún vehículo con la patente {patente}")
        print(f'\nOperación cancelada.')
        return
    fecha = x.strftime("%Y-%m-%d")
    averia = input("Motivo de ingreso a taller: ")
    query = "INSERT INTO ordenes (patente, fecha_ingreso, averia) VALUES (%s, %s, %s)"
    values = (patente, fecha, averia)
    sql.cursor.execute(query, values)
    sql.conexion.commit() 
    print("\nOrden creada con exito.")

#La función buscar(op) permite buscar ordenes de trabajo en el sistema utilizando diferentes criterios.
#la opción de búsqueda se selecciona mediante el parámetro `o`.
#Si se encuentra una orden de trabajo que coincide con la búsqueda, se muestra la información de la orden.
# #Si no se encuentra ninguna orden de trabajo, se muestra un mensaje de error. 
def buscar(op):
    if op == 1:
        id = input("Ingrese Nro. de orden a buscar: ")
        if consultar(id):
            query = """
            SELECT ordenes.idOrden, ordenes.patente, ordenes.fecha_ingreso, ordenes.averia,
            ordenes.fecha_egreso, ordenes.estado, mecanicos.apeynom
            FROM ordenes
            INNER JOIN mecanicos ON ordenes.mecanico = mecanicos.idmeca
            WHERE idOrden = %s;
            """
            values = (id,)
            sql.cursor.execute(query, values)
            nombres_de_columnas = ['NRO. ORDEN', 'DOMINIO', 'FECHA INGRESO', 'MOTIVO', 'FECHA EGRESO', 'ESTADO', 'MECANICO']
            ordenes = sql.cursor.fetchall()
            df = pd.DataFrame(ordenes, columns=nombres_de_columnas)
            if ordenes:
                print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False, colalign=("center",)*len(nombres_de_columnas)))
            else:
                print(f'\nLa orden Nº {id} aun no tiene un mecanico asignado.')
        else:
            print(f"\nNo existe ordenes de trabajo con el numero {id}.")
    elif op == 2:
        id = input("Ingrese CUIT/DNI del cliente a buscar: ")
        if clientes.consultar(id):
            query = """
            SELECT ordenes.idOrden, ordenes.patente, ordenes.fecha_ingreso, ordenes.averia, ordenes.fecha_egreso, ordenes.estado, mecanicos.apeynom
            FROM ordenes
            INNER JOIN autos ON ordenes.patente = autos.patente
            INNER JOIN clientes ON autos.id_Cliente = clientes.dni_cuit
            INNER JOIN mecanicos ON ordenes.mecanico = mecanicos.idmeca
            WHERE clientes.dni_cuit = %s;
            """
            values = (id,)
            sql.cursor.execute(query, values)
            nombres_de_columnas = ['NRO. ORDEN', 'DOMINIO', 'FECHA INGRESO', 'MOTIVO', 'FECHA EGRESO', 'ESTADO', 'MECANICO']
            ordenes = sql.cursor.fetchall()
            df = pd.DataFrame(ordenes, columns=nombres_de_columnas)
            if ordenes:
                print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False, colalign=("center",)*len(nombres_de_columnas)))
            else:
                print(f'\nLa orden del DNI/CUIT {id} aun no tiene un mecanico asignado.')
        else:
            print(f"\nNo existe clientes con el DNI/CUIT {id}.")
    elif op == 3:
            id = input("Ingrese la patente del vehiculo a buscar: ")
            if vehiculos.consultar(id):
                query = """
                SELECT ordenes.idOrden, ordenes.patente, ordenes.fecha_ingreso, ordenes.averia,
                ordenes.fecha_egreso, ordenes.estado, mecanicos.apeynom
                FROM ordenes
                INNER JOIN mecanicos ON ordenes.mecanico = mecanicos.idmeca
                WHERE patente = %s;
                """
                values = (id,)
                sql.cursor.execute(query, values)
                nombres_de_columnas = ['NRO. ORDEN', 'DOMINIO', 'FECHA INGRESO', 'MOTIVO', 'FECHA EGRESO', 'ESTADO', 'MECANICO']
                ordenes = sql.cursor.fetchall()
                df = pd.DataFrame(ordenes, columns=nombres_de_columnas)
                if ordenes:
                    print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False, colalign=("center",)*len(nombres_de_columnas)))
                else:
                    print(f'\nLa orden de patente {id} aun no tiene un mecanico asignado.')
            else:
                print(f"\nNo existe vehiculos con la patente {id} en la base de datos.")
    else:
        id = input("Ingrese la fecha de ingreso a buscar: (AAAA-MM-DD) ")
        query = """
        SELECT ordenes.idOrden, ordenes.patente, ordenes.fecha_ingreso, ordenes.averia,
        ordenes.fecha_egreso, ordenes.estado, mecanicos.apeynom
        FROM ordenes
        INNER JOIN mecanicos ON ordenes.mecanico = mecanicos.idmeca
        WHERE fecha_ingreso = %s;
        """
        values = (id,)
        sql.cursor.execute(query, values)
        nombres_de_columnas = ['NRO. ORDEN', 'DOMINIO', 'FECHA INGRESO', 'MOTIVO', 'FECHA EGRESO', 'ESTADO', 'MECANICO']
        ordenes = sql.cursor.fetchall()
        df = pd.DataFrame(ordenes, columns=nombres_de_columnas)
        if ordenes:
            print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False, colalign=("center",)*len(nombres_de_columnas)))
        else:
            print(f'\nLa orden de patente {id} aun no tiene un mecanico asignado.')
            
#La funcion asignar(opc) permite asignar o actualizar la información de una orden de trabajo existente.
#Primero, se verifica si la orden de trabajo existe en la base de datos.
#Luego, se aplica la opción de asignación seleccionada:
#    - Asignar un nuevo mecanico a la orden de trabajo
#    - Actualizar el motivo de la orden de trabajo
#    - Cerrar la orden de trabajo (marcar como finalizado)   
#    - Actualizar la fecha de ingreso de la orden de trabajo.     

def asignar(opc):
    norden = int(input("Ingrese N° de orden de trabajo a actualizar: "))
    if(consultar(norden)):
        query = """
        SELECT ordenes.idOrden, ordenes.fecha_ingreso, autos.marca, autos.modelo,
               ordenes.patente, ordenes.averia, ordenes.estado, mecanicos.apeynom
        FROM ordenes
        INNER JOIN autos ON ordenes.patente = autos.patente
        INNER JOIN mecanicos ON ordenes.mecanico = mecanicos.idmeca;
        """
        sql.cursor.execute(query)
        ordenes = sql.cursor.fetchall()
        for orden in ordenes:
            if orden[0] == norden:
                print("\n------------------------------------------")
                print(f"Nro. de Orden: {orden[0]}")
                print(f"Fecha de Ingreso: {orden[1]}")
                print(f"Marca: {orden[2]}")
                print(f"Modelo: {orden[3]}")
                print(f"Dominio: {orden[4]}")
                print(f"Motivo: {orden[5]}")
                print(f"Estado: {orden[6]}")
                print(f"Mecanico: {orden[7]}")
                print("------------------------------------------\n")
        if opc == 1:
            motivo = input("Ingrese nuevo motivo: ")
            query = "UPDATE ordenes SET averia = %s WHERE idOrden = %s"
            values = (motivo, norden)
        elif opc == 2:
            id = input("Ingrese nuevo codigo de mecanico: ")
            query = 'SELECT * FROM mecanicos WHERE idmeca = %s'
            values = (id,)
            sql.cursor.execute(query,values)
            meca = sql.cursor.fetchone()   
            if(sql.cursor.rowcount == 1):
                resp = input(f"\nDesea vincular a {meca[1]} a la orden de trabajo {norden} (S/N)")
                if resp.lower() == 's':
                    query = "UPDATE ordenes SET mecanico = %s, estado = %s WHERE idOrden = %s"
                    values = (id, 'Asignado', norden)
                else:
                    print("\nNo se realizó la asignación.")
                    return
            else:
                print(f'\nEl mecanico con codigo {id} NO existe.')
        elif opc == 3:
            resp = input(f"\nEsta seguro que desea cerrar la orden de trabajo {norden} (S/N)")
            if resp.lower() == 's':
                query = "UPDATE ordenes SET estado = 'Finalizado' WHERE idOrden = %s"
                values = (norden)
            else:
                print("\nNo se modifico la orden de trabajo.")
                return
        else:
             resp = input(f"\nIngrese nueva fecha de ingreso: (AAAA-MM-DD) ")
             query = "UPDATE ordenes SET fecha_ingreso = %s WHERE idOrden = %s"
             values = (resp, norden)
        sql.cursor.execute(query, values)
        sql.conexion.commit()
        print("\nLa acutalizacion se realizo correctamente.")
    else:
        print(f"El N° de Orden {norden} no existe.")
            
# la función mostrar() realiza una consulta a la base de datos para recuperar todas las órdenes almacenadas
# y las muestra en la consola. Si no hay órdenes disponibles, informa al usuario de esta situación.
def mostrar():
    query = 'SELECT * FROM ordenes'
    sql.cursor.execute(query)
    nombres_de_columnas = ['NRO. ORDEN', 'FECHA INGRESO', 'DOMINIO', 'MOTIVO', 'FECHA EGRESO', 'ESTADO', 'MECANICO']
    ordenes = sql.cursor.fetchall()
    df = pd.DataFrame(ordenes, columns=nombres_de_columnas)
    if ordenes:
        print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False, colalign=("center",)*len(nombres_de_columnas)))
    else:
        print("No hay ordenes en la base de datos.")
    

#la función consultar(id) permite verificar la existencia de una orden específica en la base de datos a través de su idOrden, 
# devolviendo True si la orden existe y False si no existe.
def consultar(id):
    query = "SELECT * FROM ordenes WHERE idOrden = %s"
    values = (id,)
    sql.cursor.execute(query, values)
    sql.cursor.fetchone()
    if(sql.cursor.rowcount == 1):
        return True
    else:
        return False

#La función update() actualiza una orden de trabajo existente
def update(id,status):
    query = "UPDATE ordenes SET estado = %s WHERE idOrden = %s"
    values = (status, id)
    sql.cursor.execute(query, values)
    sql.conexion.commit()
    
