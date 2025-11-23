# 🛒 Sistema de Gestión de Tienda de Electrónica

Sistema integral de gestión de inventario y ventas para una tienda de productos electrónicos desarrollado en Python con menú interactivo completo.

---

## 📋 Descripción del Proyecto

Sistema completo de gestión comercial que permite administrar el inventario de productos electrónicos, procesar ventas con descuentos según tipo de cliente, y generar reportes analíticos detallados del desempeño del negocio.

**Características principales:**
- ✅ Gestión completa de inventario (CRUD)
- ✅ Sistema de ventas con descuentos por tipo de cliente
- ✅ Generación de reportes y análisis de rendimiento
- ✅ Validaciones exhaustivas de datos
- ✅ Interfaz de usuario intuitiva con emojis
- ✅ Sistema de caché para optimizar reportes

---

## 🎯 Funcionalidades del Sistema

### 📦 GESTIÓN DE INVENTARIO

#### 1. Agregar Producto
Registra nuevos productos en el inventario con:
- ID único del producto
- Nombre, marca y categoría
- Precio unitario
- Stock disponible
- Meses de garantía

**Validaciones:**
- ID único (no duplicados)
- Campos obligatorios no vacíos
- Precio mayor a cero
- Stock no negativo
- Garantía no negativa

#### 2. Ver Todos los Productos
Muestra tabla formateada con:
- ID, nombre, marca, categoría
- Precio, stock disponible, garantía
- Total de productos en inventario
- Valor total del inventario

#### 3. Actualizar Producto
Modifica información de productos existentes:
- Búsqueda por ID
- Opción de mantener valores actuales (Enter)
- Validación de nuevos valores
- Confirmación de actualización

#### 4. Eliminar Producto
Elimina productos del inventario:
- Búsqueda por ID
- Muestra información completa antes de eliminar
- Confirmación explícita requerida (SI)
- Opción de cancelar operación

### 💳 GESTIÓN DE VENTAS

#### 5. Registrar Venta
Procesa ventas completas con:
- Datos del cliente
- Selección de tipo de cliente (4 tipos)
- Selección de producto
- Cantidad a vender
- Validación de stock disponible
- Cálculo automático de descuentos
- Actualización automática de inventario
- Ticket detallado de venta

**Tipos de Cliente y Descuentos:**
| Tipo        | Descuento |
|-------------|-----------|
| Regular     | 0%        |
| Miembro     | 5%        |
| VIP         | 10%       |
| Corporativo | 15%       |

#### 6. Ver Historial de Ventas
Muestra tabla con todas las ventas:
- Fecha y hora
- Cliente y tipo
- Producto vendido
- Cantidad
- Total de la venta
- Total de ventas registradas
- Ingresos totales generados

### 📊 REPORTES Y ANÁLISIS

#### 7. Top 3 Productos Más Vendidos
Ranking de productos por unidades vendidas:
- Posición en el ranking
- Nombre y marca del producto
- Unidades vendidas
- Ingresos generados
- Participación porcentual sobre el total

#### 8. Ventas por Marca
Reporte consolidado por marca:
- Unidades vendidas por marca
- Ingresos generados por marca
- Porcentaje de participación
- Ordenado por ingresos (mayor a menor)
- Totales generales

#### 9. Reporte Financiero
Análisis financiero completo:

**Métricas Generales:**
- Total de transacciones
- Ingreso bruto
- Total descuentos aplicados
- Ingreso neto
- Ticket promedio
- Tasa de descuento efectiva

**Análisis por Tipo de Cliente:**
- Número de transacciones
- Ingresos generados
- Descuentos otorgados
- Ticket promedio por tipo

#### 10. Rendimiento del Inventario
Evaluación detallada del inventario:

**Productos con Actividad:**
- Stock actual vs vendidos
- Ingresos generados
- Estado del stock (Agotado/Bajo/Normal/Óptimo)

**Productos sin Ventas:**
- Inventario estancado
- Valor inmovilizado
- Recomendaciones

**Análisis de Rotación:**
- Productos de alta rotación (necesitan reabastecimiento)
- Productos de baja rotación (exceso de inventario)
- Sugerencias de cantidad a reabastecer

---

## 📊 Estructura de Datos

### Producto
```python
{
    'id': str,          # Ej: "PROD001"
    'nombre': str,      # Ej: "Mouse Gamer Inalámbrico"
    'marca': str,       # Ej: "Logitech"
    'categoria': str,   # Ej: "Periféricos"
    'precio': float,    # Ej: 79.99
    'stock': int,       # Ej: 45
    'garantia': int     # Ej: 24 (meses)
}
```

### Venta
```python
{
    'fecha': str,              # "2025-11-22 14:30:15"
    'cliente': str,            # "Juan Pérez"
    'tipo_cliente': str,       # "vip"
    'id_producto': str,        # "PROD001"
    'nombre_producto': str,    # "Mouse Gamer"
    'marca': str,              # "Logitech"
    'cantidad': int,           # 2
    'precio_unitario': float,  # 79.99
    'subtotal': float,         # 159.98
    'tasa_descuento': float,   # 0.10
    'monto_descuento': float,  # 15.99
    'total': float             # 143.99
}
```

---

## 📦 Productos Precargados

El sistema se inicializa con 5 productos:

1. **Mouse Gamer Inalámbrico** - Logitech
   - Categoría: Periféricos | Precio: $79.99 | Stock: 45 | Garantía: 24 meses

2. **Teclado Mecánico RGB** - Razer
   - Categoría: Periféricos | Precio: $149.99 | Stock: 30 | Garantía: 12 meses

3. **Monitor 27" 4K** - Samsung
   - Categoría: Pantallas | Precio: $449.99 | Stock: 20 | Garantía: 36 meses

4. **Hub USB-C 7 en 1** - Anker
   - Categoría: Accesorios | Precio: $59.99 | Stock: 60 | Garantía: 18 meses

5. **Audífonos Inalámbricos** - Sony
   - Categoría: Audio | Precio: $199.99 | Stock: 35 | Garantía: 24 meses

---

## 🛠️ Tecnologías y Librerías

**Lenguaje:** Python 3.7+

**Librerías estándar:**
- `datetime`: Registro de fecha y hora de ventas
- `typing`: Type hints (Dict, List, Optional, Tuple)

**No requiere instalación de paquetes externos**

---

## 🚀 Instalación y Ejecución

### Opción 1: Ejecución directa
```bash
python tienda_de_electronica.py
```

### Opción 2: Desde cualquier directorio
```bash
cd C:\Users\USUARIO\Desktop\Riwi\Simulacro
python tienda_de_electronica.py
```

### Requisitos del Sistema
- Python 3.7 o superior instalado
- Windows, Linux o macOS
- Terminal o línea de comandos

---

## 💻 Uso del Sistema

### Navegación por Menú
El sistema presenta un menú numerado con 11 opciones (0-10):

```
📦 GESTIÓN DE INVENTARIO
   1. Agregar Producto
   2. Ver Todos los Productos
   3. Actualizar Producto
   4. Eliminar Producto

💳 GESTIÓN DE VENTAS
   5. Registrar Venta
   6. Ver Historial de Ventas

📊 REPORTES Y ANÁLISIS
   7. Top 3 Productos Más Vendidos
   8. Ventas por Marca
   9. Reporte Financiero
   10. Rendimiento del Inventario

⚙️ SISTEMA
   0. Salir del Sistema
```

### Ejemplo de Flujo Completo

**1. Ver productos disponibles:**
```
Seleccione opción: 2
→ Muestra tabla con los 5 productos precargados
```

**2. Registrar una venta:**
```
Seleccione opción: 5
→ Nombre del Cliente: Carlos Gómez
→ Tipo de Cliente: vip
→ ID del Producto: PROD001
→ Cantidad a vender: 2
✓ Venta registrada - Total: $143.99 (10% descuento aplicado)
```

**3. Ver reportes:**
```
Seleccione opción: 9
→ Muestra reporte financiero completo con métricas
```

---

## 🎓 Conceptos de Programación Implementados

### Estructuras de Datos
- **Diccionarios:** Almacenamiento de inventario y caché
- **Listas:** Historial de ventas
- **Tuplas:** Retorno múltiple de funciones

### Programación Funcional
- **Funciones puras:** validar_producto()
- **Lambda functions:** Ordenamiento y cálculos
- **Map:** Agregación de datos
- **Filter y Sort:** Procesamiento de reportes

### Type Hints
- Anotaciones de tipos en todas las funciones
- Mejora legibilidad y mantenibilidad
- Facilita debugging

### Manejo de Errores
- Try-except en todas las operaciones críticas
- Validación de tipos de datos
- Mensajes de error descriptivos
- Manejo de KeyboardInterrupt (Ctrl+C)

### Optimización
- **Sistema de caché:** Evita recalcular reportes
- **Invalidación automática:** Al registrar ventas
- **Un solo recorrido:** Para múltiples agregaciones

---

## ✨ Características Especiales

### 🎨 Interfaz de Usuario
- Emojis para mejor UX (✓, ❌, 📦, 💰, 📊)
- Tablas formateadas con alineación
- Separadores visuales
- Mensajes claros y descriptivos

### 🔒 Validaciones Robustas
- IDs únicos de productos
- Valores numéricos válidos
- Stock suficiente para ventas
- Tipo de cliente válido
- Confirmaciones para acciones críticas

### 📈 Análisis Avanzado
- Cálculo de participación porcentual
- Ticket promedio por tipo de cliente
- Identificación de inventario estancado
- Sugerencias de reabastecimiento
- Detección de exceso de stock

### 🛡️ Manejo de Excepciones
- Captura de errores de tipo
- Manejo de interrupciones
- Mensajes informativos
- Continuidad del programa

---

## 📝 Validaciones del Sistema

| Validación | Descripción |
|------------|-------------|
| ✅ ID único | No permite productos duplicados |
| ✅ Campos obligatorios | Nombre, marca, categoría no vacíos |
| ✅ Precios positivos | Mayor a cero |
| ✅ Stock válido | No negativo |
| ✅ Garantía válida | No negativa |
| ✅ Stock disponible | Suficiente para la venta |
| ✅ Tipo de cliente | Solo los 4 tipos permitidos |
| ✅ Cantidad de venta | Mayor a cero |

---

## 📈 Posibles Mejoras Futuras

### Funcionalidades
- [ ] Búsqueda de productos por nombre o categoría
- [ ] Edición múltiple de productos
- [ ] Devoluciones y reembolsos
- [ ] Sistema de proveedores
- [ ] Alertas de stock mínimo
- [ ] Gestión de múltiples sucursales

### Persistencia de Datos
- [ ] Guardar inventario en JSON
- [ ] Exportar ventas a CSV/Excel
- [ ] Base de datos SQLite
- [ ] Backup automático

### Interfaz
- [ ] Interfaz gráfica con Tkinter/PyQt
- [ ] Versión web con Flask/Django
- [ ] Generación de PDF para reportes
- [ ] Gráficos con matplotlib

### Seguridad
- [ ] Sistema de autenticación
- [ ] Roles de usuario (admin, vendedor)
- [ ] Log de auditoría
- [ ] Encriptación de datos sensibles

---

## 🏗️ Arquitectura del Código

### Módulos Principales

**1. Estructuras de Datos Globales**
- inventario: Dict con todos los productos
- historial_ventas: List con todas las ventas
- cache_reportes: Dict para optimización

**2. Gestión de Inventario**
- inicializar_inventario()
- validar_producto()
- agregar_producto()
- ver_productos()
- actualizar_producto()
- eliminar_producto()

**3. Gestión de Ventas**
- invalidar_cache_reportes()
- calcular_descuento()
- registrar_venta()
- ver_historial_ventas()

**4. Reportes y Análisis**
- generar_datos_reportes()
- top_productos_mas_vendidos()
- ventas_por_marca()
- reporte_financiero()
- rendimiento_inventario()

**5. Menú y Navegación**
- mostrar_menu()
- limpiar_pantalla()
- pausar()
- main()

---

## 👨‍💻 Información del Proyecto

**Curso:** Fundamentos de Programación con Python (M1)  
**Institución:** Riwi  
**Tipo:** Simulacro de práctica  
**Versión:** 2.0 Optimizada  
**Año:** 2025

---

## 📄 Licencia

Este proyecto es de uso **educativo** y fue desarrollado como parte del programa de formación en programación.

---

## 🎯 Objetivo de Aprendizaje

Este proyecto demuestra el dominio de:
- Estructuras de datos complejas
- Funciones y modularización
- Validación de datos
- Manejo de excepciones
- Programación funcional (lambda, map, filter)
- Type hints y documentación
- Diseño de interfaces de usuario en consola
- Optimización de código (caché)
- Lógica de negocio aplicada

---

## 🤝 Contribuciones

Este es un proyecto educativo. Para sugerencias o mejoras, contactar al instructor del curso.

---

**¡Sistema listo para usar! 🚀**
