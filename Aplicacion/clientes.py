import sql
import pandas as pd
from tabulate import tabulate

#Funcion para crear un nuevo cliente en la base de datos.
def agregar():
    dni_cuit = input('DNI/CUIT del Cliente: (solo numeros) ')
    apeynom = input('Cliente: ')
    direccion = input('Direccion: ')
    telefono = input('Telefono: ')
    email = input ('Email: ')
    query = 'INSERT INTO clientes (dni_cuit, apeynom, telefono, direccion, email) VALUES (%s, %s, %s, %s, %s)'
    values = (dni_cuit, apeynom, telefono, direccion, email)
    sql.cursor.execute(query, values)
    sql.conexion.commit()
    print(f'\nSe agregado el cliente {apeynom} con exito.')

#Funcion para actualizar datos de un cliente en la base de datos.
def actualizar():
    dni_cuit = input('DNI/CUIT del Cliente: ')
    if(consultar(dni_cuit)):
        query = 'SELECT * FROM clientes WHERE dni_cuit = %s'
        values = (dni_cuit,)
        sql.cursor.execute(query, values)
        cliente = sql.cursor.fetchone()
        print("------------------------------------------")
        print(f"(1) - Cliente: {cliente[1]}")
        print(f"(2) - Direccion: {cliente[2]}")
        print(f"(3) - Telefono: {cliente[3]}")
        print(f"(4) - Email: {cliente[4]}")
        print("------------------------------------------")
        mod = int(input("Que campo desea modificar: "))
        if mod == 1:
            apeynom = input('Ingrese nuevo cliente: ')
        elif mod == 2:
            direccion = input( 'Ingrese nueva direccion: ')
        elif mod == 3:
            telefono = input('Ingrese nuevo telefono: ')
        elif mod == 4:
            email = input('Ingrese nuevo E-mail: ')
        else:
            print("Opcion no valida")
            return
        query = f'UPDATE clientes SET {"apeynom" if mod == 1 else "direccion" if mod == 2 else "telefono" if mod == 3 else "email"} = %s WHERE dni_cuit = %s'
        values = (apeynom if mod == 1 else direccion if mod == 2 else telefono if mod == 3 else email, dni_cuit)
        sql.cursor.execute(query, values)
        sql.conexion.commit()
        print(f'\nEl cliente {dni_cuit} ha sido actualizado.')
    else:
        print(f'\nEl cliente {dni_cuit} no existe en la base de datos.')
        
#Funcion para buscar un cliente en la base de datos.
def buscar(id):
    query = "SELECT * FROM clientes WHERE dni_cuit = %s"
    values = (id,)
    sql.cursor.execute(query,values)
    clientes = sql.cursor.fetchall()
    if clientes:
        for cliente in clientes:
            print("------------------------------------------")
            print(f"Cliente: {cliente[1]}")
            print(f"Direccion: {cliente[2]}")
            print(f"Telefono: {cliente[3]}")
            print(f"E-mail: {cliente[4]}")
            print("------------------------------------------")
    else:
        print(f"\nEl cliente {id} no existe en la base de datos.")

#Funcion para eliminar un cliente en la base de datos.
def eliminar():
    dni_cuit = input('DNI/CUIT del cliente: ')
    if(consultar(dni_cuit)):
        query = "SELECT * FROM clientes WHERE dni_cuit = %s"
        values = (dni_cuit,)
        sql.cursor.execute(query, values)
        clientes = sql.cursor.fetchall()
        for cliente in clientes:
            print("------------------------------------------")
            print(f"Cliente: {cliente[1]}")
            print(f"Direccion: {cliente[2]}")
            print(f"Telefono: {cliente[3]}")
            print(f"E-mail: {cliente[4]}")
            print("------------------------------------------")
        confirmacion = input("¿Está seguro de eliminar este cliente? (s/n): ")
        if confirmacion.lower() == 's':
            query = "DELETE FROM clientes WHERE dni_cuit = %s"
            values = (dni_cuit,)
            sql.cursor.execute(query,values)
            sql.conexion.commit()
            print(f'\nEl cliente {dni_cuit} ha sido eliminado.')
        else:
            print(f'\nOperación cancelada.')
    else:
        print(f"'\nEl codigo {dni_cuit} no existe en la base de datos.")

#Funcion para mostrar todos los clientes en la base de datos.
def mostrar():
    query = 'SELECT * FROM clientes ORDER BY apeynom ASC'
    sql.cursor.execute(query)
    nombres_de_columnas = ['DNI / CUIT', 'CLIENTE', 'DIRECCION', 'TELEFONO', 'E-MAIL']
    clientes = sql.cursor.fetchall()
    df = pd.DataFrame(clientes, columns=nombres_de_columnas)
    if clientes:
        print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False, colalign=("center",)*len(nombres_de_columnas)))
    else:
        print('No hay clientes registrados en la base de datos')
           
#Funcion para consultar si existe un cliente en la base de datos.
def consultar(id):
    query = 'SELECT * FROM clientes WHERE dni_cuit = %s'
    values = (id,)
    sql.cursor.execute(query, values)
    sql.cursor.fetchone()
    if(sql.cursor.rowcount == 1):
        return True
    else:
        return False