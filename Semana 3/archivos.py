"""
Módulo de archivos para persistencia del inventario.
Contiene funciones para guardar y cargar datos desde archivos CSV.
"""

import csv
import os


def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.
    
    Parametros:
        inventario (list): Lista de diccionarios con productos
        ruta (str): Ruta del archivo CSV donde guardar
        incluir_header (bool): Si True, incluye encabezado en el archivo
    
    Retorna:
        bool: True si se guardo correctamente, False en caso de error
    """
    # Validar que el inventario no este vacio
    if not inventario:
        print("No se puede guardar: el inventario esta vacio.")
        return False
    
    try:
        # Abrir archivo para escritura
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
        print(f"Error: No tienes permisos para escribir en '{ruta}'.")
        return False
    except IOError as e:
        print(f"Error de escritura: {e}")
        return False
    except Exception as e:
        print(f"Error inesperado al guardar: {e}")
        return False


def cargar_csv(ruta):
    """
    Carga productos desde un archivo CSV.
    
    Parametros:
        ruta (str): Ruta del archivo CSV a cargar
    
    Retorna:
        list: Lista de diccionarios con productos cargados (puede estar vacia si hay errores)
    """
    productos_cargados = []
    filas_invalidas = 0
    
    try:
        # Verificar si el archivo existe
        if not os.path.exists(ruta):
            raise FileNotFoundError(f"El archivo '{ruta}' no existe.")
        
        with open(ruta, 'r', newline='', encoding='utf-8') as archivo:
            reader = csv.reader(archivo)
            
            # Leer encabezado
            try:
                header = next(reader)
            except StopIteration:
                print("Error: El archivo esta vacio.")
                return []
            
            # Validar encabezado
            if header != ['nombre', 'precio', 'cantidad']:
                print(f"Error: Encabezado invalido. Se esperaba: nombre,precio,cantidad")
                print(f"   Se encontro: {','.join(header)}")
                return []
            
            # Leer cada fila
            for num_linea, fila in enumerate(reader, start=2):  # start=2 porque línea 1 es header
                # Validar que tenga exactamente 3 columnas
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue
                
                try:
                    nombre = fila[0].strip()
                    precio = float(fila[1])
                    cantidad = int(fila[2])
                    
                    # Validar que precio y cantidad no sean negativos
                    if precio < 0 or cantidad < 0:
                        print(f"Linea {num_linea}: precio o cantidad negativos, omitiendo.")
                        filas_invalidas += 1
                        continue
                    
                    # Validar que el nombre no este vacio
                    if not nombre:
                        print(f"Linea {num_linea}: nombre vacio, omitiendo.")
                        filas_invalidas += 1
                        continue
                    
                    # Agregar producto válido
                    productos_cargados.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                
                except ValueError:
                    print(f"Linea {num_linea}: formato invalido (precio debe ser numero, cantidad debe ser entero), omitiendo.")
                    filas_invalidas += 1
                    continue
        
        # Mostrar resumen
        print(f"\nProductos cargados exitosamente: {len(productos_cargados)}")
        if filas_invalidas > 0:
            print(f"Filas invalidas omitidas: {filas_invalidas}")
        
        return productos_cargados
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return []
    except UnicodeDecodeError:
        print(f"Error: El archivo '{ruta}' no esta en formato UTF-8 o contiene caracteres invalidos.")
        return []
    except Exception as e:
        print(f"Error inesperado al cargar: {e}")
        return []


def fusionar_inventarios(inventario_actual, inventario_nuevo):
    """
    Fusiona dos inventarios. Si un producto existe en ambos, actualiza precio y suma cantidad.
    
    Parametros:
        inventario_actual (list): Inventario existente
        inventario_nuevo (list): Inventario a fusionar
    
    Retorna:
        int: Numero de productos fusionados/agregados
    """
    productos_agregados = 0
    productos_actualizados = 0
    
    for producto_nuevo in inventario_nuevo:
        # Buscar si el producto ya existe
        producto_existente = None
        for producto in inventario_actual:
            if producto["nombre"].lower() == producto_nuevo["nombre"].lower():
                producto_existente = producto
                break
        
        if producto_existente:
            # Actualizar producto existente: sumar cantidad y actualizar precio
            producto_existente["cantidad"] += producto_nuevo["cantidad"]
            producto_existente["precio"] = producto_nuevo["precio"]
            productos_actualizados += 1
        else:
            # Agregar nuevo producto
            inventario_actual.append(producto_nuevo)
            productos_agregados += 1
    
    print(f"\nResumen de fusión:")
    print(f"   - Productos nuevos agregados: {productos_agregados}")
    print(f"   - Productos actualizados: {productos_actualizados}")
    
    return productos_agregados + productos_actualizados
