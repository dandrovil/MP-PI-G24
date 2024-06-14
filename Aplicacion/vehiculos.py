import sql
import clientes

def agregar():
    patente = input("Ingrese la patente: (sin guiones) ")
    id_cliente = input("CUIT/DNI del cliente: (sin guiones) ")
    if (not clientes.consultar(id_cliente)):
        print(f'No existe ningun cliente con el DNI/CUIT: {id_cliente}')    
        return
    marca = input("Ingrese la marca: ")
    modelo = input("Ingrese el modelo: ")
    color = input("Ingrese el color: ")
    query = 'INSERT INTO autos (patente, id_Cliente, marca, modelo, color) VALUES (%s, %s, %s, %s, %s)'
    values = (patente, id_cliente, marca, modelo, color)
    sql.cursor.execute(query, values)
    sql.conexion.commit()
    print("Vehículo agregado exitosamente.")

def actualizar():
    patente = input("Ingrese la patente del vehículo que desea modificar: ")
    if consultar(patente):
        query = 'SELECT * FROM autos WHERE patente = %s'
        values = (patente,)
        sql.cursor.execute(query, values)
        patente = sql.cursor.fetchone()
        print("--------------------")
        print(f"DNI/CUIT: {patente[1]}")
        print(f"Marca: {patente[2]}")
        print(f"Modelo: {patente[3]}")
        print(f"Color: {patente[4]}")
        print("--------------------")
        id_cliente = input("CUIT/DNI del cliente: (sin guiones) ")
        if (not clientes.consultar(id_cliente)):
            print(f'No existe ningun cliente con el DNI/CUIT: {id_cliente}')               
            return
        marca = input("Ingrese la nueva marca: ")
        modelo = input("Ingrese el nuevo modelo: ")
        color = input("Ingrese el nuevo color: ")
        query = 'UPDATE autos SET id_Cliente = %s, marca = %s, modelo = %s, color = %s WHERE patente = %s'
        values = (id_cliente, marca, modelo, color, patente)
        sql.cursor.execute(query, values)
        sql.conexion.commit()
        print("Vehículo modificado exitosamente.")
    else:
        print("No se encontró ningún vehículo con esa patente.")

def buscar(id):
    query = "SELECT * FROM autos WHERE patente = %s"
    values = (id,)
    sql.cursor.execute(query,values)
    patentes = sql.cursor.fetchall()
    if patentes:
        for patente in patentes:
            print("--------------------")
            print(f"DNI/CUIT: {patente[1]}")
            print(f"Marca: {patente[2]}")
            print(f"Modelo: {patente[3]}")
            print(f"Color: {patente[4]}")
            print("--------------------")
    else:
        print(f"No se encontró ningún vehículo con esa patente {id}.")

def eliminar():
    patente = input("Ingrese la patente del vehículo que desea eliminar: ")
    if(consultar(patente)):
        query = 'DELETE FROM autos WHERE patente = %s'
        values = (patente,)
        sql.cursor.execute(query, values)
        sql.conexion.commit()
        print("Vehículo eliminado exitosamente.")
    else:
        print("No se encontró ningún vehículo con esa patente.")

def mostrar():
    query = 'SELECT * FROM autos'
    sql.cursor.execute(query)
    vehiculos = sql.cursor.fetchall()
    if vehiculos:
        for vehiculo in vehiculos:
            print(vehiculo)
    else:
        print("No hay vehículos registrados.")

def consultar(patente):
    query = 'SELECT * FROM autos WHERE patente = %s'
    values = (patente,)
    sql.cursor.execute(query, values)
    sql.cursor.fetchone()
    if(sql.cursor.rowcount == 1):
        return True
    else:
        return False