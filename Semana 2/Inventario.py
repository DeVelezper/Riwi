# Programa: Registro de productos en inventario
# Este programa permite al usuario ingresar datos de un producto
# (nombre, cantidad, precio), calcula el costo total y almacena
# el producto en una lista de inventario. Muestra el inventario
# actualizado en consola.

# Lista que almacena todos los productos del inventario
inventory = []

def enter_product():
    # Solicitar el nombre del producto
    name = input("Ingresa el nombre del producto: \n")

    # Validar que el precio sea un número válido
    while True:
        try:
            price = float(input(f"Ingresa el precio de {name} \n"))
            break
        except ValueError:
            print(f"""Ocurrio un error: entrada invalidad.
Ingrese un valor correcto\n""")

    # Validar que la cantidad sea un número entero válido
    while True:
        try:                        
            amount = int(input(f"Ingresa la cantidad de {name} \n"))
            break   
        except ValueError:
            print(f"""Ocurrio un error: entrada invalidad.
Ingrese un valor correcto\n""")
    
    # Crear y agregar el producto al inventario
    product = {
        "Name":name,
        "Price":price,
        "Amount":amount
    }
    inventory.append(product)
    print(f"Producto agregado: {name}")

def show_inventory():
    # Mostrar todos los productos del inventario
    for product in inventory:
        subtotal = product["Price"] * product["Amount"]
        print(f"Producto: {product["Name"]} | Precio: {product["Price"]} | Cantidad:{product["Amount"]} | Total: {subtotal}")
    return

def calculate_total():
    # Calcular el costo total del inventario
    total_cost = sum(i["Price"] * i["Amount"] for i in inventory)
    return total_cost

def calculate_estatistics():
    # Calcular la cantidad total de productos
    return len(inventory)

# Menú principal del programa
while True:
    print("""Menu
1. Agregar producto
2. Mostrar resultado
3. Calcular estadisticas
4. Salir""")

    option = input("Ingresa la opcion que quieres hacer: \n")

    if option == "1":
        enter_product()

    elif option == "2":
        if inventory:
            print("Productos en el inventario\n")
            show_inventory()
        else:
            print("El inventario esta vacio")
    
    elif option == "3":
        if inventory:
            print(f"""Costo total de inventario: ${calculate_total():.2f}           
Esta es la cantidad total de productos: {calculate_estatistics()}""")
        else:
            print("El inventario esta vacio")

    elif option == "4":
        break
    else:
        print(f"""Ocurrio un error: entrada invalidad.
Ingrese un valor correcto\n""")

# RESUMEN DEL PROGRAMA:
# Este programa gestiona un inventario de productos. Permite agregar productos
# con su nombre, precio y cantidad, mostrar la lista completa con subtotales
# individuales, calcular estadísticas (valor total y cantidad de productos)
# y validar los datos ingresados manejando errores de entrada.