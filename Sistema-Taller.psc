Algoritmo Menu
		
		Definir opcion, opcionSubMenu Como Entero
		
		Repetir
			Escribir "Bienvenido al Sistema de Taller Mecánico"
			Escribir "------ MENÚ ------"
			Escribir "1. Gestion de Inventario"
			Escribir "2. Gestion de Ordenes de Trabajo"
			Escribir "3. Gestion de Clientes"			
			Escribir "4. Facturacion"
			Escribir "5. Salir"
			Escribir "-------------------"
			Escribir "Seleccione una opción: "
			Leer opcion
			
			Segun opcion Hacer
				1:
					Repetir
						Escribir "------ Gestion de Inventario ------"
						Escribir "1. Agregar Repuesto al Inventario"
						Escribir "2. Actualizar Informacion de Repuesto"
						Escribir "3. Consultar Disponibilidad de Repuesto"
						Escribir "4. Eliminar Repuesto del Inventario"
						Escribir "5. Volver al Menú Principal"
						Escribir "-------------------------"
						Escribir "Seleccione una opción: "
						Leer opcionSubMenu
						Segun opcionSubMenu Hacer
							1:
								Escribir "Opcion no implementada aun"
							2:
								Escribir "Opcion no implementada aun"
							3:
								Escribir "Opcion no implementada aun"
							4:
								Escribir "Opcion no implementada aun"
							5:	
								Escribir "Volviendo al Menú Principal..."
							De Otro Modo:
								Escribir "Opción no válida. Por favor, seleccione una opción del menú"
						Fin Segun
					Hasta Que opcionSubMenu = 5
										
				2:
					Repetir
						Escribir "------ Gestion de Ordenes de Trabajo ------"
						Escribir "1. Crear Nueva Orden de Trabajo"
						Escribir "2. Consultar Órdenes de Trabajo"
						Escribir "3. Actualizar Estado de Orden de Trabajo"
						Escribir "4. Eliminar Orden de Trabajo"
						Escribir "5. Volver al Menú Principal"
						Escribir "-------------------------"
						Escribir "Seleccione una opción: "
						Leer opcionSubMenu
						Segun opcionSubMenu Hacer
							1:
								Escribir "Opcion no implementada aun"
							2:
								Escribir "Opcion no implementada aun"
							3:
								Escribir "Opcion no implementada aun"
							4:
								Escribir "Opcion no implementada aun"
							5:	
								Escribir "Volviendo al Menú Principal..."
							De Otro Modo:
								Escribir "Opción no válida. Por favor, seleccione una opción del menú"
						Fin Segun
					Hasta Que opcionSubMenu = 5
					
				3:
					Repetir
						Escribir "------ Gestion de Clientes ------"
						Escribir "1. Agregar Nuevo Cliente"
						Escribir "2. Actualizar Información de Cliente"
						Escribir "3. Consultar Información de Cliente"
						Escribir "4. Volver al Menú Principal"
						Escribir "-------------------------"
						Escribir "Seleccione una opción: "
						Leer opcionSubMenu
						Segun opcionSubMenu Hacer
							1:
								Escribir "Opcion no implementada aun"
							2:
								Escribir "Opcion no implementada aun"
							3:
								Escribir "Opcion no implementada aun"
							4:
								Escribir "Volviendo al Menú Principal..."
							De Otro Modo:
								Escribir "Opción no válida. Por favor, seleccione una opción del menú"
						Fin Segun
					Hasta Que opcionSubMenu = 4
					
				4:
					Escribir "Opcion no implementada aun"
				5:
					Escribir "¡Hasta luego!"
								
				De Otro Modo:
					Escribir "Opción no válida. Por favor, seleccione una opción del menú."
			Fin Segun
Hasta Que opcion = 5
FinAlgoritmo
