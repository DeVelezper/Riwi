# Sistema de Gestión de Inventario Avanzado - Semana 3

Sistema completo de gestión de inventario con persistencia en archivos CSV, operaciones CRUD y estadísticas avanzadas.

## Descripción

Este proyecto implementa un sistema modular de gestión de inventario que permite:
- Realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre productos
- Calcular estadísticas del inventario (valor total, productos destacados, etc.)
- Guardar y cargar inventarios desde archivos CSV
- Fusionar inventarios existentes con datos importados
- Validaciones completas y manejo robusto de errores

## Estructura del Proyecto

```
Semana 3/
├── app.py                    # Archivo principal con menú interactivo
├── servicios.py             # Módulo con funciones CRUD y estadísticas
├── archivos.py              # Módulo de persistencia (CSV)
├── inventario_ejemplo.csv   # Archivo CSV de ejemplo
└── README.md                # Documentación del proyecto
```

## Cómo Ejecutar

1. Asegúrate de tener Python 3.x instalado
2. Navega a la carpeta del proyecto:
   ```bash
   cd "Semana 3"
   ```
3. Ejecuta el programa:
   ```bash
   python app.py
   ```

## Uso del Sistema

### Menú Principal

El sistema presenta 9 opciones:

1. **Agregar producto**: Añade un nuevo producto al inventario
2. **Mostrar inventario**: Muestra todos los productos en formato tabular
3. **Buscar producto**: Busca un producto específico por nombre
4. **Actualizar producto**: Modifica precio y/o cantidad de un producto
5. **Eliminar producto**: Elimina un producto del inventario (con confirmación)
6. **Ver estadísticas**: Muestra estadísticas del inventario
7. **Guardar inventario en CSV**: Exporta el inventario a un archivo CSV
8. **Cargar inventario desde CSV**: Importa productos desde un archivo CSV
9. **Salir**: Cierra el programa

### Formato de Datos

Cada producto contiene:
- **nombre** (str): Nombre del producto
- **precio** (float): Precio unitario (no negativo)
- **cantidad** (int): Cantidad en stock (no negativa)

### Formato CSV

Los archivos CSV deben seguir este formato:
```csv
nombre,precio,cantidad
Producto 1,99.99,10
Producto 2,49.50,25
```

## Funcionalidades Detalladas

### 1. Operaciones CRUD

#### Agregar Producto
- Solicita nombre, precio y cantidad
- Valida que precio y cantidad sean no negativos
- Verifica que el producto no exista previamente

#### Mostrar Inventario
- Despliega todos los productos en formato tabular
- Muestra subtotal por producto (precio × cantidad)
- Usa funciones lambda para cálculos

#### Buscar Producto
- Búsqueda por nombre (case-insensitive)
- Muestra información detallada del producto encontrado

#### Actualizar Producto
- Permite actualizar precio y/o cantidad
- Muestra valores actuales antes de actualizar
- Permite omitir campos (dejar en blanco para mantener)

#### Eliminar Producto
- Solicita confirmación antes de eliminar
- Valida que el producto exista

### 2. Estadísticas del Inventario

Calcula y muestra:
- **Unidades totales**: Suma de todas las cantidades
- **Valor total**: Suma de (precio × cantidad) de todos los productos
- **Producto más caro**: Producto con mayor precio unitario
- **Producto con mayor stock**: Producto con mayor cantidad

### 3. Persistencia en CSV

#### Guardar CSV
- Valida que el inventario no esté vacío
- Incluye encabezado: `nombre,precio,cantidad`
- Maneja errores de permisos y escritura
- Muestra mensaje de confirmación con ruta

#### Cargar CSV
- Valida formato del archivo y encabezado
- Verifica que cada fila tenga 3 columnas
- Valida tipos de datos (float para precio, int para cantidad)
- Valida que valores no sean negativos
- Omite filas inválidas y reporta cuántas se omitieron
- Maneja errores: FileNotFoundError, UnicodeDecodeError, ValueError

#### Fusionar Inventarios
Cuando se carga un CSV con inventario existente:
- **Opción Sobrescribir (S)**: Reemplaza completamente el inventario actual
- **Opción Fusionar (N)**: 
  - Si el producto existe: suma la cantidad y actualiza el precio
  - Si el producto no existe: lo agrega
  - Muestra resumen de productos agregados/actualizados

## Validaciones Implementadas

### Validaciones de Entrada
- Opciones de menú: solo números del 1-9
- Precio: debe ser número no negativo
- Cantidad: debe ser entero no negativo
- Nombre: no puede estar vacío

### Validaciones de Archivos CSV
- Archivo debe existir
- Encabezado debe ser exactamente: `nombre,precio,cantidad`
- Cada fila debe tener 3 columnas
- Precio debe ser número válido no negativo
- Cantidad debe ser entero válido no negativo
- Nombre no puede estar vacío

### Manejo de Errores
- FileNotFoundError: archivo no encontrado
- PermissionError: sin permisos de escritura
- UnicodeDecodeError: problemas de codificación
- ValueError: conversión de tipos inválida
- KeyboardInterrupt: interrupción del usuario (Ctrl+C)
- Exception genérica: cualquier error inesperado

**Nota importante**: Ningún error cierra la aplicación; todos se capturan y muestran mensajes descriptivos.

## Módulos y Funciones

### `servicios.py`

- `agregar_producto(inventario, nombre, precio, cantidad)` → bool
- `mostrar_inventario(inventario)` → None
- `buscar_producto(inventario, nombre)` → dict | None
- `actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)` → bool
- `eliminar_producto(inventario, nombre)` → bool
- `calcular_estadisticas(inventario)` → dict
- `mostrar_estadisticas(inventario)` → None

### `archivos.py`

- `guardar_csv(inventario, ruta, incluir_header)` → bool
- `cargar_csv(ruta)` → list
- `fusionar_inventarios(inventario_actual, inventario_nuevo)` → int

### `app.py`

- `mostrar_menu()` → None
- `obtener_opcion()` → int | None
- `solicitar_producto()` → tuple | None
- `opcion_agregar(inventario)` → None
- `opcion_mostrar(inventario)` → None
- `opcion_buscar(inventario)` → None
- `opcion_actualizar(inventario)` → None
- `opcion_eliminar(inventario)` → None
- `opcion_estadisticas(inventario)` → None
- `opcion_guardar(inventario)` → None
- `opcion_cargar(inventario)` → None
- `main()` → None

## Criterios de Aceptación Cumplidos

**Persistencia**
- Se puede guardar inventario en CSV con encabezado correcto
- Se puede cargar CSV válido con opción de sobrescribir o fusionar
- Sistema maneja archivos corruptos sin cerrarse y reporta filas omitidas

**Colecciones y modularidad**
- Inventario usa lista de diccionarios con claves: nombre, precio, cantidad
- Código modularizado en 3 archivos: app.py, servicios.py, archivos.py
- Funciones CRUD, estadísticas y archivos con docstrings completos

**Estadísticas**
- Calcula correctamente: unidades_totales, valor_total, producto_mas_caro, producto_mayor_stock
- Usa lambda para calcular subtotales

**Interfaz por consola**
- Menú funcional con opciones 1-9
- Mensajes claros para todos los casos (éxito, error, vacío, no encontrado, etc.)

**Calidad**
- Código legible con nombres descriptivos
- Manejo de excepciones con try/except en todas las operaciones críticas
- Comentarios y documentación completa

## Ejemplo de Uso

### Probar con archivo de ejemplo

1. Ejecuta el programa: `python app.py`
2. Selecciona opción `8` (Cargar inventario)
3. Ingresa: `inventario_ejemplo.csv`
4. Selecciona `S` para cargar los datos de ejemplo
5. Selecciona opción `2` (Mostrar inventario) para ver los productos
6. Selecciona opción `6` (Ver estadísticas) para ver las métricas

### Crear tu propio inventario

1. Ejecuta el programa
2. Usa opción `1` para agregar productos manualmente
3. Usa opción `7` para guardar en un nuevo archivo CSV
- El archivo se guardará en la carpeta actual

## Características de Seguridad

- No se permiten valores negativos en precio o cantidad
- Confirmación antes de eliminar productos
- Validación exhaustiva de archivos CSV
- Manejo robusto de errores sin cerrar la aplicación
- Mensajes descriptivos para guiar al usuario

## Autor

Proyecto desarrollado para Riwi - Semana 3
Historia de usuario: Inventario avanzado con colecciones y persistencia en archivos

## Notas

- Todos los archivos CSV se guardan/cargan en la carpeta actual
- El sistema usa codificación UTF-8 para soportar caracteres especiales
- Los nombres de productos no distinguen mayúsculas/minúsculas en búsquedas
- La fusión de inventarios suma cantidades y actualiza precios al nuevo valor
