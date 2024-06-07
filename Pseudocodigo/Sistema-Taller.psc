// EPS del Programa "Taller Mecanico"
// ENTRADA: opcion, opcionSubMenu como entero
// El usuario selecciona una opción del menú principal
// El usuario selecciona opciones de submenús correspondientes a la funcionalidad elegida
// PROCESO: Dependiendo de la opción seleccionada, el sistema lleva a cabo diferentes procesos:
// Gestión de inventario: agregar, actualizar, consultar y eliminar repuestos
// Gestión de ordenes de trabajo: crear, actualizar y consultar órdenes de trabajo
// Gestión de clientes: agregar y actualizar información de clientes
// Facturación: procesar y generar facturas
// SALIDA: Mostrar el menú correspondiente.
// Mostrar resultados de las consultas (e.g., disponibilidad de repuestos)
// Mostrar confirmaciones de acciones realizadas (e.g., repuesto agregado)
// Generar y mostrar facturas al usuario
Algoritmo Menu
	Definir opcion, opcionSubMenu Como Entero
	Repetir
		Escribir '............Bienvenido al Sistema de Taller Mecanico..............'
		Escribir '------ MENU ------'
		Escribir '1. Gestion de Inventario y stock'
		Escribir '2. Gestion de Ordenes de Trabajo'
		Escribir '3. Gestion de Clientes'
		Escribir '4. Facturacion'
		Escribir '5. Salir'
		Escribir '-------------------'
		Escribir 'Seleccione una opcion que desea: '
		Leer opcion
		Según opcion Hacer
			1:
				Repetir
					Escribir '------ Gestion de Inventario ------'
					Escribir '1. Agregar Repuesto al Inventario'
					Escribir '2. Actualizar Informacion de Repuesto y del proveedor'
					Escribir '3. Consultar Disponibilidad de Repuesto'
					Escribir '4. Eliminar Repuesto del Inventario'
					Escribir '5. Volver al Menu Principal'
					Escribir '-------------------------'
					Escribir 'Seleccione una opcion: '
					Leer opcionSubMenu
					Según opcionSubMenu Hacer
						1:
							Escribir 'Opcion no implementada aun'
						2:
							Escribir 'Opcion no implementada aun'
						3:
							Escribir 'Opcion no implementada aun'
						4:
							Escribir 'Opcion no implementada aun'
						5:
							Escribir 'Volviendo al Menu Principal...'
						De Otro Modo:
							Escribir 'Opcion no valida. Por favor, seleccione una opcion del menu'
					FinSegún
				Hasta Que opcionSubMenu=5
			2:
				Repetir
					Escribir '------ Gestion de Ordenes de Trabajo ------'
					Escribir '1. Crear Nueva Orden de Trabajo'
					Escribir '2. Consultar ordenes de Trabajo'
					Escribir '3. Actualizar Estado de Orden de Trabajo'
					Escribir '4. Eliminar Orden de Trabajo'
					Escribir '5. Volver al Menu Principal'
					Escribir '-------------------------'
					Escribir 'Seleccione una opcion: '
					Leer opcionSubMenu
					Según opcionSubMenu Hacer
						1:
							Escribir 'Opcion no implementada aun'
						2:
							Escribir 'Opcion no implementada aun'
						3:
							Escribir 'Opcion no implementada aun'
						4:
							Escribir 'Opcion no implementada aun'
						5:
							Escribir 'Volviendo al Menu Principal...'
						De Otro Modo:
							Escribir 'Opcion no valida. Por favor, seleccione una opcion del menu'
					FinSegún
				Hasta Que opcionSubMenu=5
			3:
				Repetir
					Escribir '------ Gestion de Clientes ------'
					Escribir '1. Agregar Nuevo Cliente'
					Escribir '2. Actualizar Informacion de Cliente'
					Escribir '3. Consultar Informacion de Cliente'
					Escribir '4. Volver al Menu Principal'
					Escribir '-------------------------'
					Escribir 'Seleccione una opcion: '
					Leer opcionSubMenu
					Según opcionSubMenu Hacer
						1:
							Escribir 'Opcion no implementada aun'
						2:
							Escribir 'Opcion no implementada aun'
						3:
							Escribir 'Opcion no implementada aun'
						4:
							Escribir 'Volviendo al Menu Principal...'
						De Otro Modo:
							Escribir 'Opcion no valida. Por favor, seleccione una opcion del menu'
					FinSegún
				Hasta Que opcionSubMenu=4
			4:
				Escribir 'Opcion no implementada aun'
			5:
				Escribir '¡Hasta luego!'
			De Otro Modo:
				Escribir 'Opcion no valida. Por favor, seleccione una opcion del menu.'
		FinSegún
	Hasta Que opcion=5
FinAlgoritmo
