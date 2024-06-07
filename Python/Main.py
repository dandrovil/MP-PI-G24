import os
import msvcrt

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
           pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            print("Saliendo del sistema....")
            break
        else:
            print("Opción no válida. Por favor, presione una tecla para continuar.", end='')
            msvcrt.getch()

if __name__ == "__main__":
    mostrar_menu()
