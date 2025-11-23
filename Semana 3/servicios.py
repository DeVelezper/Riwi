"""
Módulo de servicios para gestión de inventario.
Contiene funciones CRUD y cálculo de estadísticas.
"""


def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.
    
    Parametros:
        inventario (list): Lista de diccionarios con productos
        nombre (str): Nombre del producto
        precio (float): Precio unitario del producto
        cantidad (int): Cantidad en stock
    
    Retorna:
        bool: True si se agrego correctamente, False si ya existia
    """
    # Verificar que el precio y cantidad sean validos
    if precio < 0 or cantidad < 0:
        print("Error: El precio y la cantidad no pueden ser negativos.")
        return False
    
    # Verificar si el producto ya existe
    if buscar_producto(inventario, nombre):
        print(f"El producto '{nombre}' ya existe en el inventario.")
        return False
    
    # Agregar el producto
    producto = {
        "nombre": nombre,
        "precio": float(precio),
        "cantidad": int(cantidad)
    }
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado exitosamente.")
    return True


def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario en formato tabular.
    
    Parametros:
        inventario (list): Lista de diccionarios con productos
    
    Retorna:
        None
    """
    if not inventario:
        print("\nEl inventario esta vacio.\n")
        return
    
    print("\n" + "="*70)
    print("INVENTARIO DE PRODUCTOS")
    print("="*70)
    print(f"{'Nombre':<30} {'Precio':>12} {'Cantidad':>12} {'Subtotal':>12}")
    print("-"*70)
    
    # Lambda para calcular subtotal
    calcular_subtotal = lambda p: p["precio"] * p["cantidad"]
    
    for producto in inventario:
        subtotal = calcular_subtotal(producto)
        print(f"{producto['nombre']:<30} ${producto['precio']:>11.2f} {producto['cantidad']:>12} ${subtotal:>11.2f}")
    
    print("="*70 + "\n")


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre en el inventario.
    
    Parametros:
        inventario (list): Lista de diccionarios con productos
        nombre (str): Nombre del producto a buscar
    
    Retorna:
        dict o None: Diccionario del producto si existe, None si no se encuentra
    """
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio y/o cantidad de un producto existente.
    
    Parametros:
        inventario (list): Lista de diccionarios con productos
        nombre (str): Nombre del producto a actualizar
        nuevo_precio (float, opcional): Nuevo precio del producto
        nueva_cantidad (int, opcional): Nueva cantidad del producto
    
    Retorna:
        bool: True si se actualizo correctamente, False si no se encontro
    """
    producto = buscar_producto(inventario, nombre)
    
    if not producto:
        print(f"Producto '{nombre}' no encontrado en el inventario.")
        return False
    
    # Validar valores
    if nuevo_precio is not None:
        if nuevo_precio < 0:
            print("Error: El precio no puede ser negativo.")
            return False
        producto["precio"] = float(nuevo_precio)
    
    if nueva_cantidad is not None:
        if nueva_cantidad < 0:
            print("Error: La cantidad no puede ser negativa.")
            return False
        producto["cantidad"] = int(nueva_cantidad)
    
    if nuevo_precio is None and nueva_cantidad is None:
        print("No se especificaron cambios para actualizar.")
        return False
    
    print(f"Producto '{nombre}' actualizado exitosamente.")
    return True


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario por nombre.
    
    Parametros:
        inventario (list): Lista de diccionarios con productos
        nombre (str): Nombre del producto a eliminar
    
    Retorna:
        bool: True si se elimino correctamente, False si no se encontro
    """
    producto = buscar_producto(inventario, nombre)
    
    if not producto:
        print(f"Producto '{nombre}' no encontrado en el inventario.")
        return False
    
    inventario.remove(producto)
    print(f"Producto '{nombre}' eliminado exitosamente.")
    return True


def calcular_estadisticas(inventario):
    """
    Calcula estadisticas del inventario.
    
    Parametros:
        inventario (list): Lista de diccionarios con productos
    
    Retorna:
        dict: Diccionario con las estadisticas:
            - unidades_totales (int): Total de unidades en inventario
            - valor_total (float): Valor total del inventario
            - producto_mas_caro (dict): Producto con mayor precio
            - producto_mayor_stock (dict): Producto con mayor cantidad
    """
    if not inventario:
        return {
            "unidades_totales": 0,
            "valor_total": 0.0,
            "producto_mas_caro": None,
            "producto_mayor_stock": None
        }
    
    # Lambda para calcular subtotal de un producto
    calcular_subtotal = lambda p: p["precio"] * p["cantidad"]
    
    # Calcular unidades totales
    unidades_totales = sum(p["cantidad"] for p in inventario)
    
    # Calcular valor total del inventario
    valor_total = sum(calcular_subtotal(p) for p in inventario)
    
    # Encontrar producto más caro
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    
    # Encontrar producto con mayor stock
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])
    
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }


def mostrar_estadisticas(inventario):
    """
    Muestra las estadisticas del inventario en formato legible.
    
    Parametros:
        inventario (list): Lista de diccionarios con productos
    
    Retorna:
        None
    """
    stats = calcular_estadisticas(inventario)
    
    if stats["unidades_totales"] == 0:
        print("\nNo hay productos en el inventario para calcular estadisticas.\n")
        return
    
    print("\n" + "="*70)
    print("ESTADISTICAS DEL INVENTARIO")
    print("="*70)
    print(f"Total de unidades en inventario: {stats['unidades_totales']}")
    print(f"Valor total del inventario: ${stats['valor_total']:.2f}")
    print(f"\nProducto mas caro:")
    print(f"  - {stats['producto_mas_caro']['nombre']} - ${stats['producto_mas_caro']['precio']:.2f}")
    print(f"\nProducto con mayor stock:")
    print(f"  - {stats['producto_mayor_stock']['nombre']} - {stats['producto_mayor_stock']['cantidad']} unidades")
    print("="*70 + "\n")
