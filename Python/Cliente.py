import sql

#Funcion para CREAR NUEVO CLIENTE en el inventario.
def agregar():
    cuit_cliente = input('Cuit del CLIENTE: ')
    nombre = input ('Nombre del CLIENTE: ')
    apellido = input('Apellido del CLIENTE: ')
    direccion = input('Direccion del CLIENTE: ')
    telefono = input('Telefono del CLIENTE: ')
    email= input ('Email del CLIENTE: ')
   

    query = 'INSERT INTO clientes (cuit_cliente, nombre, apellido, telefono, direccion, email) VALUES (%s, %s, %s, %s, %s, %s)'
    values = (cuit_cliente, nombre, apellido, telefono, direccion, email)

    sql.cursor.execute(query, values)
    sql.conexion.commit()

    print('Nuevo cliente agregado con exito.')

#? En este caso no hay mensaje de error, se deberia mostrar?

#Funcion para ACTUALIZAR DATOS DE UN CLIENTE en el inventario.
def actualizar():
    cuit_cliente = input('CUIT del Cliente: ')
    if(buscarCliente(cuit_cliente)):
        nombre = input ('Nuevo nombre del CLIENTE: ')
        apellido = input('Nuevo apellido del CLIENTE')
        direccion = input( 'Direccion del CLIENTE')
        telefono = input('Telefono del CLIENTE: ')
        email= input ('Email del CLIENTE')
   
        

        query = 'UPDATE clientes SET nombre = %s, apellido = %s, telefono = %s, direccion = %s, email = %s WHERE cuit_cliente = %s'
        values = (nombre, apellido, telefono, direccion, email)

        sql.cursor.execute(query, values)
        sql.conexion.commit()
        print(f'Cliente con ID {cuit_cliente} actualizado con exito.')
    else:
        print(f'Cliente con ID {cuit_cliente} NO existe. No se realizaron modificaciones.')


#Funcion para ELIMINAR UN CLIENTE en el inventario.
def eliminar():
    cuit_cliente = input('Cuit del cliente: ')
    if(buscarCliente(cuit_cliente)):
        query = 'DELETE FROM clientes WHERE cuit_cliente = %s'
        values = (cuit_cliente,)

        sql.cursor.execute(query, values)
        sql.conexion.commit()
        print(f'Cliente con ID {cuit_cliente} eliminado con exito.')
    else:
        print(f'Cliente con ID {cuit_cliente} NO existe. No se realizaron modificaciones.')


#Funcion para BUSCAR UN CLIENTE por cuit en el inventario.
def buscarCliente(cuit_cliente):
    query = 'SELECT * FROM clientes WHERE cuit_cliente = %s'
    values = (cuit_cliente,)
    sql.cursor.execute(query, values)
    clienteUnico = sql.cursor.fetchone()

    print(sql.cursor.rowcount, 'Filas afectadas')

    if(sql.cursor.rowcount == 1):
        print(clienteUnico)
        return True
    else:
        print(f'No existe ningun cliente con el ID: {cuit_cliente}')
        return False


#Funcion para MOSTRAR TODOS LOS CLIENTES en el inventario.
def mostrar_clientes():
    query = 'SELECT * FROM clientes'
    sql.cursor.execute(query)
    clientes = sql.cursor.fetchall()

    if clientes:
        for cliente in clientes:
            print(cliente)
    else:
        print('No hay datos de ningun cliente en la base de datos')


