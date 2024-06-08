import os
import msvcrt
import ot, clientes, vehiculos, stock
import sql

def mostrar_menu():
    while True:
        os.system('cls')
        print("............Bienvenido al Sistema de Taller Mecanico..............")
        print("")
        print("                    <<< MENU PRINCIPAL >>>")
        print("                        ==============")
        print("")
        print("                 (1) ---> ORDENES DE TRABAJO")
        print("                 (2) ---> CLIENTES")
        print("                 (3) ---> VEHICULOS")
        print("                 (4) ---> STOCK")
        print("                 (5) ---> FACTURACION")
        print("                 (6) ---> SALIR")
        print("")
        print("..................................................................")

        opcion = int(input("Seleccione una opción: "))
        print(f'\033[{1}F', end='')

        if opcion == 1:
            os.system('cls')
            print("............Bienvenido al Sistema de Taller Mecanico..............")
            print("")
            print("                   <<< ORDENES DE TRABAJO >>>")
            print("                       ==================")
            print("")
            print("                 (1) ---> CREAR NUEVA ORDEN DE TRABAJO")
            print("                 (2) ---> CONSULTAR ORDENES DE TRABAJO")
            print("                 (3) ---> ACTUALIZAR ESTADO DE ORTDEN DE TRABAJO")
            print("                 (4) ---> VOLVER AL MENU ANTERIOR")
            print("")
            print("..................................................................")
            
            op = int(input("Seleccione una opción: "))
                        
            if op == 1:
                ot.crear()
            elif op == 2:
                ot.consultar()
            elif op == 3:
                ot.actualizar_estado()
            elif op == 4:
                pass
       
        elif opcion == 2:
            os.system('cls')
            print("............Bienvenido al Sistema de Taller Mecanico..............")
            print("")
            print("                        <<< CLIENTES >>>")
            print("                            ========")
            print("")
            print("                 (1) ---> AGREGAR NUEVO CLIENTE")
            print("                 (2) ---> ACTUALIZAR INFORMACION DEL CLIENTE")
            print("                 (3) ---> CONSULTAR INFORMACION DEL CLIENTE")
            print("                 (4) ---> ELIMINAR CLIENTE BASE DE DATOS")
            print("                 (5) ---> VOLVER AL MENU ANTERIOR")
            print("")
            print("..................................................................")
            
            op = int(input("Seleccione una opción: "))
            
            if op == 1:
                clientes.agregar()
            elif op == 2:
                clientes.actualizar()
            elif op == 3:
                clientes.consultar()
            elif op == 4:
                clientes.eliminar()
            elif op == 5:
                pass
            
        elif opcion == 3:
            os.system('cls')
            print("............Bienvenido al Sistema de Taller Mecanico..............")
            print("")
            print("                         <<< VEHICULOS >>>")
            print("                             =========")
            print("")
            print("                 (1) ---> AGREGAR NUEVO VEHICULO")
            print("                 (2) ---> ACTUALIZAR INFORMACION DEL VEHICULO")
            print("                 (3) ---> CONSULTAR INFORMACION DEL VEHICULO")
            print("                 (4) ---> ELIMINAR VEHICULO DE LA BASE DE DATOS")
            print("                 (5) ---> VOLVER AL MENU ANTERIOR")
            print("")
            print("..................................................................")
            
            op = int(input("Seleccione una opción: "))
            
            if op == 1:
                vehiculos.agregar()
            elif op == 2:
                vehiculos.actualizar()
            elif op == 3:
                vehiculos.consultar()
            elif op == 4:
                vehiculos.eliminar()
            elif op == 5:
                pass
            
        elif opcion == 4:
            os.system('cls')
            print("............Bienvenido al Sistema de Taller Mecanico..............")
            print("")
            print("                         <<< STOCK >>>")
            print("                             =====")
            print("")
            print("                 (1) ---> AGREGAR REPUESTO AL INVENTARIO")
            print("                 (2) ---> ACTUALIZAR INFORMACION REPUESTO")
            print("                 (3) ---> CONSULTAR DISPONIBILIDAD DE REPUESTO")
            print("                 (4) ---> ELIMINAR REPUESTO DEL INVENTARIO")
            print("                 (5) ---> VOLVER AL MENU ANTERIOR")
            print("")
            print("..................................................................")
            
            op = int(input("Seleccione una opción: "))
            
            if op == 1:
                stock.agregar()
            elif op == 2:
                stock.actualizar()
            elif op == 3:
                stock.consultar()
            elif op == 4:
                stock.eliminar()
            elif op == 5:
                pass
            
        elif opcion == 5:
            pass
        
        elif opcion == 6:
            print("Saliendo del sistema....")
            # sql.cerrar_bd() cerrar base de datos
            break
        else:
            print("Opción no válida. Por favor, presione una tecla para continuar.", end='')
            msvcrt.getch()

if __name__ == "__main__":
    mostrar_menu()
