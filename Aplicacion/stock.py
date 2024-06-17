import sql
import pandas as pd
from tabulate import tabulate

#Funcion para agregar nuevos items en el inventario. 
def agregar():
    marca = input('Marca: ')
    descripcion = input('Descripcion: ')
    existencia = input('Existencia: ')
    query = 'INSERT INTO stock (marca, descripcion, existencia) VALUES (%s, %s, %s)'
    values = (marca, descripcion, existencia)
    sql.cursor.execute(query, values)
    sql.conexion.commit()
    print("\nNuevo repuesto agregado con exito.")

#Funcion para actualizar datps de un item en el inventario.
def actualizar():
    idstock = input('Codigo de repuesto a actualizar: ')
    if(consultar(idstock)):
        query = 'SELECT * FROM stock WHERE idstock = %s'
        values = (idstock,)
        sql.cursor.execute(query, values)
        item = sql.cursor.fetchone()
        print("------------------------------------------")
        print(f"(1) - Marca: {item[1]}")
        print(f"(2) - Descripcion: {item[2]}")
        print(f"(3) - Existencia: {item[3]}")
        print("------------------------------------------")
        mod = int(input("Que campo desea modificar: "))
        if mod == 1:
            marca = input('Ingrese nuevo marca: ')
        elif mod == 2:
            desc = input( 'Ingrese nueva descripcion: ')
        elif mod == 3:
            cant = input('Ingrese nuevo cantidad: ')
        else:
            print("Opcion no valida")
            return
        query = f'UPDATE stock SET {"marca" if mod == 1 else "descripcion" if mod == 2 else "existencia"} = %s WHERE idstock = %s'
        values = (marca if mod == 1 else desc if mod == 2 else cant, idstock)
        sql.cursor.execute(query, values)
        sql.conexion.commit()
        print(f'\nEl repuesto con codigo {idstock} ha sido actualizado.')
    else:
        print(f'\nEl repuesto con codigo {idstock} no existe en la base de datos.')

#Funcion para buscar un repuesto en el inventario.
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
        print(f"\nNo hay repuestos con el codigo {id} en la base de datos.")

#Funcion para eliminar un item del inventario. 
def eliminar():
    idstock = input('Codigo de repuesto a eliminar: ')
    if(consultar(idstock)):
         query = "SELECT * FROM stock WHERE idstock = %s"
         values = (idstock,)
         sql.cursor.execute(query, values)
         items = sql.cursor.fetchall()
         for item in items:
            print("------------------------------------------")
            print(f"Marca: {item[1]}")
            print(f"Descripcion: {item[2]}")
            print(f"Existencia: {item[3]}")
            print("------------------------------------------")
         confirmacion = input("¿Está seguro de eliminar este item? (s/n): ")
         if confirmacion.lower() == 's':
             query = 'DELETE FROM stock WHERE idstock = %s'
             values = (idstock,)
             sql.cursor.execute(query, values)
             sql.conexion.commit()
             print(f'\nEl repuesto codigo {idstock} ha sido eliminado.')
         else:
             print(f'\nOpcion invalida - Operación cancelada.')
    else:
         print(f'\nEl item con codigo de repuesto {idstock} no existe en la base de datos.')

#Funcion para mostrar todos los items en el inventario.
def mostrar():
    query = 'SELECT * FROM stock ORDER BY marca ASC'
    sql.cursor.execute(query)
    nombres_de_columnas = ['CODIGO', 'MARCA', 'DESCRIPCION', 'EXISTENCIA']
    items = sql.cursor.fetchall()
    df = pd.DataFrame(items, columns=nombres_de_columnas)
    if items:
        print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False, colalign=("center",)*len(nombres_de_columnas)))
    else:
        print('No hay ningun repuesto en la base de datos.')

#Funcion para consultar si existe un repuesto en el inventario.
def consultar(idstock):
    query = 'SELECT * FROM stock WHERE idstock = %s'
    values = (idstock,)
    sql.cursor.execute(query, values)
    sql.cursor.fetchone()
    if(sql.cursor.rowcount == 1):
        return True
    else:
        return False
    
