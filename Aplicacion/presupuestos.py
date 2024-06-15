import sql
import mecanicos,stock, ot

#Funcion para CREAR  NUEVO PRESUPUESTO en la base  de datos. / LISTO
def crear():
    idmeca = input('Ingrese su codigo del mecanico: ')
    if(mecanicos.consultar(idmeca)):
        query = "SELECT * FROM ordenes WHERE mecanico = %s AND estado = %s"
        values = (idmeca, "ASIGNADO")
        sql.cursor.execute(query,values)
        ordenes = sql.cursor.fetchall()
        if ordenes:
            for orden in ordenes:
                print("--------------------")
                print(f"Nro. de Orden: {orden[0]}")
                print(f"Vehiculo: {orden[1]}")
                print(f"Fecha ingreso: {orden[2].strftime("%Y-%m-%d")}")
                print(f"Motivo: {orden[3]}")
                print("--------------------")
            nroorden = input("Ingrese numero de orden a presupuestar: ")
            tot = 0
            opc = True
            while opc:
                nrorep = input("Ingrese Codigo de repuesto: ")
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
                    opc = input("Quiere cargar mas repuestos(S/N): ")
                    if opc.lower() == "n":
                        opc = False
                else:
                    print(f"El codigo {nrorep} es inexistente")
        else:
             print("No tiene ordenes para presupuestar.")
             return
    else:
        print(f'El codigo de mecanico {idmeca} no existe.')
        return
    
    trabajo = input("Describa trabajo realizado: ")
    costo = float(input("Ingrese costo de mano de obra: $ "))
    total = tot + costo
    query = 'INSERT INTO presupuesto (idorden, desc_trabajo, p_repuestos, p_manodeobra, total) VALUES (%s, %s, %s, %s, %s)'
    values = (nroorden, trabajo, tot, costo, total)
    sql.cursor.execute(query, values)
    sql.conexion.commit()
    ot.update(nroorden, "PRESUPUESTADO")
    print(f"Presupuesto para la orden de trabajo N° {nroorden} ha sido confeccionado")
    
#Funcion para ACTUALIZAR DATOS DE UN PRESUPUESTO en la base de datos. / LISTO
def actualizar():
    cod_presupuesto = int(input('Codigo del presupuesto que desea modificar: '))
    if(buscarPresupuesto(cod_presupuesto)):
        cantidad = int(input('Nueva cantidad: '))
        precio_unitario = int(input('Nuevo precio unitario: '))
        mano_obra = int(input('Nuevo precio por mano de obra: '))
        subtotal = int(input('Nuevo subtotal: '))

        query = 'UPDATE taller.Presupuesto SET cantidad = %s, precio_unitario = %s, mano_obra = %s, subtotal = %s WHERE cod_presupuesto = %s'
        values = (cantidad, precio_unitario, mano_obra, subtotal, cod_presupuesto)

        sql.cursor.execute(query, values)
        sql.conexion.commit()
        print(f'Presupuesto con codigo {cod_presupuesto} modificado con exito')
    else:
        print(f'NO EXISTE presupuesto con codigo {cod_presupuesto}. No se realizaron modificaciones.')

def oknok():
    query = 'SELECT * FROM presupuesto'
    sql.cursor.execute(query)
    presupuestos = sql.cursor.fetchall()
    if presupuestos:
        for presupuesto in presupuestos:
            print(presupuesto)
    else:
        print("No hay presupuestos para mostrar")
    
    p = input('Ingrese el numero de presupuesto a aprobar o rechazar: ')
    o = 0
    for presupuesto in presupuestos:
        if p == presupuestos[0]:
            o == presupuestos[1]
    e = input("Aprobado o Rechazado (A/R): ")
    if e.lower() == "r":
        ot.update(o, "RECHAZADO")
        query = 'DELETE FROM pedidos WHERE idorden = %s'
        values = (o,)
        sql.cursor.execute(query, values)
        sql.conexion.commit()
        query = 'DELETE FROM presupuesto WHERE idpresupuesto = %s'
        values = (p,)
        sql.cursor.execute(query, values)
        sql.conexion.commit()
        print(f'El presupuesto Nº {p} fue eliminado.')
    elif e.lower() == "a":
         ot.update(o, "APROBADO")
    else:
        return
  
def detalle(id):
    if(consultar(id)):
        query = 'SELECT * FROM presupuesto WHERE idpresupuesto = %s'
        values = (id,)
        sql.cursor.execute(query, values)
        presupuesto = sql.cursor.fetchone()
        print("-----------------------------------------------------")
        print(f"Nro. de Presupuesto: {presupuesto[0]}")
        print(f"Corresponde a Nro. de Orden: {presupuesto[1]}")
        print(f"Descripcion del trabajo realizado: {presupuesto[2]}")
        print("-----------------------------------------------------")
        query = 'select stock.descripcion, pedidos.cantidad, pedidos.preciou from stock inner join pedidos on stock.idstock = pedidos.idstock where idorden = %s'
        values = (presupuesto[1],)
        sql.cursor.execute(query, values)
        resultados = sql.cursor.fetchall()
        for resultado in resultados:
            print(resultado)
        print("-----------------------------------------------------")
        print(f"Total de Repuestos: {presupuesto[3]}")
        print(f"Precio de mano de obra: {presupuesto[4]}")
        print(f"Importe total: {presupuesto[5]}")
        print("----------------------------------------------------")
    else:
        print(f"No existe el presupesto N° {id}")
         

#Funcion para BUCAR UN PRESUPUESTO POR CODIGO en la base. / LISTO
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

#Funcion para MOSTRAR TODOS LOS PRESUPUESTOS creados en la base de datos. / LISTO
def mostrar():
    query = 'SELECT * FROM presupuesto'
    sql.cursor.execute(query)
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
        print('No hay ningun presupuesto cargado en la base de datos.')


#######################################################################
#BUSCAR UN PRESUPUESTO POR CODIGO. Funcion usada anteriormente.
def consultar(id):
    query = 'SELECT * FROM presupuesto WHERE idpresupuesto = %s'
    values = (id,)
    sql.cursor.execute(query, values)
    sql.cursor.fetchone()
    if(sql.cursor.rowcount == 1):
        return True
    else:
        return False