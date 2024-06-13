import sql

#Funcion para CREAR NUEVO CLIENTE en el inventario.
def agregar():
    dni_cuit = input('DNI/CUIT del Cliente: (sin guiones) ')
    apeynom = input('Apellido y Nombre del Cliente: ')
    direccion = input('Direccion del Cliente: ')
    telefono = input('Telefono del Cliente: ')
    email = input ('Email del Cliente: ')
    query = 'INSERT INTO clientes (dni_cuit, apeynom, telefono, direccion, email) VALUES (%s, %s, %s, %s, %s)'
    values = (dni_cuit, apeynom, telefono, direccion, email)
    sql.cursor.execute(query, values)
    sql.conexion.commit()
    print('Nuevo cliente agregado con exito.')

#Funcion para ACTUALIZAR DATOS DE UN CLIENTE en el inventario.
def actualizar():
    dni_cuit = input('DNI/CUIT del Cliente: (sin guiones) ')
    if(consultar(dni_cuit)):
        query = 'SELECT * FROM clientes WHERE dni_cuit = %s'
        values = (dni_cuit,)
        sql.cursor.execute(query, values)
        cliente = sql.cursor.fetchone()
        print("--------------------")
        print(f"Apellido y Nombre: {cliente[1]}")
        print(f"Direccion: {cliente[2]}")
        print(f"Telefono: {cliente[3]}")
        print(f"Email: {cliente[4]}")
        print("--------------------")
        apeynom = input('Nuevo apellido y nombre: ')
        direccion = input( 'Direccion: ')
        telefono = input('Telefono: ')
        email= input ('Email: ')
        query = 'UPDATE clientes SET apeynom = %s, direccion = %s, telefono = %s, email = %s WHERE dni_cuit = %s'
        values = (apeynom, direccion, telefono, email, dni_cuit)
        sql.cursor.execute(query, values)
        sql.conexion.commit()
        print(f'Cliente con DNI/CUIT {dni_cuit} actualizado con exito.')
    else:
        print(f'Cliente con DNI/CUIT {dni_cuit} NO existe.')

#Funcion para ELIMINAR UN CLIENTE en el inventario.
def eliminar():
    print("Ingrese el DNI/CUIT sin guiones ")
    dni_cuit = input('DNI/CUIT del cliente: ')
    if(consultar(dni_cuit)):
        query = 'DELETE FROM clientes WHERE dni_cuit = %s'
        values = (dni_cuit,)
        sql.cursor.execute(query, values)
        sql.conexion.commit()
        print(f'Cliente con ID {dni_cuit} eliminado con exito.')
    else:
        print(f'Cliente con ID {dni_cuit} NO existe.')

#Funcion para MOSTRAR TODOS LOS CLIENTES en el inventario.
def mostrar():
    query = 'SELECT * FROM clientes'
    sql.cursor.execute(query)
    clientes = sql.cursor.fetchall()
    if clientes:
        for cliente in clientes:
            print(cliente)
    else:
        print('No hay datos de ningun cliente en la base de datos')
        
#Funcion para BUSCAR UN CLIENTE por cuit en el inventario.
def consultar(dni_cuit):
    query = 'SELECT * FROM clientes WHERE dni_cuit = %s'
    values = (dni_cuit,)
    sql.cursor.execute(query, values)
    clienteunico = sql.cursor.fetchone()
    if(sql.cursor.rowcount == 1):
        return True
    else:
        return False