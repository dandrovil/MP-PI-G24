import sql
import pandas as pd
from tabulate import tabulate

#Funcion para crear un nuevo cliente en la base de datos.
def agregar():
    apeynom = input('Apellido y Nombre: ')
    especialidad = input('Especialidad: ')
    telefono = input('Telefono: ')
    email = input('Email: ')
    query = 'INSERT INTO Mecanico (apeynom, especialidad, telefono, email) VALUES (%s, %s, %s, %s)'
    values = (apeynom, especialidad, telefono, email)
    sql.cursor.execute(query, values)
    sql.conexion.commit()
    print(f'\nSe agregado el mecanico {apeynom} con exito.')
    
#Funcion para actualizar datos de un vehiculo en la base de datos.
def actualizar():
    idmeca = input('Codigo del mecanico: ')
    if(consultar(idmeca)):
        query = 'SELECT * FROM mecanicos WHERE idmeca = %s'
        values = (idmeca,)
        sql.cursor.execute(query,values)
        mecanico = sql.cursor.fetchone()
        print("------------------------------------------")
        print(f"(1) - Apellido y Nombre: {mecanico[1]}")
        print(f"(2) - Especialidad: {mecanico[2]}")
        print(f"(3) - Telefono: {mecanico[3]}")
        print(f"(4) - Email: {mecanico[4]}")
        print("------------------------------------------")
        mod = int(input("Que campo desea modificar: "))
        if mod == 1:
            apeynom = input('Ingrese nuevo apelldio y nombre: ')
        elif mod == 2:
            especialidad = input( 'Ingrese nueva especialidad: ')
        elif mod == 3:
            telefono = input('Ingrese nuevo telefono: ')
        elif mod == 4:
            email = input('Ingrese nuevo E-mail: ')
        else:
            print("Opcion no valida")
            return
        query = f'UPDATE mecanicos SET {"apeynom" if mod == 1 else "especialidad" if mod == 2 else "telefono" if mod == 3 else "email"} = %s WHERE idmeca = %s'
        values = (apeynom, especialidad, telefono, email, idmeca)
        sql.cursor.execute(query, values)
        sql.conexion.commit()
        print(f'nEl mecanico {idmeca} actualizado con exito.')
    else:
        print(f'\nEl mecanico {idmeca} no existe en la base de datos.')

#Funcion para buscar un cliente en la base de datos.
def buscar(id):
    query = "SELECT * FROM mecanicos WHERE idmeca = %s"
    values = (id,)
    sql.cursor.execute(query,values)
    mecanicos = sql.cursor.fetchall()
    if mecanicos:
        for mecanico in mecanicos:
            print("------------------------------------------")
            print(f"Apellido y Nombre: {mecanico[1]}")
            print(f"Especialidad: {mecanico[2]}")
            print(f"Telefono: {mecanico[3]}")
            print(f"Email: {mecanico[4]}")
            print("------------------------------------------")
    else:
        print(f"\nEl mecanicos {id} no existe en la base de datos.")

#Funcion para eliminar un cliente en la base de datos.
def eliminar():
    idmeca = input('Codigo del mecanico: ')
    if(consultar(idmeca)):
        query = "SELECT * FROM mecanicos WHERE idmeca = %s"
        values = (idmeca,)
        sql.cursor.execute(query,values)
        mecanicos = sql.cursor.fetchall()
        for mecanico in mecanicos:
            print("------------------------------------------")
            print(f"Cliente: {mecanico[1]}")
            print(f"Direccion: {mecanico[2]}")
            print(f"Telefono: {mecanico[3]}")
            print(f"E-mail: {mecanico[4]}")
            print("------------------------------------------")
        confirmacion = input("¿Está seguro de eliminar este mecanico? (s/n): ")
        if confirmacion.lower() == 's':
            query = 'DELETE FROM mecanicos WHERE idmeca = %s'
            values = (idmeca,)
            sql.cursor.execute(query, values)
            sql.conexion.commit()
            print(f'El mecanico {idmeca} ha sido eliminado.')
        else:
            print(f'\nOperación cancelada.')
    else:
        print(f'Mecanico con ID {idmeca} no existe en la base de datos.')


#Funcion para mostrar todos los clientes en la base de datos.
def mostrar():
    query = 'SELECT * FROM mecanicos ORDER BY apeynom ASC'
    sql.cursor.execute(query)
    nombres_de_columnas = ['DNI / CUIT', 'CLIENTE', 'DIRECCION', 'TELEFONO', 'E-MAIL']
    mecanicos = sql.cursor.fetchall()
    df = pd.DataFrame(mecanicos, columns=nombres_de_columnas)
    if mecanicos:
         print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False, colalign=("center",)*len(nombres_de_columnas)))
    else:
        print('No hay mecanicos registrados en la base de datos')

#Funcion para consultar si existe un cliente en la base de datos.
def consultar(id):
    query = 'SELECT * FROM mecanicos WHERE idmeca = %s'
    values = (id,)
    sql.cursor.execute(query,values)
    sql.cursor.fetchone()   
    if(sql.cursor.rowcount == 1):
        return True
    else:
        return False