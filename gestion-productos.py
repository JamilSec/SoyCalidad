import os # Importamos la libreria os para poder usar system y limpiar la consola

productos = {1: 'Pantalones', 2: 'Camisas', 3: 'Corbatas', 4: 'Casacas'}
precios = {1: 200.00, 2: 120.00, 3: 50.00, 4: 350.00}
stock = {1: 50, 2: 45, 3: 30, 4: 15}


def mostrar_productos():
    os.system("cls" if os.name == "nt" else "clear") # Usamos os, para llamar a system y mandarle "cls", esto nos permitira limpiar la consola, "nt" representa windows
    print("\n========================================")
    print("Lista de Productos:")
    print("========================================")
    print(f"{'ID':<8}{'Producto':<15}{'Precio':<10}{'Stock':<10}")  # Encabezado de la salida de consola
    for key in productos:
        print(f"{key:<8}{productos[key]:<15}{precios[key]:<10}{stock[key]:<10}")
    print("========================================")


def agregar_producto():
    try:
        nuevo_id = max(productos.keys()) + 1
        nombre = input("Ingrese el nombre del nuevo producto: ")
        precio = float(input("Ingrese el precio del nuevo producto: "))
        cantidad = int(input("Ingrese el stock del nuevo producto: "))
        productos[nuevo_id] = nombre
        precios[nuevo_id] = precio
        stock[nuevo_id] = cantidad
        print("\nProducto agregado correctamente.")
    except ValueError:
        print("\nError: Ingrese datos validos.")


def eliminar_producto():
    try:
        id_eliminar = int(input("Ingrese el numero del producto a eliminar: "))
        if id_eliminar in productos:
            del productos[id_eliminar], precios[id_eliminar], stock[id_eliminar]
            print("\nProducto eliminado correctamente.")
        else:
            print("\nEl numero ingresado no existe.")
    except ValueError:
        print("\nError: Ingrese un numero valido.")


def actualizar_producto():
    try:
        id_actualizar = int(input("Ingrese el numero del producto a actualizar: "))
        if id_actualizar in productos:
            nombre = input("Ingrese el nuevo nombre del producto: ")
            precio = float(input("Ingrese el nuevo precio del producto: "))
            cantidad = int(input("Ingrese el nuevo stock del producto: "))
            productos[id_actualizar] = nombre
            precios[id_actualizar] = precio
            stock[id_actualizar] = cantidad
            print("\nProducto actualizado correctamente.")
        else:
            print("\nEl numero ingresado no existe.")
    except ValueError:
        print("\nError: Ingrese datos validos.")


def main():
    while True:
        mostrar_productos()
        print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
        try:
            opcion = int(input("Elija opción: "))
            if opcion == 1:
                agregar_producto()
            elif opcion == 2:
                eliminar_producto()
            elif opcion == 3:
                actualizar_producto()
            elif opcion == 4:
                print("\nSaliendo del programa.")
                break
            else:
                print("\nOpción invalida. Intente nuevamente.")
        except ValueError:
            print("\nPor favor, ingrese una opción valida.")


if __name__ == "__main__":
    main()