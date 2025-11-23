"""
Sistema de Gestión de Inventario Avanzado
Inventario con persistencia en archivos CSV y estadísticas.
"""

import servicios
import archivos


def mostrar_menu():
    """Muestra el menú principal de opciones."""
    print("\n" + "="*70)
    print("SISTEMA DE GESTION DE INVENTARIO")
    print("="*70)
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Ver estadisticas")
    print("7. Guardar inventario en CSV")
    print("8. Cargar inventario desde CSV")
    print("9. Salir")
    print("="*70)


def obtener_opcion():
    """
    Solicita y valida la opcion del menu.
    
    Retorna:
        int o None: Opcion seleccionada o None si es invalida
    """
    try:
        opcion = input("Selecciona una opcion (1-9): ").strip()
        opcion_num = int(opcion)
        
        if 1 <= opcion_num <= 9:
            return opcion_num
        else:
            print("Opcion invalida. Por favor, selecciona un numero entre 1 y 9.")
            return None
    except ValueError:
        print("Entrada invalida. Por favor, ingresa un numero.")
        return None


def solicitar_producto():
    """
    Solicita los datos de un producto al usuario.
    
    Retorna:
        tuple o None: (nombre, precio, cantidad) o None si hay error
    """
    try:
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            print("El nombre no puede estar vacio.")
            return None
        
        precio = float(input("Precio del producto: "))
        if precio < 0:
            print("El precio no puede ser negativo.")
            return None
        
        cantidad = int(input("Cantidad en stock: "))
        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            return None
        
        return (nombre, precio, cantidad)
    
    except ValueError:
        print("Error: El precio debe ser un numero y la cantidad un entero.")
        return None


def opcion_agregar(inventario):
    """Maneja la opción de agregar producto."""
    print("\nAGREGAR PRODUCTO")
    print("-" * 70)
    
    datos = solicitar_producto()
    if datos:
        nombre, precio, cantidad = datos
        servicios.agregar_producto(inventario, nombre, precio, cantidad)


def opcion_mostrar(inventario):
    """Maneja la opción de mostrar inventario."""
    servicios.mostrar_inventario(inventario)


def opcion_buscar(inventario):
    """Maneja la opción de buscar producto."""
    print("\nBUSCAR PRODUCTO")
    print("-" * 70)
    
    nombre = input("Nombre del producto a buscar: ").strip()
    producto = servicios.buscar_producto(inventario, nombre)
    
    if producto:
        print(f"\nProducto encontrado:")
        print(f"   - Nombre: {producto['nombre']}")
        print(f"   - Precio: ${producto['precio']:.2f}")
        print(f"   - Cantidad: {producto['cantidad']}")
        print(f"   - Subtotal: ${producto['precio'] * producto['cantidad']:.2f}\n")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.\n")


def opcion_actualizar(inventario):
    """Maneja la opcion de actualizar producto."""
    print("\nACTUALIZAR PRODUCTO")
    print("-" * 70)
    
    nombre = input("Nombre del producto a actualizar: ").strip()
    producto = servicios.buscar_producto(inventario, nombre)
    
    if not producto:
        print(f"Producto '{nombre}' no encontrado en el inventario.\n")
        return
    
    print(f"\nProducto actual: {producto['nombre']} | Precio: ${producto['precio']:.2f} | Cantidad: {producto['cantidad']}")
    print("\nDeja en blanco si no deseas cambiar un valor.")
    
    try:
        # Solicitar nuevo precio
        precio_input = input("Nuevo precio (actual: ${:.2f}): ".format(producto['precio'])).strip()
        nuevo_precio = float(precio_input) if precio_input else None
        
        # Solicitar nueva cantidad
        cantidad_input = input("Nueva cantidad (actual: {}): ".format(producto['cantidad'])).strip()
        nueva_cantidad = int(cantidad_input) if cantidad_input else None
        
        servicios.actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
    
    except ValueError:
        print("Error: Formato invalido. El precio debe ser numero y la cantidad entero.")


def opcion_eliminar(inventario):
    """Maneja la opcion de eliminar producto."""
    print("\nELIMINAR PRODUCTO")
    print("-" * 70)
    
    nombre = input("Nombre del producto a eliminar: ").strip()
    
    # Confirmar eliminacion
    confirmacion = input(f"Estas seguro de eliminar '{nombre}'? (S/N): ").strip().upper()
    
    if confirmacion == 'S':
        servicios.eliminar_producto(inventario, nombre)
    else:
        print("Operación cancelada.")


def opcion_estadisticas(inventario):
    """Maneja la opcion de ver estadisticas."""
    servicios.mostrar_estadisticas(inventario)


def opcion_guardar(inventario):
    """Maneja la opcion de guardar inventario en CSV."""
    print("\nGUARDAR INVENTARIO")
    print("-" * 70)
    
    ruta = input("Nombre del archivo (por defecto 'inventario.csv'): ").strip()
    if not ruta:
        ruta = "inventario.csv"
    
    # Agregar extensión .csv si no la tiene
    if not ruta.endswith('.csv'):
        ruta += '.csv'
    
    archivos.guardar_csv(inventario, ruta)


def opcion_cargar(inventario):
    """Maneja la opcion de cargar inventario desde CSV."""
    print("\nCARGAR INVENTARIO")
    print("-" * 70)
    
    ruta = input("Nombre del archivo a cargar: ").strip()
    if not ruta:
        print("Debes especificar un archivo.")
        return
    
    # Cargar productos del archivo
    productos_nuevos = archivos.cargar_csv(ruta)
    
    if not productos_nuevos:
        return
    
    # Preguntar si sobrescribir o fusionar
    if inventario:
        print(f"\nEl inventario actual tiene {len(inventario)} productos.")
        opcion = input("Sobrescribir inventario actual? (S/N): ").strip().upper()
        
        if opcion == 'S':
            # Sobrescribir: reemplazar inventario
            inventario.clear()
            inventario.extend(productos_nuevos)
            print(f"\nInventario reemplazado. Total de productos: {len(inventario)}")
        elif opcion == 'N':
            # Fusionar inventarios
            print("\nFusionando inventarios...")
            print("   Politica: Se sumara la cantidad y se actualizara el precio para productos existentes.")
            archivos.fusionar_inventarios(inventario, productos_nuevos)
            print(f"\nInventario fusionado. Total de productos: {len(inventario)}")
        else:
            print("Opcion invalida. Operacion cancelada.")
    else:
        # Si el inventario está vacío, simplemente cargar
        inventario.extend(productos_nuevos)
        print(f"\nInventario cargado. Total de productos: {len(inventario)}")


def main():
    """Funcion principal del programa."""
    # Inicializar inventario como lista vacia
    inventario = []
    
    print("\n" + "="*70)
    print("BIENVENIDO AL SISTEMA DE GESTION DE INVENTARIO")
    print("="*70)
    print("Sistema con persistencia en CSV y estadisticas avanzadas.")
    
    # Bucle principal del programa
    while True:
        try:
            mostrar_menu()
            opcion = obtener_opcion()
            
            if opcion is None:
                continue
            
            # Procesar opción seleccionada
            if opcion == 1:
                opcion_agregar(inventario)
            elif opcion == 2:
                opcion_mostrar(inventario)
            elif opcion == 3:
                opcion_buscar(inventario)
            elif opcion == 4:
                opcion_actualizar(inventario)
            elif opcion == 5:
                opcion_eliminar(inventario)
            elif opcion == 6:
                opcion_estadisticas(inventario)
            elif opcion == 7:
                opcion_guardar(inventario)
            elif opcion == 8:
                opcion_cargar(inventario)
            elif opcion == 9:
                print("\n" + "="*70)
                print("Gracias por usar el Sistema de Gestion de Inventario!")
                print("="*70 + "\n")
                break
        
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            print("Hasta luego!\n")
            break
        except Exception as e:
            print(f"\nError inesperado: {e}")
            print("El programa continuara ejecutandose.\n")


if __name__ == "__main__":
    main()
