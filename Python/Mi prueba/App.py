# app.py
# Programa principal: Sistema de gestión de inventario con persistencia CSV

# Importar módulos personalizados
import servicios
import archivos

# Lista global que almacena el inventario
inventario = []

def menu_agregar():
    """Solicita datos y agrega un producto al inventario"""
    print("\n=== AGREGAR PRODUCTO ===")
    
    # Solicitar nombre del producto
    nombre = input("Ingresa el nombre del producto: ")
    
    # Validar precio
    while True:
        try:
            precio = float(input(f"Ingresa el precio de {nombre}: "))
            if precio < 0:
                print("El precio no puede ser negativo")
                continue
            break
        except ValueError:
            print("Error: Ingresa un número válido para el precio")
    
    # Validar cantidad
    while True:
        try:
            cantidad = int(input(f"Ingresa la cantidad de {nombre}: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa")
                continue
            break
        except ValueError:
            print("Error: Ingresa un número entero válido para la cantidad")
    
    # Agregar producto
    servicios.agregar_producto(inventario, nombre, precio, cantidad)

def menu_buscar():
    """Busca un producto por nombre y muestra su información"""
    print("\n=== BUSCAR PRODUCTO ===")
    nombre = input("Ingresa el nombre del producto a buscar: ")
    
    producto = servicios.buscar_producto(inventario, nombre)
    
    if producto:
        subtotal = producto["precio"] * producto["cantidad"]
        print(f"\nProducto encontrado:")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']:.2f}")
        print(f"Cantidad: {producto['cantidad']}")
        print(f"Subtotal: ${subtotal:.2f}")
    else:
        print(f"Producto '{nombre}' no encontrado")

def menu_actualizar():
    """Actualiza precio y/o cantidad de un producto"""
    print("\n=== ACTUALIZAR PRODUCTO ===")
    nombre = input("Ingresa el nombre del producto a actualizar: ")
    
    # Verificar si existe
    producto = servicios.buscar_producto(inventario, nombre)
    if not producto:
        print(f"Producto '{nombre}' no encontrado")
        return
    
    # Mostrar valores actuales
    print(f"\nValores actuales:")
    print(f"Precio: ${producto['precio']:.2f}")
    print(f"Cantidad: {producto['cantidad']}")
    
    # Preguntar qué actualizar
    print("\n¿Qué deseas actualizar?")
    print("1. Precio")
    print("2. Cantidad")
    print("3. Ambos")
    
    opcion = input("Selecciona una opción: ")
    
    nuevo_precio = None
    nueva_cantidad = None
    
    # Actualizar precio
    if opcion in ["1", "3"]:
        while True:
            try:
                nuevo_precio = float(input("Nuevo precio: "))
                if nuevo_precio < 0:
                    print("El precio no puede ser negativo")
                    continue
                break
            except ValueError:
                print("Error: Ingresa un número válido")
    
    # Actualizar cantidad
    if opcion in ["2", "3"]:
        while True:
            try:
                nueva_cantidad = int(input("Nueva cantidad: "))
                if nueva_cantidad < 0:
                    print("La cantidad no puede ser negativa")
                    continue
                break
            except ValueError:
                print("Error: Ingresa un número entero válido")
    
    # Aplicar actualización
    servicios.actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)

def menu_eliminar():
    """Elimina un producto del inventario"""
    print("\n=== ELIMINAR PRODUCTO ===")
    nombre = input("Ingresa el nombre del producto a eliminar: ")
    
    # Confirmar eliminación
    confirmacion = input(f"¿Estás seguro de eliminar '{nombre}'? (S/N): ")
    
    if confirmacion.upper() == 'S':
        servicios.eliminar_producto(inventario, nombre)
    else:
        print("Eliminación cancelada")

def menu_guardar_csv():
    """Guarda el inventario en un archivo CSV"""
    print("\n=== GUARDAR INVENTARIO EN CSV ===")
    
    # Solicitar ruta del archivo
    ruta = input("Ingresa la ruta del archivo (ejemplo: inventario.csv): ")
    
    # Si no tiene extensión .csv, agregarla
    if not ruta.endswith('.csv'):
        ruta += '.csv'
    
    # Guardar
    archivos.guardar_csv(inventario, ruta)

def menu_cargar_csv():
    """Carga el inventario desde un archivo CSV"""
    print("\n=== CARGAR INVENTARIO DESDE CSV ===")
    
    # Solicitar ruta del archivo
    ruta = input("Ingresa la ruta del archivo CSV: ")
    
    # Cargar productos
    productos_cargados = archivos.cargar_csv(ruta)
    
    if not productos_cargados:
        return
    
    # Preguntar si sobrescribir o fusionar
    if inventario:
        print("\nYa tienes productos en el inventario actual.")
        opcion = input("¿Sobrescribir inventario actual? (S/N): ")
        
        if opcion.upper() == 'S':
            # Sobrescribir
            inventario.clear()
            inventario.extend(productos_cargados)
            print(f"\nInventario sobrescrito. Total de productos: {len(inventario)}")
        else:
            # Fusionar
            print("\nFusionando inventarios...")
            print("Política: Si el producto existe, se suma la cantidad y se actualiza el precio")
            archivos.fusionar_inventarios(inventario, productos_cargados)
            print(f"Total de productos en inventario: {len(inventario)}")
    else:
        # Si el inventario está vacío, simplemente cargar
        inventario.extend(productos_cargados)
        print(f"\nInventario cargado. Total de productos: {len(inventario)}")

# Menú principal del programa
while True:
    print("\n" + "="*40)
    print("SISTEMA DE GESTIÓN DE INVENTARIO")
    print("="*40)
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Calcular estadísticas")
    print("7. Guardar inventario en CSV")
    print("8. Cargar inventario desde CSV")
    print("9. Salir")
    print("="*40)
    
    # Solicitar opción al usuario
    opcion = input("Selecciona una opción (1-9): ")
    
    try:
        # Procesar opción 1: Agregar producto
        if opcion == "1":
            menu_agregar()
        
        # Procesar opción 2: Mostrar inventario
        elif opcion == "2":
            servicios.mostrar_inventario(inventario)
        
        # Procesar opción 3: Buscar producto
        elif opcion == "3":
            menu_buscar()
        
        # Procesar opción 4: Actualizar producto
        elif opcion == "4":
            menu_actualizar()
        
        # Procesar opción 5: Eliminar producto
        elif opcion == "5":
            menu_eliminar()
        
        # Procesar opción 6: Estadísticas
        elif opcion == "6":
            servicios.mostrar_estadisticas(inventario)
        
        # Procesar opción 7: Guardar CSV
        elif opcion == "7":
            menu_guardar_csv()
        
        # Procesar opción 8: Cargar CSV
        elif opcion == "8":
            menu_cargar_csv()
        
        # Procesar opción 9: Salir
        elif opcion == "9":
            print("\n¡Gracias por usar el sistema de inventario!")
            break
        
        # Opción inválida
        else:
            print("\nError: Opción inválida. Selecciona un número del 1 al 9")
    
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario")
        break
    except Exception as e:
        print(f"\nError inesperado: {e}")
        print("El programa continuará ejecutándose")

# RESUMEN DEL PROGRAMA:
# Este sistema de gestión de inventario permite realizar operaciones CRUD completas
# (Crear, Leer, Actualizar, Eliminar) sobre productos, calcular estadísticas
# avanzadas (unidades totales, valor total, producto más caro, mayor stock),
# y persistir los datos en archivos CSV. El sistema valida todas las entradas,
# maneja errores sin cerrarse, y ofrece opciones de fusión o sobrescritura al
# cargar datos. Está modularizado en tres archivos: app.py (menú principal),
# servicios.py (funciones CRUD y estadísticas) y archivos.py (persistencia CSV).