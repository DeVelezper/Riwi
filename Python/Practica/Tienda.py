# Simulador de tienda en Python

# Diccionario de productos con precio y stock
productos = {
    "manzana": {"precio": 2000, "stock": 50},
    "banana": {"precio": 1500, "stock": 30},
    "pan": {"precio": 3000, "stock": 20},
    "leche": {"precio": 4000, "stock": 25},
    "huevo": {"precio": 5000, "stock": 40}
}

carrito = []

# Función para mostrar productos disponibles
def mostrar_productos():
    print("\nProductos disponibles:")
    for producto, info in productos.items():
        print(f"{producto.title()} - Precio: ${info['precio']} - Stock: {info['stock']}")

# Función para agregar productos al carrito
def agregar_al_carrito(producto, cantidad):
    subtotal = productos[producto]["precio"] * cantidad
    carrito.append({"producto": producto, "cantidad": cantidad, "precio_unitario": productos[producto]["precio"], "subtotal": subtotal})
    productos[producto]["stock"] -= cantidad
    print(f"{cantidad} {producto}(s) agregados al carrito. Subtotal: ${subtotal}")

# Función para validar cantidad
def validar_cantidad(producto, cantidad):
    if not cantidad.isdigit() or int(cantidad) <= 0:
        print("Cantidad inválida. Debe ser un número positivo.")
        return False
    cantidad = int(cantidad)
    if cantidad > productos[producto]["stock"]:
        print(f"Lo sentimos, solo hay {productos[producto]['stock']} unidades disponibles.")
        return False
    return cantidad

# Función para calcular total y aplicar descuentos
def calcular_total():
    total = sum(item["subtotal"] for item in carrito)
    descuento = 0
    if total >= 20000:
        descuento = total * 0.1  # 10% de descuento
        total -= descuento
    return total, descuento

# Función para mostrar el carrito
def mostrar_carrito():
    if not carrito:
        print("No hay productos en el carrito.")
        return
    print("\nResumen de su compra:")
    for item in carrito:
        print(f"{item['producto'].title()} x{item['cantidad']} = ${item['subtotal']}")
    total, descuento = calcular_total()
    if descuento > 0:
        print(f"Descuento aplicado: ${descuento}")
    print(f"Total a pagar: ${total}")

# Función principal
def tienda():
    print("¡Bienvenido a la tienda virtual!")
    while True:
        mostrar_productos()
        seleccion = input("\nIngrese el producto que desea comprar (o 'salir' para terminar): ").lower()
        if seleccion == "salir":
            break
        if seleccion in productos:
            cantidad = input(f"¿Cuántos {seleccion}s desea comprar?: ")
            cantidad_valida = validar_cantidad(seleccion, cantidad)
            if cantidad_valida:
                agregar_al_carrito(seleccion, cantidad_valida)
        else:
            print("Producto no disponible.")
    mostrar_carrito()
    print("\n¡Gracias por su compra!")

# Ejecutar la tienda
if __name__ == "__main__":
    tienda()
