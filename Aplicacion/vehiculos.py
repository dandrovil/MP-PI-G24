import sql, clientes
import pandas as pd
from tabulate import tabulate

#Funcion para crear un nuevo cliente en la base de datos.
def agregar():
    patente = input("Ingrese la patente: (sin guiones) ")
    marca = input("Ingrese la marca: ")
    modelo = input("Ingrese el modelo: ")
    color = input("Ingrese el color: ")
    id = input("CUIT/DNI del propietario: ")
    if (not clientes.consultar(id)):
        print(f'\nNo existe ningun propietario con el DNI/CUIT: {id}')    
        print("Operacion cancelada.")
        return
    query = 'INSERT INTO autos (patente, id_Cliente, marca, modelo, color) VALUES (%s, %s, %s, %s, %s)'
    values = (patente, id, marca, modelo, color)
    sql.cursor.execute(query, values)
    sql.conexion.commit()
    print(f"\nSe ha agregado el vehículo con dominio {patente} con exito.")

#Funcion para actualizar datos de un cliente en la base de datos.
def actualizar():
    pat = input("Ingrese la patente del vehículo que desea modificar: ")
    if consultar(pat):
        query = 'SELECT autos.marca, autos.modelo, autos.color, clientes.apeynom FROM autos INNER JOIN clientes ON autos.id_Cliente = clientes.dni_cuit WHERE patente = %s'
        values = (pat,)
        sql.cursor.execute(query, values)
        patente = sql.cursor.fetchone()
        print("------------------------------------------")
        print(f"(1) - Marca: {patente[0]}")
        print(f"(2) - Modelo: {patente[1]}")
        print(f"(3) - Color: {patente[2]}")
        print(f"(4) - Propietario: {patente[3]}")
        print("------------------------------------------")
        mod = int(input("Que campo desea modificar: "))
        if mod == 1:
            marca = input('Ingrese nueva marca: ')
        elif mod == 2:
            modelo = input( 'Ingrese nuevo modelo: ')
        elif mod == 3:
            color = input('Ingrese nuevo color: ')
        elif mod == 4:
            id_cliente = input('Ingrese el DNI/CUIT del nuevo propietario: (solo numeros) ')
            if (not clientes.consultar(id_cliente)):
                print(f'\nNo existe ningun propietario con el DNI/CUIT: {id_cliente}')               
                print("Operacion cancelada.")
                return
        else:
            print("Opcion no valida")
            return
        query = f'UPDATE autos SET {"marca" if mod == 1 else "modelo" if mod == 2 else "color" if mod == 3 else "id_Cliente"} = %s WHERE patente = %s'
        values = (marca if mod == 1 else modelo if mod == 2 else color if mod == 3 else id_cliente, pat)
        sql.cursor.execute(query, values)
        sql.conexion.commit()
        print(f"\nEl vehículo {pat} ha sido modificado.")
    else:
        print(f"\nEl vehiculo {pat} no existe en la base de datos.")

#Funcion para buscar un vehiculo por patente en la base de datos.
def buscar_patente(id):
    query = 'SELECT autos.marca, autos.modelo, autos.color, clientes.apeynom FROM autos INNER JOIN clientes ON autos.id_Cliente = clientes.dni_cuit WHERE patente = %s'
    values = (id,)
    sql.cursor.execute(query,values)
    patentes = sql.cursor.fetchall()
    if patentes:
        for patente in patentes:
            print("------------------------------------------")
            print(f"Marca: {patente[0]}")
            print(f"Modelo: {patente[1]}")
            print(f"Color: {patente[2]}")
            print(f"Propietario: {patente[3]}")
            print("------------------------------------------")
    else:
        print(f"No se encontró ningún vehículo con esa patente {id}.")

#Funcion para buscar un vehiculo por cliente en la base de datos.
def buscar_propietario(id):
    if (clientes.consultar(id)):
        query = 'SELECT * FROM autos WHERE id_Cliente = %s'
        values = (id,)
        sql.cursor.execute(query,values)
        patentes = sql.cursor.fetchall()
        if patentes:
            for patente in patentes:
                print("------------------------------------------")
                print(f"Marca: {patente[2]}")
                print(f"Modelo: {patente[3]}")
                print(f"Color: {patente[4]}")
                print(f"Dominio: {patente[0]}")
                print("------------------------------------------")
        else:
            print(f"No se encontró ningún vehículo con esa patente {id}.")

#Funcion para eliminar un vehiculo en la base de datos.
def eliminar():
    patente = input("Patente del vehículo: ")
    if(consultar(patente)):
        query = 'SELECT autos.marca, autos.modelo, autos.color, clientes.apeynom FROM autos INNER JOIN clientes ON autos.id_Cliente = clientes.dni_cuit WHERE patente = %s'
        values = (patente,)
        sql.cursor.execute(query, values)
        vehiculos = sql.cursor.fetchall()
        for vehiculo in vehiculos:
            print("------------------------------------------")
            print(f"Marca: {vehiculo[0]}")
            print(f"Modelo: {vehiculo[1]}")
            print(f"Color: {vehiculo[2]}")
            print(f"Propietario: {vehiculo[3]}")
            print("------------------------------------------")
        confirmacion = input("¿Está seguro de eliminar este vehiculo? (s/n): ")
        if confirmacion.lower() == 's':
            query = 'DELETE FROM autos WHERE patente = %s'
            values = (patente,)
            sql.cursor.execute(query, values)
            sql.conexion.commit()
            print(f"\nEl vehículo {patente} ha sido eliminado.")
        else:
            print(f'\nOperación cancelada.')
    else:
        print(f"\nEl vehículo {patente} no existe en la base de datos.")

#Funcion para mostrar todos los vehiculos en la base de datos.
def mostrar():
    query = 'SELECT autos.marca, autos.modelo, autos.color, autos.patente, clientes.apeynom FROM autos INNER JOIN clientes ON autos.id_Cliente = clientes.dni_cuit ORDER BY marca asc'
    sql.cursor.execute(query)
    nombres_de_columnas = ['MARCA', 'MODELO', 'COLOR', 'DOMINIO', 'PROPIETARIO']
    vehiculos = sql.cursor.fetchall()
    df = pd.DataFrame(vehiculos, columns=nombres_de_columnas)
    if vehiculos:
        print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False, colalign=("center",)*len(nombres_de_columnas)))
    else:
        print("No hay vehículos registrados en la base de datos.")

#Funcion para consultar si existe un vehiculo en la base de datos.
def consultar(id):
    query = 'SELECT * FROM autos WHERE patente = %s'
    values = (id,)
    sql.cursor.execute(query, values)
    sql.cursor.fetchone()
    if(sql.cursor.rowcount == 1):
        return True
    else:
        return False