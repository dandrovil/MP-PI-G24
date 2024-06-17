import sql, os, msvcrt
import mecanicos,stock, ot
import datetime
import pandas as pd
from tabulate import tabulate
from decimal import Decimal, getcontext

if os.name == 'nt':
    screen = 'cls'
else:
    screen = 'clear'

#Funcion para crear un nuevo presupuesto en la base  de datos. 
def agregar():
    idmeca = input('Ingrese su codigo del mecanico: ')
    if(mecanicos.consultar(idmeca)):
        query = """
        SELECT ordenes.idOrden, ordenes.fecha_ingreso, autos.marca, autos.modelo, ordenes.patente, ordenes.averia
        FROM ordenes
        INNER JOIN autos ON ordenes.patente = autos.patente
        WHERE mecanico = %s AND estado = %s
        """
        values = (idmeca, "Asignado")
        sql.cursor.execute(query,values)
        nombres_de_columnas = ['NRO. ORDEN', 'FECHA INGRESO', 'MARCA', 'MODELO', 'DOMINIO', 'MOTIVO']
        ordenes = sql.cursor.fetchall()
        df = pd.DataFrame(ordenes, columns=nombres_de_columnas)
        if ordenes:
            print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False, colalign=("center",)*len(nombres_de_columnas)))
            nroorden = input("\nIngrese numero de orden a presupuestar: ")
            tot = 0
            nrorep = 1
            while nrorep != 0:
                os.system(screen)
                nrorep = int(input("\nIngrese Codigo de repuesto: (0 para salir) "))
                if nrorep != 0:
                    if (stock.consultar(nrorep)):
                        query = "SELECT * FROM stock WHERE idstock = %s"
                        values = (nrorep,)
                        sql.cursor.execute(query,values)
                        nombre = sql.cursor.fetchone()
                        print(nombre[2])
                        cant = int(input("Cantidad: "))
                        precio = float(input("Precio: "))
                        sub = cant * precio
                        tot = tot + sub
                        query = 'INSERT INTO pedidos (idorden, idstock, cantidad, preciou, subtotal) VALUES (%s, %s, %s, %s, %s)'
                        values = (nroorden, nrorep, cant, precio, sub)
                        sql.cursor.execute(query, values)
                        sql.conexion.commit()
                    else:
                        print(f"\nEl codigo {nrorep} es inexistente")
                        msvcrt.getch()
        else:
             print("No tiene ordenes para presupuestar.")
             return
    else:
        print(f'El codigo de mecanico {idmeca} no existe.')
        return
   
    trabajo = input("\nDescriba trabajo realizado: ")
    costo = float(input("\nIngrese costo de mano de obra: $ "))
    total = tot + costo
    query = 'INSERT INTO presupuesto (idorden, desc_trabajo, p_repuestos, p_manodeobra, total) VALUES (%s, %s, %s, %s, %s)'
    values = (nroorden, trabajo, tot, costo, total)
    sql.cursor.execute(query, values)
    sql.conexion.commit()
    ot.update(nroorden, "Presupuestado")
    print(f"\nPresupuesto para la orden de trabajo N° {nroorden} ha sido confeccionado")
    
# La funcion generar() sirve para generar la factura carga los datos en la tabla facturacion.
def generar():
    query = """
    SELECT presupuesto.idpresupuesto, presupuesto.idorden, presupuesto.desc_trabajo, presupuesto.p_repuestos, presupuesto.p_manodeobra, presupuesto.total
    FROM presupuesto
    WHERE estado = %s
    """
    values = ('Aprobado',)
    sql.cursor.execute(query, values)
    nombres_de_columnas = ['NRO. PRESUPUESTO', 'NRO. ORDEN', 'DESCRIPCION', 'REPUESTOS', 'MANO DE OBRA', 'TOTAL']
    presupuestos = sql.cursor.fetchall()
    df = pd.DataFrame(presupuestos, columns=nombres_de_columnas)
    if presupuestos:
        print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False, colalign=("center",)*len(nombres_de_columnas)))
        npre = int(input('\nIngrese el numero de presupuesto a facturar: '))
        ans = ""
        while ans != 's' and ans != 'n':
            ans = input("\nEs consumidor final? (s/n): ")
            if ans.lower() == 's':
                cf = 1
            elif ans.lower() == 'n':
                cf = 0
            else:
                print("Opcion invalida.")
        nor = 0
        tot = Decimal(0)
        for presupuesto in presupuestos:
            if npre == presupuesto[0]:
                nor = presupuesto[1]
                tot = Decimal(presupuesto[5])
                break
        query = """
        select autos.id_Cliente
        from autos
        inner join ordenes on autos.patente = ordenes.patente
        where idOrden = %s
        """
        values = (nor,)
        sql.cursor.execute(query, values)
        idcliente = sql.cursor.fetchone()
        dni_cuit = idcliente[0]
        x=datetime.datetime.now()
        fecha = x.strftime("%Y-%m-%d")
        iva =  0.0
        if cf == 0:
             iva = tot * Decimal('0.21')
             tot = tot + iva
        query = 'INSERT INTO facturas (idpresupuesto, dni_cuit, fechaemision, consumidorfinal, iva, total) VALUES (%s, %s, %s, %s, %s, %s)'
        values = (npre, dni_cuit, fecha, cf, iva, tot)
        sql.cursor.execute(query, values)
        sql.conexion.commit()
        update(nor, "Facturado")
        ot.update(nor, "Finalizado")
        print("\nLa factura ha sido generada")

#La funcion oknok() sirve para aceptar o rechazar un presupuesto modificando la tabla
#stock si es aprobado y la tabla pedidos si es rechazado.        
def oknok():
    query = """
    SELECT presupuesto.idpresupuesto, presupuesto.idorden, presupuesto.desc_trabajo, presupuesto.p_repuestos, presupuesto.p_manodeobra, presupuesto.total
    FROM presupuesto
    WHERE estado = %s
    """
    values = ('Pendiente',)
    sql.cursor.execute(query, values)
    nombres_de_columnas = ['NRO. PRESUPUESTO', 'NRO. ORDEN', 'DESCRIPCION', 'REPUESTOS', 'MANO DE OBRA', 'TOTAL']
    presupuestos = sql.cursor.fetchall()
    df = pd.DataFrame(presupuestos, columns=nombres_de_columnas)
    if presupuestos:
        print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False, colalign=("center",)*len(nombres_de_columnas)))
        nrop = int(input('\nIngrese el numero de presupuesto a aprobar o rechazar: '))
        orden = 0
        for presupuesto in presupuestos:
            if nrop == presupuesto[0]:
                orden = presupuesto[1]
                break
        print("---------------------")
        print("(1) - A P R O B A R")
        print("(2) - R E C H A Z A R")
        print("---------------------")
        op = int(input("Su opcion: "))
        if op == "1":
             update(orden, "Aprobado")
             query = 'SELECT pedidos.idstock, pedidos.cantidad FROM pedidos WHERE idorden = %s'
             values = (orden,)
             sql.cursor.execute(query, values)
             pedidos = sql.cursor.fetchall()
             for pedido in pedidos:
                 idstock, cantidad = pedido
                 print(idstock, cantidad)
                 query = 'UPDATE stock SET existencia = existencia - %s WHERE idstock = %s'
                 values = (cantidad, idstock) 
                 sql.cursor.execute(query, values)
             sql.conexion.commit()
             print(f"\nEl presupuesto Nro. {nrop} ha sido aprobado y el stock actualizado.")
        elif op == 2:
            update(orden, "Rechazado")
            query = 'DELETE FROM pedidos WHERE idorden = %s'
            values = (orden,)
            sql.cursor.execute(query, values)
            sql.conexion.commit()
            print(f'El presupuesto Nº {nrop} ha sido rechazado y el pedido fue eliminado.')
        else:
            print("Opcion invalida")
    else:
        print("No hay presupuestos pendientes de aprobación")

#La funcion detalle() sirve para mostrar un presupuesto con la parte de los pedidos de stock.  
def detalle(id):
    if(consultar(id)):
        query = 'SELECT * FROM presupuesto WHERE idpresupuesto = %s'
        values = (id,)
        sql.cursor.execute(query, values)
        presupuesto = sql.cursor.fetchone()
        print(f"Nro. de Presupuesto: {presupuesto[0]}")
        print(f"Corresponde a Nro. de Orden: {presupuesto[1]}")
        print(f"Descripcion del trabajo realizado: {presupuesto[2]}")
        query = """
        SELECT pedidos.cantidad, stock.descripcion, pedidos.preciou,pedidos.subtotal 
        FROM stock 
        INNER JOIN pedidos ON stock.idstock = pedidos.idstock 
        WHERE idorden = %s
        """
        values = (presupuesto[1],)
        sql.cursor.execute(query, values)
        nombres_de_columnas = ['CANTIDAD', 'DESCRIPCION', 'PRECIO UNITARIO', 'SUBTOTAL']
        resultados = sql.cursor.fetchall()
        df = pd.DataFrame(resultados, columns=nombres_de_columnas)
        if resultados:
            print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False, colalign=("center",)*len(nombres_de_columnas)))
        print(f"Total de Repuestos: {presupuesto[3]}".rjust(62, " "))
        print(f"Precio de mano de obra: {presupuesto[4]}".rjust(62, " "))
        print(f"Importe total: {presupuesto[5]}".rjust(62, " "))
    else:
        print(f"No existe el presupesto N° {id}")
         

#Funcion para buscar un preseupuesto por numero de orden en la base de datos.
def buscar(id):
    query = 'SELECT * FROM presupuesto WHERE idorden = %s'
    values = (id,)
    sql.cursor.execute(query, values)
    presupuestos = sql.cursor.fetchall()
    if presupuestos:
        for presupuesto in presupuestos:
            print("-----------------------------------------------------")
            print(f"Nro. de Presupuesto: {presupuesto[0]}")
            print(f"Corresponde a Nro. de Orden: {presupuesto[1]}")
            print(f"Descripcion del trabajo realizado: {presupuesto[2]}")
            print(f"Precio de repuestos: {presupuesto[3]}")
            print(f"Precio de mano de obra: {presupuesto[4]}")
            print(f"Importe total: {presupuesto[5]}")
            print("----------------------------------------------------")
    else:
        print(f'La orden N° {id} no tiene cargado un presupuesto.')

#Funcion para mostrar todos los presupuestos creados en la base de datos. 
def mostrar():
    query = 'SELECT * FROM presupuesto'
    sql.cursor.execute(query)
    nombres_de_columnas = ['NRO. PRESUPUESTO', 'NRO. ORDEN', 'DESCRIPCION', 'REPUESTOS', 'MANO DE OBRA', 'TOTAL', 'ESTADO']
    presupuestos = sql.cursor.fetchall()
    df = pd.DataFrame(presupuestos, columns=nombres_de_columnas)
    if presupuestos:
        print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False, colalign=("center",)*len(nombres_de_columnas)))
    else:
        print('No hay ningun presupuesto cargado en la base de datos.')


#la función consultar(id) permite verificar la existencia de una presupuesto en la base de datos a través de su idpresupuesto, 
# devolviendo True si la orden existe y False si no existe.
def consultar(id):
    query = 'SELECT * FROM presupuesto WHERE idpresupuesto = %s'
    values = (id,)
    sql.cursor.execute(query, values)
    sql.cursor.fetchone()
    if(sql.cursor.rowcount == 1):
        return True
    else:
        return False

#La función update() actualiza una orden de trabajo existente
def update(id,status):
    query = "UPDATE presupuesto SET estado = %s WHERE idOrden = %s"
    values = (status, id)
    sql.cursor.execute(query, values)
    sql.conexion.commit()