import sql

#Funcion para CREAR NUEVO MECANICO en la base de datos. / LISTO
def agregar():
    idmeca = input('Codigo del mecanico: ')
    apeynom = input('Apellido y Nombre del mecanico: ')
    especialidad = input('Especialidad del mecanico: ')
    telefono = input('Telefono del mecanico: ')
    email = input('Email del mecanico: ')
    query = 'INSERT INTO Mecanico (idmeca, apeynom, especialidad, telefono, email) VALUES (%s, %s, %s, %s, %s)'
    values = (idmeca, apeynom, especialidad, telefono, email)
    sql.cursor.execute(query, values)
    sql.conexion.commit()
    print('Nuevo mecanico agregado con exito.')

#Funcion para ACTUALIZAR DATOS DE UN MECANICO en la base de datos. / LISTO
def actualizar():
    id = input('Codigo del mecanico: ')
    if(consultar(id)):
        query = 'SELECT * FROM mecanicos WHERE idmeca = %s'
        values = (id,)
        sql.cursor.execute(query,values)
        mecanico = sql.cursor.fetchone()
        print("--------------------")
        print(f"Apellido y Nombre: {mecanico[1]}")
        print(f"Especialidad: {mecanico[2]}")
        print(f"Telefono: {mecanico[3]}")
        print(f"Email: {mecanico[4]}")
        print("--------------------")
        apeynom = input('Nuevo apellido y nombre del mecanico: ')
        especialidad = input('Nuevo especialidad del mecanico: ')
        telefono = input('Nuevo telefono del mecanico: ')
        email = input('Nuevo email del mecanico: ')
        query = 'UPDATE mecanicos SET apeynom = %s, especialidad = %s, telefono = %s, email = %s WHERE idmeca = %s'
        values = (apeynom, especialidad, telefono, email, idmeca)
        sql.cursor.execute(query, values)
        sql.conexion.commit()
        print(f'Mecanico con codigo {idmeca} actualizado con exito.')
    else:
        print(f'Mecanico con codigo {idmeca} NO existe.')


#Funcion para ELIMINAR UN MECANICO en la base de datos. / LISTO
def eliminar():
    idmeca = input('Codigo del mecanico a eliminar: ')
    if(consultar(idmeca)):
        query = 'DELETE FROM mecanicos WHERE idmeca = %s'
        values = (idmeca,)
        sql.cursor.execute(query, values)
        sql.conexion.commit()
        print(f'Mecanico con codigo {idmeca} eliminado con exito.')
    else:
        print(f'Mecanico con ID {idmeca} NO existe. No se realizaron modificaciones.')

def buscar(id):
    query = "SELECT * FROM mecanicos WHERE idmeca = %s"
    values = (id,)
    sql.cursor.execute(query,values)
    mecanicos = sql.cursor.fetchall()
    if mecanicos:
        for mecanico in mecanicos:
            print("--------------------")
            print(f"Apellido y Nombre: {mecanico[1]}")
            print(f"Especialidad: {mecanico[2]}")
            print(f"Telefono: {mecanico[3]}")
            print(f"Email: {mecanico[4]}")
            print("--------------------")
    else:
        print(f"No hay mecanicos con el codigo {id} en la base de datos.")

#Funcion para MOSTRAR TODOS LOS MECANICO en la base de datos. / LISTO
def mostrar():
    query = 'SELECT * FROM mecanicos'
    sql.cursor.execute(query)
    mecanicos = sql.cursor.fetchall()
    if mecanicos:
        for mecanico in mecanicos:
            print(mecanico)
    else:
        print('No hay datos de ningun mecanico en la base de datos')

#BUSCAR UN MECANICO POR CODIGO de mecanico en la base de datos. Funcion usada anteriormente.
def consultar(id):
    query = 'SELECT * FROM mecanicos WHERE idmeca = %s'
    values = (id,)
    sql.cursor.execute(query,values)
    sql.cursor.fetchone()   
    if(sql.cursor.rowcount == 1):
        return True
    else:
        return False