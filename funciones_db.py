"""
Este programa es un sistema de gestión de inventario que utiliza una base de datos SQLite para almacenar información sobre productos. 
Permite realizar las siguientes operaciones:
- Crear una tabla para almacenar productos (si no existe).
- Insertar nuevos productos con atributos como nombre, descripción, cantidad, precio y categoría.
- Mostrar una lista de productos registrados en la base de datos.
- Actualizar campos específicos de productos existentes.
- Eliminar productos de la base de datos por su código.
- Buscar un producto por su código y mostrar sus detalles.
- Generar un reporte de productos con stock por debajo de un nivel mínimo especificado.
"""
# Este programa está diseñado para facilitar la gestión de inventarios de forma eficiente y confiable.

#Importa el módulo sqlite3, que es parte de la biblioteca estándar de Python. 
#Este módulo permite interactuar con bases de datos SQLite, un sistema de gestión de bases de datos ligero, integrado y sin servidor
import sqlite3 

ruta_db = "inventario.db"  # Ruta donde se encuentra la base de datos SQLite.

def conectar_db():
    """Conecta a la base de datos SQLite.
    Retorna un objeto de conexión.
    Si la base de datos no existe, la crea.
    """
    return sqlite3.connect(ruta_db)

def crear_tabla_productos():
    """
    Crea la tabla `productos` en la base de datos si no existe.
    La tabla incluye los campos:
    - `codigo`: Identificador único (autoincremental).
    - `nombre`: Nombre del producto (obligatorio).
    - `descripcion`: Breve descripción del producto.
    - `cantidad`: Stock disponible (obligatorio).
    - `precio`: Precio del producto (obligatorio).
    - `categoria`: Categoría del producto.
    """
    conexion = conectar_db()
    cursor = conexion.cursor()
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                categoria TEXT
            )
        ''')
        print("Tabla creada con éxito")
        conexion.commit()
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")
    finally:
        conexion.close()

def insertar_producto(nombre, descripcion, cantidad, precio, categoria):
    """
    Inserta un nuevo producto en la tabla `productos`.
    Recibe como parámetros:
    - `nombre`: Nombre del producto.
    - `descripcion`: Descripción del producto.
    - `cantidad`: Cantidad disponible en stock.
    - `precio`: Precio unitario.
    - `categoria`: Categoría del producto.
    """
    conexion = conectar_db()
    cursor = conexion.cursor()
    try:
        cursor.execute('''
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        print(f"Producto {nombre} ingresado correctamente")
    except sqlite3.Error as e:
        print(f"Error al registrar producto: {e}")
    finally:
        conexion.close()

def mostrar_productos():
    """
    Muestra todos los productos registrados en la tabla `productos`.
    Incluye detalles como código, nombre, descripción, cantidad, precio y categoría.
    """
    conexion = conectar_db()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT codigo, nombre, descripcion, cantidad, precio, categoria FROM productos")
        productos = cursor.fetchall()
        if productos:
            print(f"{'Cód.':<6}\t{'Nombre':<20}\t{'Descr.':<20}\t{'Cant.':<6}\t{'Precio':<6}\t{'Categoría':<20}")
            print("="*80)
            for codigo, nombre, descripcion, cantidad, precio, categoria in productos:
                print(f"{codigo:<6}\t{nombre:<20}\t{descripcion:<20}\t{cantidad:<6}\t{precio:<6}\t{categoria:<20}")
                print("-"*80)
        else:
            print("No hay productos registrados.")
    except sqlite3.Error as e:
        print(f"Error al mostrar productos: {e}")
    finally:
        conexion.close()

def actualizar_producto(codigo):
    """
    Actualiza un campo específico de un producto identificado por su código.
    - Muestra primero los productos disponibles.
    - Solicita el código del producto a actualizar.
    - Ofrece un menú para elegir el campo a modificar (nombre, descripción, cantidad, precio o categoría).
    - Actualiza el valor del campo seleccionado.
    """
    conexion = conectar_db()
    cursor = conexion.cursor()
    try:
        mostrar_productos()

        # Verificar si el producto existe
        cursor.execute("SELECT * FROM productos WHERE codigo = ?", (codigo,))
        producto = cursor.fetchone()
        if not producto:
            print("No se encontró un producto con ese código.")
            return

        # Menú de opciones de actualización
        print("\n¿Qué desea actualizar?")
        print("1. Nombre")
        print("2. Descripción")
        print("3. Cantidad")
        print("4. Precio")
        print("5. Categoría")
        opcion = int(input("Ingrese el número de la opción a actualizar: "))

        # Lista de campos correspondientes
        campos = ["nombre", "descripcion", "cantidad", "precio", "categoria"]
        if 1 <= opcion <= 5:
            nuevo_valor = input(f"Ingrese el nuevo valor para {campos[opcion - 1]}: ")

            # Convertir el valor según el tipo de campo (cantidad y precio)
            if campos[opcion - 1] == "cantidad":
                nuevo_valor = int(nuevo_valor)
            elif campos[opcion - 1] == "precio":
                nuevo_valor = float(nuevo_valor)

            # Actualizar en la base de datos
            cursor.execute(f'''
                UPDATE productos
                SET {campos[opcion - 1]} = ?
                WHERE codigo = ?
            ''', (nuevo_valor, codigo))
            conexion.commit()
            print("Producto {nombre} actualizado con éxito.")
        else:
            print("Opción no válida.")
    except sqlite3.Error as e: #Al producirse un error, se envía un mensaje
        print(f"Error al actualizar producto: {e}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")
    finally:
        conexion.close() # Cierra la conexión a la base de datos

def eliminar_producto():
    """
    Elimina un producto de la tabla `productos` basado en su código.
    Solicita al usuario ingresar el código del producto a eliminar.
    """
def eliminar_producto():
    #Elimina un producto de la base de datos basándose en su código.
    #Muestra el código y el nombre del producto eliminado.
    conexion = conectar_db()
    cursor = conexion.cursor()
    try:
        codigo = int(input("Ingrese el código del producto a eliminar: "))

        # Verificar si el producto existe y obtener su nombre
        cursor.execute("SELECT nombre FROM productos WHERE codigo = ?", (codigo,))
        producto = cursor.fetchone()
        if producto:
            nombre = producto[0]  # Obtener el nombre del producto
            # Eliminar el producto
            cursor.execute("DELETE FROM productos WHERE codigo = ?", (codigo,))
            conexion.commit()
            print(f"Producto eliminado: Codigo: {codigo}, Nombre: {nombre}")
        else:
            print("No se encontró un producto con ese código.")
    except ValueError:
        print("Por favor, ingrese un número válido para el código.")
    except sqlite3.Error as e:
        print(f"Error al eliminar producto: {e}")
    finally:
        conexion.close()
    
def mostrar_producto_por_codigo():
    """
    Busca y muestra un producto basado en su código.
    Retorna un diccionario con los detalles del producto si se encuentra, de lo contrario retorna None.
    """
    conexion = conectar_db()
    cursor = conexion.cursor()
    try:
        codigo = int(input("Ingrese el código del producto a buscar: "))
        cursor.execute("SELECT codigo, nombre, descripcion, cantidad, precio, categoria FROM productos WHERE codigo = ?", (codigo,))
        producto = cursor.fetchone()
        if producto:
            producto_dict = {
                "ID": producto[0],
                "Nombre": producto[1],
                "Descripción": producto[2],
                "Cantidad": producto[3],
                "Precio": producto[4],
                "Categoría": producto[5]
            }
            return producto_dict
        else:
            print("No se encontró un producto con ese código.")
            return None
    except ValueError:
        print("Por favor, ingrese un número válido para el código.")
    except sqlite3.Error as e:
        print(f"Error al buscar producto: {e}")
    finally:
        conexion.close()

def reporte_bajo_stock(stock_minimo):
    """
    Genera un reporte de productos cuyo stock está por debajo de un nivel mínimo.
    Recibe como parámetro:
    - `stock_minimo`: Cantidad mínima de stock para filtrar productos.
    """
    conexion = conectar_db()
    cursor = conexion.cursor()
    try:
        # Selecciona todos los productos con stock menor a stock_minimo
        cursor.execute("SELECT codigo, nombre, cantidad FROM productos WHERE cantidad < ?", (stock_minimo,))
        productos = cursor.fetchall()  # Obtiene todos los productos que cumplan la condición
        if productos:
            print(f"{'Cód.':<6}\t{'Nombre':<20}\t{'Cant.':<6}")  # Encabezados
            print("=" * 32)
            for codigo, nombre, cantidad in productos:  # Desempaqueta los campos directamente
                print(f"{codigo:<6}\t{nombre:<20}\t{cantidad:<6}")
                print("-" * 32)
        else:
            print("No hay productos con bajo stock.")
    except sqlite3.Error as e:
        print(f"Error al consultar la base de datos: {e}")
    finally:
        conexion.close()

