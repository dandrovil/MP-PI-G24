import os
import msvcrt
import ot, clientes, vehiculos, stock, mecanicos, presupuestos
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
                os.system('cls')
                print("............Bienvenido al Sistema de Taller Mecanico..............")
                print("")
                print("                   <<< ORDENES DE TRABAJO >>>")
                print("                       ==================")
                print("")
                print("                 (1) ---> CREAR NUEVA ORDEN DE TRABAJO") 
                print("                 (2) ---> CONSULTAR ORDENES POR ESTADO")
                print("                 (3) ---> ASIGNAR DE ORTDEN DE TRABAJO A MECANICO")
                print("                 (4) ---> MOSTRAR ORDENES")
                print("                 (5) ---> VOLVER AL MENU ANTERIOR")
                print("")
                print("..................................................................")
            
                op = int(input("Seleccione una opción: "))
                        
                if op == 1:
                    ot.crear()
                    msvcrt.getch()
                
                elif op == 2:
                    o = 1
                    while o != 0:
                        os.system('cls')
                        print("............Bienvenido al Sistema de Taller Mecanico..............")
                        print("")
                        print("                       <<< ESTADOS >>>")
                        print("                       ===============")
                        print("")
                        print("                 (1) ---> INGRESADO") 
                        print("                 (2) ---> ASIGNADO")
                        print("                 (3) ---> PRESUPUESTADO")
                        print("                 (4) ---> APROBADO")
                        print("                 (5) ---> RECHAZADO")
                        print("                 (6) ---> REPARADO")
                        print("                 (0) ---> SALIR DE LA CONSULTA")
                        print("")
                        print("..................................................................")
            
                        o = int(input("Seleccione una opción: "))
                        
                        if o == 1:
                            ot.consultar("ingresado")
                            msvcrt.getch()
                        elif o == 2:
                            ot.consultar("asignado")
                            msvcrt.getch()
                        elif o == 3:
                            ot.consultar("presupuestado")
                            msvcrt.getch()
                        elif o == 4:
                            ot.consultar("aprobado")
                            msvcrt.getch()
                        elif o == 5:
                            ot.consultar("rechazado")
                            msvcrt.getch()
                        elif o == 6:
                            ot.consultar("reparado")
                            msvcrt.getch()
                                           
                elif op == 3:
                    ot.asignar()
                    msvcrt.getch()
                                   
                elif op == 4:                
                    ot.mostrar_ordenes()
                    msvcrt.getch()

                elif op == 5:
                    pass
       
        elif opcion == 2:
            op = 0
            while op != 6:
                os.system('cls')
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
                   clientes.agregar()
                   msvcrt.getch()
                
                elif op == 2:
                   clientes.actualizar()
                   msvcrt.getch()
               
                elif op == 3:
                    id = input("Ingrese DNI/CUIT del cliente: (sin guiones) ")
                    clientes.buscar(id)
                    msvcrt.getch()
                                    
                elif op == 4:
                    clientes.eliminar()
                    msvcrt.getch()
                
                elif op == 5:
                    clientes.mostrar()
                    msvcrt.getch()
                    
                elif op == 6:
                    pass
            
        elif opcion == 3:
            op = 0
            while op != 6:
                os.system('cls')
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
                    vehiculos.agregar()
                    msvcrt.getch()
                
                elif op == 2:
                    vehiculos.actualizar()
                    msvcrt.getch()
                    pass
                
                elif op == 3:
                    id = input("Ingrese patente del vehiculo: (sin guiones) ")
                    vehiculos.buscar(id)
                    msvcrt.getch()
                                    
                elif op == 4:
                    vehiculos.eliminar()
                    msvcrt.getch()
                                    
                elif op == 5:
                    vehiculos.mostrar()
                    msvcrt.getch()
            
                elif op == 6:
                    pass
                
        elif opcion == 4:
            op = 0
            while op != 6:
                os.system('cls')
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
                   mecanicos.agregar()
                   msvcrt.getch()
                
                elif op == 2:
                   mecanicos.actualizar()
                   msvcrt.getch()
               
                elif op == 3:
                    id = input("Ingrese codigo de mecanico: ")
                    mecanicos.buscar(id)
                    msvcrt.getch()
                                    
                elif op == 4:
                    mecanicos.eliminar()
                    msvcrt.getch()
                
                elif op == 5:
                    mecanicos.mostrar()
                    msvcrt.getch()
                    
                elif op == 6:
                    pass
                
        elif opcion == 5:
            op = 0
            while op != 6:
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
                print("                 (5) ---> MOSTRAR REPUESTOS")
                print("                 (6) ---> VOLVER AL MENU ANTERIOR")
                print("")
                print("..................................................................")
            
                op = int(input("Seleccione una opción: "))
            
                if op == 1:
                    stock.agregar()
                    msvcrt.getch()
                
                elif op == 2:
                    stock.actualizar()
                    msvcrt.getch()
                
                elif op == 3:
                    id = input("Ingrese codigo de repuesto: ")
                    stock.buscar(id)
                    msvcrt.getch()
                
                elif op == 4:
                    stock.eliminar()
                    msvcrt.getch()
                
                elif op == 5:
                    stock.mostrar()
                    msvcrt.getch()
                
                elif op == 6:
                    pass
            
        elif opcion == 6:
            op = 0
            while op != 6:
                os.system('cls')
                print("............Bienvenido al Sistema de Taller Mecanico..............")
                print("")
                print("                       <<< PRESUPUESTOS >>>")
                print("                           ============")
                print("")
                print("                 (1) ---> CREAR PRESUPUESTO")
                print("                 (2) ---> APROBAR/RECHAZAR PRESUPUESTO")
                print("                 (3) ---> BUSCAR PRESUPUESTOS POR NRO. DE ORDEN")
                print("                 (4) ---> MOSTRAR TODOS LOS PRESUPUESTOS")
                print("                 (5) ---> MOSTRAR PRESUPUESOS EN DETALLE")
                print("                 (6) ---> VOLVER AL MENU ANTERIOR")
                print("")
                print("..................................................................")
            
                op = int(input("Seleccione una opción: "))
            
                if op == 1:
                    presupuestos.crear()
                    msvcrt.getch()
                
                elif op == 2:
                    presupuestos.oknok()
                    msvcrt.getch()
                                    
                elif op == 3:
                    id = input("Ingrese Nro. de orden a buscar: ")
                    presupuestos.buscar(id)
                    msvcrt.getch()
                    pass
                
                elif op == 4:
                    presupuestos.mostrar()
                    msvcrt.getch()
                                    
                elif op == 5:
                    id = input("Ingrese Nro. de presupuesto a detallar: ")
                    presupuestos.detalle(id)
                    msvcrt.getch()
                                    
                elif op == 6:
                    pass
            pass
        
        elif opcion == 7:
            print("Saliendo del sistema....")
            # sql.cerrar_bd() cerrar base de datos
            break
        else:
            print("Opción no válida. Por favor, presione una tecla para continuar.", end='')
            msvcrt.getch()

if __name__ == "__main__":
    mostrar_menu()
