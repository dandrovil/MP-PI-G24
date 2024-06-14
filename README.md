Modulo Programacion - Proyecto Integrador - Grupo 24

Miembros:

            Nombre: Daniel
            Apellido: Villalba
            DNI: 26.368.675
            Email: dandrovil.dv@gmail.com
            Github: https://github.com/dandrovil

            Nombre: Nahir
            Apellido: Zucaria
            DNI: 40.739.637
            Email: nahirzucaria@gmail.com
            Github: https://github.com/NZucaria

            Nombre: Adriel
            Apellido: Delosanto
            DNI: 36.876.897
            Email: adridelosanto@gmail.com
            Github: https://github.com/adriel1364

            Nombre: Dalmiro
            Apellido: Vilca
            DNI: 40.403.978
            Email: dalmirovilca@gmail.com
            Github: https://github.com/dalmiro

            Nombre: Eglimar
            Apellido: Ramirez
            DNI: 96.062.692
            Email: eglimarmramirez@gmail.com
            Github: https://github.com/EglimarRamirez


# **Propuesta: Desarrollo de un Sistema Para un Taller Mecanico.**



# **DESCRIPCIÓN GENERAL DEL PROYECTO**


## **Sistema de Gestión Para un taller Mecánico**


El sistema de gestión que se desarrolla, es una solución integral para optimizar la operación diaria de un taller mecánico, facilitando la administración de clientes, vehículos, órdenes de trabajo, inventarios y facturación. Este sistema tiene como objetivo mejorar la eficiencia operativa, reducir errores administrativos y proporcionar una mejor experiencia tanto para los empleados del taller como para los clientes.



**Funcionalidades Claves**


--Registro de Clientes y Vehículos: Permite agregar, modificar y eliminar clientes y sus vehículos.

--Gestión de Órdenes de Trabajo: Crea, visualiza y actualiza órdenes de trabajo. Cambia el estado de las órdenes cuando se completan.

--Generación de Facturas: Crea y visualiza facturas para los servicios prestados a los clientes.

--Control de stock: Permite tener un seguimiento e inventario del stock de respuestos notificando asi a los mecanicos cuando el stock ya es 0 del respuesto especifico 




**Beneficios del Sistema**


--Eficiencia Operativa: Reduce el tiempo y los errores asociados con la gestión manual de información.

--Mejor Servicio al Cliente: Proporciona información precisa y rápida a los clientes sobre sus vehículos y trabajos realizados.

--Transparencia y Trazabilidad: Facilita el seguimiento de las órdenes de trabajo y las responsabilidades de cada mecánico.  

--Automatización de Facturación: Asegura la generación precisa y rápida de facturas, mejorando el flujo de caja del taller.

--Control permantente de stock: Asegura contar con respuestos necesarios y llevar un inventario de los mismos para brindar el servicio en un tiempo acorde y eficiente.
  

## **Carpeta aplicacion** ##

**Modulo Mecanico.py** 
Función agregar():Función para crear un nuevo mecanico en la base de datos.
Funcion actualizar(): Funcion para actualizar datos de un mecanico en la base de datos.
Funcion busquedaMecanico(): Funcion para buscar un mecanico por codigo de mecanico en la base.
Funcion mostrar mecanicos(): Funcion para mostrar todos los mecanicos en la base de datos.
Funcion buscarMecanico(): Busca un mecanico por codigo de mecanico en la base de datos. Funcion usada
anteriormente.

**Modulo Presupuesto.py**
Funcion agregar(): Agrega un nuevo presupuesto a la base de datos.
Funcion actualizar(): Actualiza los datos de un presupuesto existente en la base de datos.
Funcion eliminar(): Elimina un presupuesto de la base de datos.
Funcion busquedaPresupuesto(): Busca un presupuesto por su codigo en la base de datos.
Funcion mostrar presupuestos(): Muestra todos los presupuestos almacenados en la base de datos.
Funcion buscarPresupuesto(): Busca un presupuesto por su codigo en la base de datos.

**Modulo Proveedor.py**
Funcion agregar():Agrega un nuevo proveedor a la base de datos.
Funcion actualizar(): Actualiza los datos de un proveedor existente en la base de datos.
Funcion eliminar(): Elimina un proveedor de la base de datos.
Funcion busquedaProveedor(): Muestra todos los proveedores almacenados en la base de datos.
Funcion mostrar proveedores():Muestra todos los proveedores almacenados en la base de datos.
Funcion buscarProveedor(): Busca un proveedor por su codigo en la base de datos.

**Modulo Stock.py**
Funcion agregar():Agrega nuevos ´ıtems al inventario.
Funcion actualizar(): Actualiza los datos de un ıtem existente en el inventario.
Funcion eliminar(): Elimina un ´ıtem del inventario.
Funcion busquedaPrecio(): Busca un ´ıtem por su precio en el inventario.
Funcion mostrar stock():Muestra todos los ıtems almacenados en el inventario.
Funcion buscarPrecio(): Se usa en otras funciones. Busca un ´ıtem en el inventario por su precio.
Funcion buscarItem(): Se usa en otras funciones. Busca un item en el inventario por su codigo de repuesto.

**Modulo Cliente.py**
Funcion agregar(): Agrega un nuevo cliente a la base de datos.
Funcion actualizar(): Actualiza los datos de un cliente existente en la base de datos.
Funcion eliminar(): Elimina un cliente de la base de datos.
Funcion buscarCliente(): Busca un cliente por su CUIT en la base de datos.



# Mapa de la Aplicacion


[![5649876513.png](https://i.postimg.cc/j2TYLyDJ/5649876513.png)](https://postimg.cc/47WS07bJ)




Main: Se encarga de las presentacion de los diferentes menu de opciones del programa.

Sql: Maneja el control a la base de datos, como conexion, consulta y desconexion.

Clientes: Almacena la información de los clientes, como nombre, dirección y número de contacto.

Vehículos: Registra los vehículos asociados a los clientes, incluyendo detalles como la marca, modelo, año y placa del vehículo.

Órdenes de Trabajo: Contiene detalles de las reparaciones solicitadas para cada vehículo, como el número de orden, estado de la reparación.

Inventario: Registra el inventario de repuestos disponibles en el taller, incluyendo detalles como el nombre del repuesto, cantidad en stock y precio unitario.

Facturas: Almacena detalles de las facturas generadas para los servicios realizados, incluyendo información de la orden de trabajo asociada, repuestos utilizados y el costo total de la factura.
