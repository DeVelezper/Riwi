# archivos.py
# Módulo para guardar y cargar inventario en formato CSV

import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV
    
    Parámetros:
    - inventario: lista de diccionarios con productos
    - ruta: ruta del archivo CSV (str)
    - incluir_header: si incluir encabezado (bool)
    
    Retorna: True si se guardó correctamente, False en caso de error
    """
    # Validar que el inventario no esté vacío
    if not inventario:
        print("El inventario está vacío. No hay nada que guardar.")
        return False
    
    try:
        # Abrir archivo y escribir
        with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            
            # Escribir encabezado si se solicita
            if incluir_header:
                writer.writerow(['nombre', 'precio', 'cantidad'])
            
            # Escribir cada producto
            for producto in inventario:
                writer.writerow([
                    producto['nombre'],
                    producto['precio'],
                    producto['cantidad']
                ])
        
        print(f"Inventario guardado en: {ruta}")
        return True
        
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{ruta}'")
        return False
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        return False

def cargar_csv(ruta):
    """
    Carga un inventario desde un archivo CSV
    
    Parámetros:
    - ruta: ruta del archivo CSV (str)
    
    Retorna: lista de productos cargados, o lista vacía si hay error
    """
    productos_cargados = []
    filas_invalidas = 0
    
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo)
            
            # Leer y validar encabezado
            try:
                header = next(reader)
                if header != ['nombre', 'precio', 'cantidad']:
                    print(f"Error: El archivo no tiene el encabezado válido (nombre,precio,cantidad)")
                    return []
            except StopIteration:
                print("Error: El archivo está vacío")
                return []
            
            # Leer cada fila
            for numero_fila, fila in enumerate(reader, start=2):
                # Validar que tenga 3 columnas
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue
                
                try:
                    nombre = fila[0].strip()
                    precio = float(fila[1])
                    cantidad = int(fila[2])
                    
                    # Validar que precio y cantidad no sean negativos
                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue
                    
                    # Agregar producto válido
                    productos_cargados.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                    
                except ValueError:
                    filas_invalidas += 1
                    continue
        
        # Mostrar resumen
        print(f"\nProductos cargados correctamente: {len(productos_cargados)}")
        if filas_invalidas > 0:
            print(f"Filas inválidas omitidas: {filas_invalidas}")
        
        return productos_cargados
        
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no existe")
        return []
    except UnicodeDecodeError:
        print(f"Error: El archivo '{ruta}' no tiene formato de texto válido")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []

def fusionar_inventarios(inventario_actual, inventario_nuevo):
    """
    Fusiona dos inventarios actualizando productos existentes y agregando nuevos
    
    Política de fusión:
    - Si el producto existe: suma cantidades y actualiza precio al nuevo
    - Si el producto no existe: lo agrega
    
    Parámetros:
    - inventario_actual: inventario existente (lista)
    - inventario_nuevo: inventario a fusionar (lista)
    
    Retorna: número de productos fusionados/agregados
    """
    productos_agregados = 0
    productos_actualizados = 0
    
    for producto_nuevo in inventario_nuevo:
        encontrado = False
        
        # Buscar si el producto ya existe
        for producto_actual in inventario_actual:
            if producto_actual["nombre"].lower() == producto_nuevo["nombre"].lower():
                # Actualizar producto existente
                producto_actual["cantidad"] += producto_nuevo["cantidad"]
                producto_actual["precio"] = producto_nuevo["precio"]
                productos_actualizados += 1
                encontrado = True
                break
        
        # Si no existe, agregarlo
        if not encontrado:
            inventario_actual.append(producto_nuevo)
            productos_agregados += 1
    
    print(f"\nProductos nuevos agregados: {productos_agregados}")
    print(f"Productos actualizados: {productos_actualizados}")
    
    return productos_agregados + productos_actualizados