# servicios.py
# Módulo con funciones CRUD y estadísticas del inventario

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un producto al inventario
    
    Parámetros:
    - inventario: lista de diccionarios con productos
    - nombre: nombre del producto (str)
    - precio: precio unitario (float)
    - cantidad: cantidad en stock (int)
    
    Retorna: True si se agregó, False si ya existe
    """
    # Verificar si el producto ya existe
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print(f"El producto '{nombre}' ya existe en el inventario")
            return False
    
    # Crear y agregar el producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado exitosamente")
    return True

def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario
    
    Parámetros:
    - inventario: lista de diccionarios con productos
    """
    if not inventario:
        print("El inventario está vacío")
        return
    
    print("\n=== INVENTARIO ===")
    # Mostrar cada producto con su subtotal
    for producto in inventario:
        subtotal = producto["precio"] * producto["cantidad"]
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']:.2f} | Cantidad: {producto['cantidad']} | Subtotal: ${subtotal:.2f}")
    print()

def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre
    
    Parámetros:
    - inventario: lista de diccionarios con productos
    - nombre: nombre del producto a buscar (str)
    
    Retorna: diccionario del producto o None si no existe
    """
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio y/o cantidad de un producto
    
    Parámetros:
    - inventario: lista de diccionarios con productos
    - nombre: nombre del producto a actualizar (str)
    - nuevo_precio: nuevo precio (float, opcional)
    - nueva_cantidad: nueva cantidad (int, opcional)
    
    Retorna: True si se actualizó, False si no existe
    """
    producto = buscar_producto(inventario, nombre)
    
    if producto is None:
        print(f"Producto '{nombre}' no encontrado")
        return False
    
    # Actualizar los valores si se proporcionaron
    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio
    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad
    
    print(f"Producto '{nombre}' actualizado exitosamente")
    return True

def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario
    
    Parámetros:
    - inventario: lista de diccionarios con productos
    - nombre: nombre del producto a eliminar (str)
    
    Retorna: True si se eliminó, False si no existe
    """
    producto = buscar_producto(inventario, nombre)
    
    if producto is None:
        print(f"Producto '{nombre}' no encontrado")
        return False
    
    inventario.remove(producto)
    print(f"Producto '{nombre}' eliminado exitosamente")
    return True

def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario
    
    Parámetros:
    - inventario: lista de diccionarios con productos
    
    Retorna: tupla con (unidades_totales, valor_total, producto_mas_caro, producto_mayor_stock)
    """
    if not inventario:
        return (0, 0.0, None, None)
    
    # Calcular unidades totales
    unidades_totales = sum(p["cantidad"] for p in inventario)
    
    # Calcular valor total (usando lambda opcional)
    subtotal = lambda p: p["precio"] * p["cantidad"]
    valor_total = sum(subtotal(p) for p in inventario)
    
    # Encontrar producto más caro
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    
    # Encontrar producto con mayor stock
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])
    
    return (unidades_totales, valor_total, producto_mas_caro, producto_mayor_stock)

def mostrar_estadisticas(inventario):
    """
    Muestra las estadísticas del inventario de forma legible
    
    Parámetros:
    - inventario: lista de diccionarios con productos
    """
    if not inventario:
        print("El inventario está vacío. No hay estadísticas para mostrar.")
        return
    
    # Obtener estadísticas
    unidades, valor, mas_caro, mayor_stock = calcular_estadisticas(inventario)
    
    # Mostrar estadísticas
    print("\n=== ESTADÍSTICAS DEL INVENTARIO ===")
    print(f"Unidades totales: {unidades}")
    print(f"Valor total del inventario: ${valor:.2f}")
    print(f"Producto más caro: {mas_caro['nombre']} (${mas_caro['precio']:.2f})")
    print(f"Producto con mayor stock: {mayor_stock['nombre']} ({mayor_stock['cantidad']} unidades)")
    print()