inventario = []

def menu():

    sw = True
    while sw:

        print("""Seleccione que acción desea realizar:
            1. Agregar producto
            2. Mostrar inventario
            3. Calcular estadísticas
            4. Salir""")
        
        try:
            
            opcion = int(input("Seleccione una opción: "))

            while opcion == 1:

                producto = input("Producto: ")
                precio = input("Precio: ")
                cantidad = input("Cantidad: ")

                producto = {"nombre": producto, "precio": precio, "cantidad": cantidad}

                inventario.append(producto)

                salir = input("¿Desea salir? (si/no): ")

                opcion != 1


        except ValueError:

            print("Ingrese una opción válida")
            not sw


print(menu())