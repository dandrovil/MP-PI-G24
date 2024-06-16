# **Modulo Programacion - Proyecto Integrador - Grupo 24** - **Propuesta: Desarrollo de un Sistema de Gestion Para un Taller Mecanico.**

## Miembros:

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


## **Descripcion general del proyecto y aplicacion**

El proyecto se realiza integrando los temas abordados en el "módulo de programador" del primer semestre del ISPC. Este abarca las materias Ética y Deontología Profesional, Base de Datos e Introducción a la Programación.  
Se trata de un sistema de gestión que desarrolla una solución integral para optimizar la operación diaria de un taller mecánico, facilitando la administración de clientes, vehículos, órdenes de trabajo, inventarios y facturación.  
Este sistema tiene como objetivo mejorar la eficiencia operativa, reducir errores administrativos y proporcionar una mejor experiencia tanto para los empleados del taller como para los clientes. Mientras qué a nivel académico busca plasmar los conocimientos adquiridos en las distintas materias durante el cursado del espacio curricular.


## **Funcionalidades Claves**

- Registro de Clientes y Vehículos: Permite agregar, modificar y eliminar clientes y sus vehículos.
- Gestión de Órdenes de Trabajo: Crea, visualiza y actualiza órdenes de trabajo. Cambia el estado de las órdenes cuando se completan.
- Generación de Facturas: Crea y visualiza facturas para los servicios prestados a los clientes.
- Control de stock: Permite tener un seguimiento e inventario del stock de respuestos.

## **Beneficios del Sistema**

- Eficiencia Operativa: Reduce el tiempo y los errores asociados con la gestión manual de información.
- Mejor Servicio al Cliente: Proporciona información precisa y rápida a los clientes sobre sus vehículos y trabajos realizados.
- Transparencia y Trazabilidad: Facilita el seguimiento de las órdenes de trabajo y las responsabilidades de cada mecánico.  
- Automatización de Facturación: Asegura la generación precisa y rápida de facturas, mejorando el flujo de caja del taller.
- Control permantente de stock: Asegura contar con respuestos necesarios y llevar un inventario de los mismos para brindar el servicio en un tiempo acorde y eficiente.


## Mapa de la Aplicacion
[![5649876513.png](https://i.postimg.cc/j2TYLyDJ/5649876513.png)](https://postimg.cc/47WS07bJ)

## **Contenido del repositorio**

### **Carpeta Aplicacion**

- **Main_V2.py:** Es el archivo qué contiene el código del menú principal del programa, desde el cuál se accede mediante input del usuario a las diferentes funciones (CRUD) de cada módulo.


- **mecanicos.py:** Archivo con el CRUD del módulo MECANICOS.
  - Función agregar():Función para crear un nuevo mecanico en la base de datos.
  - Función agregar():Función para crear un nuevo mecanico en la base de datos.
  - Funcion actualizar(): Funcion para actualizar datos de un mecanico en la base de datos.
  - Funcion buscar(): #Funcion para buscar un mecanico en la base de datos.
  - Funcion eliminar(): Funcion para eliminar un mecanico en la base de datos.
  - Funcion mostrar(): Funcion para mostrar todos los mecanicos en la base de datos.

- **presupuestos.py:** Archivo con el  CRUD del módulo presupuesto.
  - Funcion crear(): Agrega un nuevo presupuesto a la base de datos.
  - Funcion actualizar(): Actualiza los datos de un presupuesto existente en la base de datos.
  - Funcion buscar(): Funcion para buscar un presupuesto por "idorden" en la base de datos.
  - Funcion mostrar(): Muestra todos los presupuetos que existen en la base de datos.
  - Funcion consultar(): Buscar un presupuesto por "idpresupuesto".

- **stock.py:** Archivo con el  CRUD del módulo stock.
  - Funcion agregar():Agrega nuevos ´ıtems al inventario.
  - Funcion actualizar(): Actualiza los datos de un ıtem existente en el inventario.
  - Funcion eliminar(): Elimina un ´ıtem del inventario.
  - Funcion mostrar(): Muestra todos los ıtems almacenados en el inventario.
  - Funcion buscar(): Buscar item en el inventario por "idstock".

- **clientes.py:** Archivo con el CRUD del módulo clientes.
  - Funcion agregar(): Agrega un nuevo cliente a la base de datos.
  - Funcion actualizar(): Actualiza los datos de un cliente existente en la base de datos.
  - Funcion buscar(): Funcion para buscar un cliente en la base de datos.
  - Funcion eliminar(): Elimina un cliente de la base de datos.
  - Funcion mostrar(): Funcion para mostrar todos los clientes en la base de datos.

- **vehiculos.py:** Archivo con el  CRUD del modulo vehiculos.
  - Funcion agregar(): Agrega un nuevo vehiculo a la base de datos.
  - Funcion actualizar(): Actualiza los datos de un vehiculo existente en la base de datos.
  - Funcion buscar_patente(): Funcion para buscar un vehiculo por patente en la base de datos.
  - Funcion buscar_propietario(): Funcion para buscar un vehiculo por "id_Cliente" en la base de datos.
  - Funcion mostrar(): Funcion para mostrar todos los vehiculos en la base de datos.
  - Funcion consultar(): Funcion para consultar si existe un vehiculo en la base de datos.
  - Funcion eliminar(): Elimina un vehiculo de la base de datos.

- **ot.py:** Archivo con el CRUD del módulo ORDENES.
  - Funcion crear(): La función crear() permite registrar una nueva orden de trabajo para un vehículo específico en una base de datos solicitando la patente del vehículo y el motivo de la avería, y luego almacenando esta información junto con la fecha actual en la tabla ordenes.
  - Funcion consultar(): La función consultar(id) busca y muestra todas las órdenes de trabajo que tienen un estado específico (id) en la base de datos formateando y mostrando los detalles relevantes de cada orden si se encuentran.
  - Funcion asignar(): la función asignar() facilita la asignación de una orden de trabajo a un mecánico específico en la base de datos verificando la existencia de la orden y del mecánico antes de realizar la asignación.
  - Funcion mostrar_ordenes(): La función mostrar_ordenes() realiza una consulta a la base de datos para recuperar todas las órdenes almacenadas y las muestra en la consola. Si no hay órdenes disponibles, informa al usuario de esta situación.
  - Funcion buscar(): la función buscar(id) permite verificar la existencia de una orden específica en la base de datos a través de su idOrden devolviendo True si la orden existe y False si no existe.
  - Funcion update(): La función update(id, status) permite modificar el estado de una orden específica en la base de datos.

- **sql:** Archivo qué contiene el código necesario para establecer la conexión, desconexion y realizar consultas con la base de datos.

### **Carpeta BD**
- **CROWFOOT.jpeg:** Archivo en formato jpeg con el diagrama de la base de datos en notación Crowfoot.
- **Notacion de CHEN.jpeg:** Archivo en formato jpeg con el diagrama de la base de datos en notación de CHEN.
- **taller.mwb:** Archivo en formato mwb con el Crowfoot de la base de datos.
- **taller.sql:** Archivo en formato sql qué contiene el script para crear las tablas y sus respectivos datos en la base de datos.

### **Carpeta Pseudocodigo**
- **Diagrama de flujo.png:** Archivo en formato png qué contiene el diagrama de flujo de la aplicación.
- **EPS.txt:** Un archivo en formato txt qué contiene el análisis EPS (Entrada, Proceso, Salida) del programa.
- **Sistema-Taller.psc:** Archivo en formato psc qué contiene el pseudocódigo del menú principal del programa.

### **Otros archivos**
- **.gitignore:** Archivo de configuración en el cuál se especifica qué archivos se van a ignorar al hacer un push. Por ej. dependencias,  archivos de configuración de VSC, etc.
- **Análisis.txt:** Archivo en formato txt qué contiene el análisis  de funcionamiento del programa.
- **README.md**: Archivo en formato markdown qué contiene principalmente  información sobre el contenido del repositorio, el funcionamiento general del programa y cómo utilizarlo.
- **Video:** Video explicativo del uso de la aplicacion, con casos de uso y ejemplos.

## **Cómo usar la aplicación**

En el menú principal del programa se mostrarán opciones para interactuar con las diferentes funcionalidades de cada módulo.  
Al elegir alguno de estos módulos se darán las opciones de crear, eliminar, actualizar o mostrar instancias de una entidad, según el módulo qué se seleccione.  
Una vez seleccionado un módulo se deberá elegir a continuación qué acción se desea realizar ( crear, eliminar, actualizar o mostrar) y luego se deberá ingresar los datos solicitados por el programa.
El resultado se mostrará en terminal de acuerdo a las opciones elegidas.
NOTA: Revisar el archivo **Video** del repositorio para informacion adicional.

## **Requisitos de la aplicación**

Para utilizar el programa se deberá instalar lo siguiente:  
- SQL y MySQL Workbench- Se recomienda desde la web [MySQL Installer](https://dev.mysql.com/downloads/installer/ "MySQL Installer")
- SQL Connector - Desde la terminal usar el comando pip install mysqlx-connector-python.
- Pandas - Desde la terminal usar el comando pip install pandas.
- Tabulate - Desde la terminal usar el comando pip install tabulate.
