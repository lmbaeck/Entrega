Proyecto Integrador Final
Curso Introducción a Python 2024
Este proyecto consiste en una aplicación de gestión de inventarios diseñada para registrar, consultar, actualizar y eliminar productos en una base de datos SQLite. Es una solución ligera y eficiente para pequeños negocios o proyectos personales.
El proyecto consta de crear 3 programas en Python que gestionan el inventario mediante una base de datos SQlite

Archivos principales:
- `programa_principal.py`: Controla el flujo principal de la aplicación y muestra el menú principal.
- `menu_funciones.py`: Contiene funciones auxiliares para mostrar menúes y solicitar datos al usuario.
- `funciones_db.py`: Gestiona las operaciones con la base de datos SQLite, como insertar, actualizar, eliminar, reporte de bajo stock, mostrar y buscar productos por codigo y consultar productos.

Descripción para cada programa
Archivo: menu_principal.py
Propósito:
Controla la ejecución principal del programa, presentando un menú al usuario y manejando las opciones seleccionadas. Desde este archivo se llaman las funciones de los módulos auxiliares para realizar las operaciones necesarias.

Características principales:

Muestra un menú interactivo con opciones como registrar productos, consultar productos con bajo stock, y eliminar productos.
Llama a funciones específicas para realizar acciones sobre la base de datos.
Flujo principal:

- Crea la base de datos si no existe (crear_tabla_productos).
- Muestra el menú al usuario con opciones claras.
- Maneja cada opción llamando a funciones como:
 	insertar_producto, 
	mostrar_productos, 
	eliminar_producto,
	buscar_producto por codigo,
	reporte de productos con bajo stock,
- 	actualizar productos,
	salir

Archivo: menu_funciones.py

Propósito:
- Proporciona funciones auxiliares para la interacción con el usuario, como mostrar menús y solicitar datos de manera estructurada.

Funciones principales:

- menu_mostrar_opciones(): Presenta el menú principal y devuelve la opción seleccionada.
- solicitar_datos_producto(): Solicita al usuario los datos necesarios para registrar un producto.
- solicitar_stock_minimo(): Solicita un valor para filtrar productos con bajo stock.

Archivo: funciones_db.py
Propósito:
Gestiona todas las operaciones relacionadas con la base de datos SQLite, incluyendo la creación de tablas, inserción de datos, actualizaciones y consultas.

Funciones principales:

- crear_tabla_productos(): Crea la tabla de productos en la base de datos si no existe.
- insertar_producto(): Inserta un nuevo producto en la base de datos.
- mostrar_productos(): Lista todos los productos registrados.
- actualizar_producto(codigo): Actualiza campos específicos de un producto según su código.
- eliminar_producto(): Elimina un producto de la base de datos según su código.
- reporte_bajo_stock(stock_minimo): Genera un listado de productos cuyo stock está por debajo de un nivel mínimo.

Estas funciones reciben un parametro que corresponde a la ruta de la base de datos
"inventario.db"

Se usaron las estructuras Try-Execept para manejar los errores de base de datos y los errores propios de la ejecución del programa, 
tales como los ingresos erroneos del usuario.

Los Archivos subidos a GitHub de este trabajo final son:
- Este archivo README
- Este archivo "inventario.db"
- 3 Archivos de código fuente en python: 
	- programa_principal.py
	- menu_funciones.py
	- funciones_db.py

El Archivo "inventario.db" no es necesario para el ejecución del programa, ya que el programa está preparado para generarlo, 
solo basta ingresar a la opción 1 del menú "Agregar Producto" para que el archivo se genere en la ruta específica que se declare en la 
variable:
 rutaBaseDatos = "inventario.db" este archivo.db se crea en el mismo directorio donde se encuentra en archivo proyectoFinalDB.py 
También puede ser indicada la ruta completa por ejemplo:
ruta_db = inventario.db" 
Si bien el proyecto se encuentra en la carpeta C:\Curso Python\Entrega_Final, no coloco esta ruta dado que la ruta no siempre va a coincidir si se abre en otro equipo. Igualmente, el programa está preparado para crear la base de datos y la tabla productos de manera automática.

El programa fue desarrollado usando las herramientas del Curso Introducción a Python
se usaron :
            *Estructuras de control
            *Llamadas al usuario (función input())
            *uso de listas y diccionarios
            *uso de sqlite
            *librerias OS y Colorama
Ante dudas o bugs enviar un e-mail a: 
lmbaeck@gmail.com

Este programa fue desarrollado mediante software libre



