import os
import msvcrt
import ot, clientes, vehiculos, stock, mecanicos, presupuestos
import sql

if os.name == 'nt':
    screen = 'cls'
else:
    screen = 'clear'

#La funcion mostrar_menu() muestra el menu principal del programa.
def mostrar_menu():
    while True:
        os.system(screen)
        print("............Bienvenido al Sistema de Taller Mecanico..............")
        print("")
        print("                    <<< MENU PRINCIPAL >>>")
        print("                        ==============")
        print("")
        print("                 (1) ---> ORDENES DE TRABAJO")
        print("                 (2) ---> CLIENTES")
        print("                 (3) ---> VEHICULOS")
        print("                 (4) ---> MECANICOS")
        print("                 (5) ---> STOCK")
        print("                 (6) ---> PRESUPUESTOS")
        print("                 (7) ---> SALIR")
        print("")
        print("..................................................................")

        opcion = int(input("Seleccione una opción: "))
        print(f'\033[{1}F', end='')

        if opcion == 1:
            op = 0
            while op != 5:
                os.system(screen)
                print("............Bienvenido al Sistema de Taller Mecanico..............")
                print("")
                print("                   <<< ORDENES DE TRABAJO >>>")
                print("                       ==================")
                print("")
                print("                 (1) ---> CREAR NUEVA ORDEN DE TRABAJO") 
                print("                 (2) ---> CONSULTAR ORDENES POR ESTADO")
                print("                 (3) ---> ACTUALIZAR DE ORDENES DE TRABAJO")
                print("                 (4) ---> MOSTRAR TODAS LAS ORDENES")
                print("                 (5) ---> VOLVER AL MENU ANTERIOR")
                print("")
                print("..................................................................")
            
                op = int(input("Seleccione una opción: "))
                        
                if op == 1:
                    os.system(screen)
                    ot.agregar()
                    msvcrt.getch()
                
                elif op == 2:
                   os.system(screen)
                   print("(1) ---> Buscar por numero de orden")
                   print("(2) ---> Buscar por DNI/CUIT de cliente")
                   print("(3) ---> Buscar por patende del vehiculo")
                   print("(4) ---> Buscar por fecha de ingreso")
                   print("----------------------------------------")
                   o = int(input("Seleccione una opción: "))
                   if o == 1 or o == 2 or o == 3 or o == 4:
                         os.system(screen)
                         ot.buscar(o)
                   else:
                       print("\nOpción no válida - Operacion Candelada")
                   msvcrt.getch()
                        
                elif op == 3:
                     os.system(screen)
                     print("(1) ---> Modificar detalles del problema")
                     print("(2) ---> Asignar / Cambiar Mecanico")
                     print("(3) ---> Cerrar Orden de Trabajo")
                     print("(4) ---> Cambiar fecha de ingreso")
                     print("----------------------------------------")
                     op3 = int(input("Seleccione una opción: "))
                     if op3 == 1 or op3 == 2 or op3 == 3 or op3 == 4:
                         os.system(screen)
                         ot.asignar(op3)
                     else:
                         print("\nOpción no válida - Operacion Candelada")
                     msvcrt.getch()
                                                       
                elif op == 4:                
                    os.system(screen)
                    ot.mostrar()
                    msvcrt.getch()

                elif op == 5:
                    pass
       
        elif opcion == 2:
            op = 0
            while op != 6:
                os.system(screen)
                print("............Bienvenido al Sistema de Taller Mecanico..............")
                print("")
                print("                        <<< CLIENTES >>>")
                print("                            ========")
                print("")
                print("                 (1) ---> AGREGAR NUEVO CLIENTE")
                print("                 (2) ---> ACTUALIZAR INFORMACION DEL CLIENTE")
                print("                 (3) ---> CONSULTAR INFORMACION DEL CLIENTE")
                print("                 (4) ---> ELIMINAR CLIENTE")
                print("                 (5) ---> MOSTRAR CLIENTES")
                print("                 (6) ---> VOLVER AL MENU ANTERIOR")
                print("")
                print("..................................................................")
            
                op = int(input("Seleccione una opción: "))
            
                if op == 1:
                   os.system(screen)
                   clientes.agregar()
                   msvcrt.getch()
                
                elif op == 2:
                    os.system(screen)
                    clientes.actualizar()
                    msvcrt.getch()
               
                elif op == 3:
                    os.system(screen)
                    id = input("Ingrese DNI/CUIT del cliente: (solo numeros) ")
                    clientes.buscar(id)
                    msvcrt.getch()
                                    
                elif op == 4:
                    os.system(screen)
                    clientes.eliminar()
                    msvcrt.getch()
                
                elif op == 5:
                    os.system(screen)
                    clientes.mostrar()
                    msvcrt.getch()
                    
                elif op == 6:
                    pass
            
        elif opcion == 3:
            op = 0
            while op != 6:
                os.system(screen)
                print("............Bienvenido al Sistema de Taller Mecanico..............")
                print("")
                print("                         <<< VEHICULOS >>>")
                print("                             =========")
                print("")
                print("                 (1) ---> AGREGAR NUEVO VEHICULO")
                print("                 (2) ---> ACTUALIZAR INFORMACION DEL VEHICULO")
                print("                 (3) ---> CONSULTAR INFORMACION DEL VEHICULO")
                print("                 (4) ---> ELIMINAR VEHICULO")
                print("                 (5) ---> MOSTRAR VEHICULOS")
                print("                 (6) ---> VOLVER AL MENU ANTERIOR")
                print("")
                print("..................................................................") 
            
                op = int(input("Seleccione una opción: "))
            
                if op == 1:
                    os.system(screen)
                    vehiculos.agregar()
                    msvcrt.getch()
                
                elif op == 2:
                    os.system(screen)
                    vehiculos.actualizar()
                    msvcrt.getch()
                    pass
                
                elif op == 3:
                    os.system(screen)
                    print("(1) ---> Busqueda por patente")
                    print("(2) ---> Busqueda por CUIT/DNI")
                    print("------------------------------")
                    op2 = int(input("Seleccione una opción: "))
                    if op2 == 1:
                        os.system(screen)
                        id = input("Ingrese patente del vehhiculo: (solo numeros) ")
                        vehiculos.buscar_patente(id)
                    elif op2 == 2:
                        os.system(screen)
                        id = input("Ingrese DNI/CUIT del propietario: (solo numeros) ")
                        vehiculos.buscar_propietario(id)
                    else:
                        print("Opción no válida")
                    msvcrt.getch()
                                                       
                elif op == 4:
                    os.system(screen)
                    vehiculos.eliminar()
                    msvcrt.getch()
                                    
                elif op == 5:
                    os.system(screen)
                    vehiculos.mostrar()
                    msvcrt.getch()
            
                elif op == 6:
                    pass
                
        elif opcion == 4:
            op = 0
            while op != 6:
                os.system(screen)
                print("............Bienvenido al Sistema de Taller Mecanico..............")
                print("")
                print("                        <<< MECANICOS >>>")
                print("                            =========")
                print("")
                print("                 (1) ---> AGREGAR NUEVO MECANICO")
                print("                 (2) ---> ACTUALIZAR INFORMACION DEL MECANICO")
                print("                 (3) ---> CONSULTAR INFORMACION DEL MECANICO")
                print("                 (4) ---> ELIMINAR MECANICO")
                print("                 (5) ---> MOSTRAR MECANICOS")
                print("                 (6) ---> VOLVER AL MENU ANTERIOR")
                print("")
                print("..................................................................")
            
                op = int(input("Seleccione una opción: "))
            
                if op == 1:
                   os.system(screen)
                   mecanicos.agregar()
                   msvcrt.getch()
                
                elif op == 2:
                    os.system(screen)
                    mecanicos.actualizar()
                    msvcrt.getch()
               
                elif op == 3:
                    os.system(screen)
                    id = input("Ingrese codigo de mecanico: ")
                    mecanicos.buscar(id)
                    msvcrt.getch()
                                    
                elif op == 4:
                    os.system(screen)
                    mecanicos.eliminar()
                    msvcrt.getch()
                
                elif op == 5:
                    os.system(screen)
                    mecanicos.mostrar()
                    msvcrt.getch()
                    
                elif op == 6:
                    pass
                
        elif opcion == 5:
            op = 0
            while op != 6:
                os.system(screen)
                print("............Bienvenido al Sistema de Taller Mecanico..............")
                print("")
                print("                         <<< STOCK >>>")
                print("                             =====")
                print("")
                print("                 (1) ---> AGREGAR REPUESTO AL INVENTARIO")
                print("                 (2) ---> ACTUALIZAR INFORMACION REPUESTO")
                print("                 (3) ---> CONSULTAR DISPONIBILIDAD DE REPUESTO")
                print("                 (4) ---> ELIMINAR REPUESTO DEL INVENTARIO")
                print("                 (5) ---> MOSTRAR REPUESTOS")
                print("                 (6) ---> VOLVER AL MENU ANTERIOR")
                print("")
                print("..................................................................")
            
                op = int(input("Seleccione una opción: "))
            
                if op == 1:
                    os.system(screen)
                    stock.agregar()
                    msvcrt.getch()
                
                elif op == 2:
                    os.system(screen)
                    stock.actualizar()
                    msvcrt.getch()
                
                elif op == 3:
                    os.system(screen)
                    id = input("Ingrese codigo de repuesto: ")
                    stock.buscar(id)
                    msvcrt.getch()
                
                elif op == 4:
                    os.system(screen)
                    stock.eliminar()
                    msvcrt.getch()
                
                elif op == 5:
                    os.system(screen)
                    stock.mostrar()
                    msvcrt.getch()
                
                elif op == 6:
                    pass
            
        elif opcion == 6:
            op = 0
            while op != 7:
                os.system(screen)
                print("............Bienvenido al Sistema de Taller Mecanico..............")
                print("")
                print("                       <<< PRESUPUESTOS >>>")
                print("                           ============")
                print("")
                print("                 (1) ---> CREAR PRESUPUESTO")
                print("                 (2) ---> APROBAR/RECHAZAR PRESUPUESTO")
                print("                 (3) ---> MOSTRAR TODOS LOS PRESUPUESTOS")
                print("                 (4) ---> MOSTRAR PRESUPUESOS EN DETALLE")
                print("                 (5) ---> GENERAR FACTURA")
                print("                 (6) ---> BUSCAR UN POR NRO DE ORDEN")
                print("                 (7) ---> VOLVER AL MENU ANTERIOR")
                print("")
                print("..................................................................")
            
                op = int(input("Seleccione una opción: "))
            
                if op == 1:
                    os.system(screen)
                    presupuestos.agregar()
                    msvcrt.getch()
                
                elif op == 2:
                    os.system(screen)
                    presupuestos.oknok()
                    msvcrt.getch()
                                    
                elif op == 3:
                    os.system(screen)
                    presupuestos.mostrar()
                    msvcrt.getch()
                                   
                elif op == 4:
                    os.system(screen)
                    id = input("Ingrese Nro. de presupuesto a detallar: ")
                    presupuestos.detalle(id)
                    msvcrt.getch()
                                    
                elif op == 5:
                    os.system(screen)
                    presupuestos.generar()
                    msvcrt.getch()
                                    
                elif op == 6:
                    os.system(screen)
                    id = input("Ingrese Nro. de orden de repuesto: ")
                    presupuestos.buscar(id)
                    msvcrt.getch()
                
                elif op == 7:
                    pass
                    
        elif opcion == 7:
            print("Saliendo del sistema....")
            sql.cerrar_bd()
            break
        else:
            print("Opción no válida. Por favor, presione una tecla para continuar.", end='')
            msvcrt.getch()

if __name__ == "__main__":
    mostrar_menu()
