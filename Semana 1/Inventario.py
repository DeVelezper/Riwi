# ------------------------------
# Programa: Registro de productos en inventario
# Este programa permite al usuario ingresar datos de un producto
# (nombre, cantidad, precio), calcula el costo total y almacena
# el producto en una lista de inventario. Muestra el inventario
# actualizado en consola.
# ------------------------------

# Inicializar lista de inventario (persistente dentro de esta ejecución)
inventario = []

# ------------------------------
# Solicitar nombre del producto al usuario
# Se valida que contenga solo letras (sin números ni símbolos)
# ------------------------------
while True:
    nombre = input("Ingrese el nombre del producto: \n")
    if nombre.isalpha():
        break
    print("Error: El nombre del producto debe contener solo letras. Intente de nuevo.\n")

# ------------------------------
# Solicitar cantidad del producto
# Se valida que sea un número entero
# ------------------------------
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: \n"))
        break
    except ValueError:
        print("Error: La cantidad debe ser un número entero. Intente de nuevo.\n")

# ------------------------------
# Solicitar precio unitario del producto
# Se valida que sea un número decimal
# ------------------------------
while True:
    try:
        precio = float(input("Ingrese el precio del producto: \n"))
        break
    except ValueError:
        print("Error: El precio debe ser un número. Intente de nuevo.\n")

# ------------------------------
# Calcular costo total del producto
# ------------------------------
costo_total = cantidad * precio
print(f"El costo total del producto '{nombre}' es: {costo_total:.2f}\n")

# ------------------------------
# Crear diccionario con los datos del producto
# ------------------------------
producto = {
    'nombre': nombre, 
    'cantidad': cantidad, 
    'precio': precio, 
    'costo_total': costo_total
}

# ------------------------------
# Agregar el producto a la lista de inventario
# La lista inventario es persistente mientras dure la ejecución
# ------------------------------
inventario.append(producto)

# ------------------------------
# Mostrar inventario actualizado en consola
# ------------------------------
print("Inventario actualizado:\n")
for i in inventario:
    print(f"Producto: {i['nombre']}, Cantidad: {i['cantidad']}, Precio: {i['precio']:.2f}, Costo Total: {i['costo_total']:.2f}\n")

# ------------------------------
# Fin del programa
# El programa permite ingresar un producto, validarlo, calcular su costo total,
# agregarlo al inventario y mostrarlo de manera clara en consola.
# ------------------------------
