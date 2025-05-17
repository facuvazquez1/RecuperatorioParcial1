# Alumno: Facundo Gaston Vazquez
# Materia: Programacion 1
# Programa de gestión de stock de productos

# Listas paralelas para nombres de productos y sus cantidades
nombres = []
cantidades = []

salir = True

while salir:
    # Mostrar menú de opciones
    print("\n🛒 Menú de opciones:")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Consultar stock de un producto")     
    print("4. Actualizar stock")                   
    print("5. Ver todos los productos")           
    print("6. Salir")                             
    
    opcion = input("Seleccione una opción (1-6): ")

    if opcion == "1":
        # Agregar un nuevo producto
        nombre = input("Ingrese el nombre del producto: ")
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))
        except ValueError:
            print("Cantidad inválida. Debe ser un número entero.")
            continue
        nombres.append(nombre)
        cantidades.append(cantidad)
        print(f"Producto '{nombre}' agregado con éxito, stock = {cantidad}.")

    elif opcion == "2":
        # Mostrar productos agotados
        print("\nProductos agotados:")
        agotados = False
        for i in range(len(nombres)):
            if cantidades[i] == 0:
                print(f"- {nombres[i]}")
                agotados = True
        if not agotados:
            print("No hay productos agotados.")

    elif opcion == "3":
        # Consultar stock de un producto específico   # Modificación: implementación del punto 4
        producto = input("Ingrese el nombre del producto a consultar: ")
        encontrado = False
        for i in range(len(nombres)):
            if nombres[i].lower() == producto.lower():
                print(f"Stock de '{nombres[i]}': {cantidades[i]} unidades")
                encontrado = True
                break
        if not encontrado:
            print(f"Producto '{producto}' no encontrado.")

    elif opcion == "4":
        # Actualizar el stock de un producto existente
        producto = input("Ingrese el nombre del producto a actualizar: ")
        encontrado = False
        for i in range(len(nombres)):
            if nombres[i].lower() == producto.lower():
                encontrado = True
                try:
                    nueva_cantidad = int(input(f"Ingrese la nueva cantidad para '{nombres[i]}': "))
                except ValueError:
                    print("Cantidad inválida. Debe ser un número entero.")
                    break
                cantidades[i] = nueva_cantidad
                print(f"Stock de '{nombres[i]}' actualizado a {nueva_cantidad}.")
                break
        if not encontrado:
            print(f"Producto '{producto}' no encontrado.")

    elif opcion == "5":
        # Listar todos los productos con su stock
        if not nombres:
            print("\nNo hay productos registrados.")
        else:
            print("\nListado de productos y stock:")
            for i in range(len(nombres)):
                print(f"- {nombres[i]}: {cantidades[i]} unidades")

    elif opcion == "6":
        # Salir del programa
        print("Gracias por usar el sistema de gestión de stock.")
        salir = False

    else:
        print("Opción inválida. Por favor seleccione una opción del 1 al 6.")
