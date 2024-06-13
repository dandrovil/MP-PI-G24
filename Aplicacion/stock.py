import sql

#Funcion para CREAR NUEVOS ITEMS en el inventario. / LISTO
def agregar():
    idstock = input('Codigo de repuesto: ')
    marca = input('Marca: ')
    descripcion = input('Descripcion: ')
    existencia = input('Existencia: ')
    query = 'INSERT INTO stock (idstock, marca, descripcion, existencia) VALUES (%s, %s, %s, %s)'
    values = (idstock, marca, descripcion, existencia)
    sql.cursor.execute(query, values)
    sql.conexion.commit()
    print("Nuevo repuesto agregado con exito.")

#Funcion para ACTUALIZAR ITEMS en el inventario. / LISTO
def actualizar():
    idstock = input('Codigo de repuesto a actualizar: ')
    if(consultar(idstock)):
        query = 'SELECT * FROM stock WHERE idstock = %s'
        values = (idstock,)
        sql.cursor.execute(query, values)
        item = sql.cursor.fetchone()
        print("--------------------")
        print(f"Marca: {item[1]}")
        print(f"Descripcion: {item[2]}")
        print(f"Existencia: {item[3]}")
        print("--------------------")
        marca = input('Nuevo marca: ')
        descripcion = input('Nueva descripcion: ')
        existencia = input('Nueva existencia: ')
        query = 'UPDATE stock SET marca = %s, descripcion = %s, existencia = %s WHERE idstock = %s'
        values = (marca, descripcion, existencia, idstock)
        sql.cursor.execute(query, values)
        sql.conexion.commit()
        print(f'Repuesto con codigo {cod_repuesto} actualizado con exito.')
    else:
        print(f'Repuesto con codigo {cod_repuesto} NO existe.')

def buscar(id):
    query = "SELECT * FROM stock WHERE idstock = %s"
    values = (id,)
    sql.cursor.execute(query,values)
    stock = sql.cursor.fetchall()
    if stock:
        for item in stock:
            print("--------------------")
            print(f"Marca: {item[1]}")
            print(f"Descripcion: {item[2]}")
            print(f"Existencia: {item[3]}")
            print("--------------------")
    else:
        print(f"No hay repuestos con el codigo {id} en la base de datos.")

#Funcion para ELIMINAR ITEMS en el inventario. / LISTO
def eliminar():
    idstock = input('Codigo de repuesto a eliminar: ')
    if(consultar(idstock)):
        query = 'DELETE FROM stock WHERE idmeca = %s'
        values = (idstock,)
        sql.cursor.execute(query, values)
        sql.conexion.commit()
        print(f'ITEM con codigo de repuesto {idstock} eliminado con exito.')
    else:
        print(f'ITEM con codigo de repuesto {idstock} NO existe. No se realizaron modificaciones.')

#Funcion para MOSTRAR TODOS ITEMS en el inventario. / LISTO (REVISAR COMO HACER UN STOP)
def mostrar():
    query = 'SELECT * FROM stock'
    sql.cursor.execute(query)
    items = sql.cursor.fetchall()
    if items:
        for item in items:
            print (item)
    else:
        print('No hay ningun repuesto en la base de datos.')

#Buscar por codigo de repuesto usada anteriormente.
def consultar(idstock):
    query = 'SELECT * FROM stock WHERE idstock = %s'
    values = (idstock,)
    sql.cursor.execute(query, values)
    if(sql.cursor.rowcount == 1):
        return True
    else:
        return False
    
