def menu_mostrar_opciones():
    """
    Muestra el menú principal de opciones al usuario y captura su elección.
    Opciones disponibles:
    1. Registrar un nuevo producto.
    2. Mostrar todos los productos registrados.
    3. Actualizar los datos de un producto existente.
    4. Eliminar un producto de la base de datos.
    5. Buscar un producto por su ID.
    6. Generar un reporte de productos con stock bajo.
    7. Salir del programa.
    Retorna la opción seleccionada por el usuario como una cadena.
    """
    print("\n=== Menú Principal ===")
    print("1. Registrar producto")
    print("2. Mostrar todos los productos")
    print("3. Actualizar un producto")
    print("4. Eliminar un producto")
    print("5. Buscar un producto")
    print("6. Reporte de bajo stock")
    print("7. Salir")
    return input("Seleccione una opción: ")

def solicitar_datos_producto():
    """
    Solicita al usuario los datos necesarios para registrar un nuevo producto.
    Datos solicitados:
    - Nombre del producto.
    - Descripción del producto.
    - Cantidad disponible en stock.
    - Precio unitario del producto.
    - Categoría a la que pertenece el producto.
    Retorna una tupla con los datos ingresados.
    """
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción del producto: ")
    cantidad = int(input("Cantidad disponible: "))
    precio = float(input("Precio unitario: "))
    categoria = input("Categoría: ")
    return nombre, descripcion, cantidad, precio, categoria

def solicitar_id_producto():
    """
    Solicita al usuario ingresar el ID del producto para realizar una acción específica 
    (como actualizar, eliminar o buscar).
    Retorna el ID ingresado como un entero.
    """
    return int(input("Ingrese el ID del producto: "))

def solicitar_stock_minimo():
    """
    Solicita al usuario ingresar un límite mínimo de stock.
    Este valor se utiliza para generar un reporte de productos cuyo stock está 
    por debajo de este límite.
    Retorna el stock mínimo como un entero.
    """
    return int(input("Ingrese el límite mínimo de stock: "))

def mostrar_mensaje(mensaje):
    """
    Muestra un mensaje genérico al usuario.
    Ideal para informar resultados de acciones (como éxito o error).
    Parámetros:
    - mensaje (str): El mensaje que se desea mostrar.
    """
    print(mensaje)
