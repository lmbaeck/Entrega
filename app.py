""" Colorama
Importación y uso de Colorama:

Se importaron Fore, Style, y init de Colorama.
Se llamó a init(autoreset=True) para restablecer automáticamente los colores después de cada impresión.

Mensajes con colores:
Mensajes en verde (Fore.GREEN) para operaciones exitosas como agregar o actualizar un producto.
Mensajes en rojo (Fore.RED) para errores o advertencias, como opciones no válidas o eliminación.
Mensajes en azul, cian, o magenta (Fore.BLUE, Fore.CYAN, Fore.MAGENTA) para encabezados y resultados informativos.

Formato limpio y consistente:
El texto mantiene un formato atractivo mientras comunica claramente el propósito del mensaje.
"""
# Importación de funciones necesarias desde módulos externos:
from menu_funciones import (menu_mostrar_opciones, solicitar_datos_producto, solicitar_stock_minimo)
from funciones_db import (crear_tabla_productos, insertar_producto, 
                          mostrar_productos, actualizar_producto, 
                          eliminar_producto, mostrar_producto_por_codigo, 
                          reporte_bajo_stock)

# Importar Colorama para colores en la consola
from colorama import Fore, Style, init

# Inicializar Colorama
init(autoreset=True)  # Resetea el color al predeterminado después de cada línea.

# Función principal que se ejecuta al iniciar el programa
def menu_principal():
    crear_tabla_productos()  # Crea la tabla de productos en la base de datos si no existe.

    while True:
        opcion = menu_mostrar_opciones()  # Muestra las opciones del menú al usuario.
        
        if opcion == "1":  # Opción para agregar un producto.
            nombre, descripcion, cantidad, precio, categoria = solicitar_datos_producto()
            insertar_producto(nombre, descripcion, cantidad, precio, categoria)
            print(Fore.GREEN + "Producto agregado correctamente.")  # Mensaje en verde.

        elif opcion == "2":  # Opción para listar todos los productos.
            print(Fore.BLUE + "Listado de productos:")  # Mensaje en azul.
            mostrar_productos()

        elif opcion == "3":  # Opción para actualizar un producto.
            mostrar_productos()
            try:
                codigo = int(input(Fore.YELLOW + "Ingrese el código del producto que desea actualizar: "))
                actualizar_producto(codigo)
                print(Fore.GREEN + "Producto actualizado con éxito.")  # Mensaje en verde.
            except ValueError:
                print(Fore.RED + "Error: debe ingresar un número válido para el código.")  # Mensaje en rojo.

        elif opcion == "4":  # Opción para eliminar un producto.
            eliminar_producto()
            print(Fore.RED + "Producto eliminado.")  # Mensaje en rojo.

        elif opcion == "5":  # Opción para mostrar un producto por su código.
            producto = mostrar_producto_por_codigo()
            if producto:
                print(Fore.CYAN + "Detalles del producto:")  # Mensaje en cian.
                for clave, valor in producto.items():
                    print(f"{clave}: {valor}")

        elif opcion == "6":  # Opción para mostrar productos con bajo stock.
            stock_minimo = solicitar_stock_minimo()
            try:
                print(Fore.MAGENTA + f"Productos con stock menor a {stock_minimo}:")
                reporte_bajo_stock(stock_minimo)
            except Exception as e:
                print(Fore.RED + f"Error al obtener productos con stock bajo: {e}")

        elif opcion == "7":  # Opción para salir de la aplicación.
            print(Fore.GREEN + "Gracias por usar nuestra App")
            break

        else:  # Manejo de opciones no válidas.
            print(Fore.RED + "Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()
