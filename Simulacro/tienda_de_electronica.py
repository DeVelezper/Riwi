
#   Sistema Integral de Gestión de Inventario y Ventas para Tienda de Electrónica
#   ==============================================================================
#   Módulo: Fundamentos de programación con Python (M1)
#    Versión: 2.0 Optimizada


from datetime import datetime

# ============================================================================
# ESTRUCTURAS DE DATOS GLOBALES
# ============================================================================

inventario = {}
historial_ventas = []

# Sistema de caché para optimizar generación de reportes
# Se invalida automáticamente cuando se registra una nueva venta
cache_reportes = {
    'valido': False,
    'datos': {}
}

DESCUENTOS_CLIENTE = {
    'regular': 0.0,
    'miembro': 0.05,
    'vip': 0.10,
    'corporativo': 0.15
}


# ============================================================================
# FUNCIONES HELPER
# ============================================================================

def mostrar_encabezado(titulo, ancho=60):
    print("\n" + "="*ancho)
    print(titulo)
    print("="*ancho)

def mostrar_error(mensaje, detalle=""):
    print(f" Error: {mensaje}")
    if detalle:
        print(f"   {detalle}")

def mostrar_exito(mensaje):
    print(f"✓ {mensaje}")

def mostrar_mensaje_vacio(tipo, sugerencia=""):
    mostrar_encabezado(f"❌ NO HAY {tipo.upper()}")
    if sugerencia:
        print(f"Sugerencia: {sugerencia}")

def mostrar_tabla(headers, rows, ancho=110):
    print("\n" + "="*ancho)
    print(" ".join(headers))
    print("="*ancho)
    for row in rows:
        print(" ".join(str(item) for item in row))
    print("="*ancho)

def mostrar_info_producto(producto):
    print(f"""
📦 Producto seleccionado: {producto['nombre']}
   Precio unitario: ${producto['precio']:.2f}
   Stock disponible: {producto['stock']} unidades""")

def mostrar_ticket_venta(venta_info):
    mostrar_encabezado("✓ ¡VENTA REGISTRADA EXITOSAMENTE!")
    print(f"""
Cliente: {venta_info['cliente']} ({venta_info['tipo'].capitalize()})
Producto: {venta_info['producto']}
Cantidad: {venta_info['cantidad']} unidades × ${venta_info['precio_unitario']:.2f}
{'-' * 60}
Subtotal: ${venta_info['subtotal']:.2f}
Descuento ({venta_info['descuento_pct']:.0f}%): -${venta_info['descuento']:.2f}
{'=' * 60}
TOTAL A PAGAR: ${venta_info['total']:.2f}
{'=' * 60}
Stock restante: {venta_info['stock_restante']} unidades
{'=' * 60}""")

def solicitar_datos_producto():
    return {
        'nombre': input("Nombre del Producto: ").strip(),
        'marca': input("Marca: ").strip(),
        'categoria': input("Categoría: ").strip()
    }

def solicitar_valores_numericos():
    precio = float(input("Precio Unitario ($): "))
    stock = int(input("Cantidad en Stock: "))
    garantia = int(input("Garantía (meses): "))
    return precio, stock, garantia


# ============================================================================
# FUNCIONES DE INICIALIZACIÓN
# ============================================================================

def inicializar_inventario():
    productos_precargados = [
        {
            'id': 'PROD001',
            'nombre': 'Mouse Gamer Inalámbrico',
            'marca': 'Logitech',
            'categoria': 'Periféricos',
            'precio': 79.99,
            'stock': 45,
            'garantia': 24
        },
        {
            'id': 'PROD002',
            'nombre': 'Teclado Mecánico RGB',
            'marca': 'Razer',
            'categoria': 'Periféricos',
            'precio': 149.99,
            'stock': 30,
            'garantia': 12
        },
        {
            'id': 'PROD003',
            'nombre': 'Monitor 27" 4K',
            'marca': 'Samsung',
            'categoria': 'Pantallas',
            'precio': 449.99,
            'stock': 20,
            'garantia': 36
        },
        {
            'id': 'PROD004',
            'nombre': 'Hub USB-C 7 en 1',
            'marca': 'Anker',
            'categoria': 'Accesorios',
            'precio': 59.99,
            'stock': 60,
            'garantia': 18
        },
        {
            'id': 'PROD005',
            'nombre': 'Audífonos Inalámbricos',
            'marca': 'Sony',
            'categoria': 'Audio',
            'precio': 199.99,
            'stock': 35,
            'garantia': 24
        }
    ]
    
    for producto in productos_precargados:
        inventario[producto['id']] = producto
    
    mostrar_exito("Inventario inicializado con 5 productos precargados")


# ============================================================================
# MÓDULO: GESTIÓN DE INVENTARIO
# ============================================================================

def validar_producto(nombre, marca, categoria, precio, stock, garantia):
    if not nombre or not nombre.strip():
        return False, "El nombre del producto no puede estar vacío"
    
    if not marca or not marca.strip():
        return False, "La marca no puede estar vacía"
    
    if not categoria or not categoria.strip():
        return False, "La categoría no puede estar vacía"
    
    if precio <= 0:
        return False, "El precio debe ser mayor a cero"
    
    if stock < 0:
        return False, "El stock no puede ser negativo"
    
    if garantia < 0:
        return False, "La garantía no puede ser negativa"
    
    return True, ""


def agregar_producto():
    try:
        mostrar_encabezado("AGREGAR NUEVO PRODUCTO AL INVENTARIO")
        
        id_producto = input("ID del Producto (ej: PROD006): ").strip().upper()
        
        if id_producto in inventario:
            mostrar_error("¡El ID del producto ya existe!", 
                        f"Producto existente: {inventario[id_producto]['nombre']}")
            return
        
        if not id_producto:
            mostrar_error("El ID no puede estar vacío")
            return
        
        datos = solicitar_datos_producto()
        
        try:
            precio, stock, garantia = solicitar_valores_numericos()
        except ValueError:
            mostrar_error("Los valores numéricos deben ser válidos",
                        "Precio: número decimal, Stock y Garantía: números enteros")
            return
        
        es_valido, mensaje_error = validar_producto(
            datos['nombre'], datos['marca'], datos['categoria'], precio, stock, garantia
        )
        
        if not es_valido:
            mostrar_error(f"Validación: {mensaje_error}")
            return
        
        inventario[id_producto] = {
            'id': id_producto,
            **datos,
            'precio': precio,
            'stock': stock,
            'garantia': garantia
        }
        
        mostrar_encabezado("✓ ¡PRODUCTO AGREGADO EXITOSAMENTE!")
        print(f"ID: {id_producto} | Nombre: {datos['nombre']} | Precio: ${precio:.2f} | Stock: {stock}")
        print("="*60)
        
    except KeyboardInterrupt:
        print("\n Operación cancelada por el usuario")
    except Exception as e:
        mostrar_error(f"Inesperado al agregar producto: {e}")


def ver_productos():
    if not inventario:
        mostrar_mensaje_vacio("PRODUCTOS EN EL INVENTARIO", 
                            "Use la opción 1 para agregar productos")
        return
    
    print("\n" + "="*110)
    print(f"{'ID':<12} {'NOMBRE':<28} {'MARCA':<15} {'CATEGORÍA':<15} {'PRECIO':<12} {'STOCK':<10} {'GARANTÍA'}")
    print("="*110)
    
    for prod in inventario.values():
        print(f"{prod['id']:<12} {prod['nombre']:<28} {prod['marca']:<15} "
            f"{prod['categoria']:<15} ${prod['precio']:<11.2f} "
            f"{prod['stock']:<10} {prod['garantia']} meses")
    
    valor_total = sum(p['precio'] * p['stock'] for p in inventario.values())
    print("="*110)
    print(f"Total: {len(inventario)} productos | Valor inventario: ${valor_total:,.2f}")
    print("="*110)


def actualizar_producto():
    try:
        mostrar_encabezado("ACTUALIZAR PRODUCTO EXISTENTE")
        
        id_producto = input("Ingrese el ID del Producto a actualizar: ").strip().upper()
        
        if id_producto not in inventario:
            mostrar_error(f"No existe un producto con ID '{id_producto}'")
            return
        
        producto = inventario[id_producto]
        
        print(f"""
📦 Actualizando: {producto['nombre']}
{'-' * 60}
Instrucciones: Presione Enter para mantener el valor actual
{'-' * 60}""")
        
        campos = ['nombre', 'marca', 'categoria']
        valores = {campo: input(f"{campo.capitalize()} [{producto[campo]}]: ").strip() or producto[campo] 
                for campo in campos}
        
        try:
            precio = float(input(f"Precio [${producto['precio']}]: ").strip() or producto['precio'])
            stock = int(input(f"Stock [{producto['stock']}]: ").strip() or producto['stock'])
            garantia = int(input(f"Garantía [{producto['garantia']} meses]: ").strip() or producto['garantia'])
        except ValueError:
            mostrar_error("Los valores numéricos deben ser válidos")
            return
        
        es_valido, mensaje_error = validar_producto(
            valores['nombre'], valores['marca'], valores['categoria'], precio, stock, garantia
        )
        
        if not es_valido:
            mostrar_error(f"Validación: {mensaje_error}")
            return
        
        producto.update({**valores, 'precio': precio, 'stock': stock, 'garantia': garantia})
        mostrar_encabezado("✓ ¡PRODUCTO ACTUALIZADO EXITOSAMENTE!")
        
    except KeyboardInterrupt:
        print("\n Operación cancelada por el usuario")
    except Exception as e:
        mostrar_error(f"Inesperado al actualizar producto: {e}")


def eliminar_producto():
    try:
        mostrar_encabezado("ELIMINAR PRODUCTO DEL INVENTARIO")
        print(" ADVERTENCIA: Esta acción no se puede deshacer\n" + "="*60)
        
        id_producto = input("Ingrese el ID del Producto a eliminar: ").strip().upper()
        
        if id_producto not in inventario:
            mostrar_error(f"No existe un producto con ID '{id_producto}'")
            return
        
        p = inventario[id_producto]
        print(f"\n {p['nombre']} | {p['marca']} | Stock: {p['stock']} | Valor: ${p['precio'] * p['stock']:.2f}")
        
        if input("\n¿Eliminar este producto? (SI/no): ").strip().upper() == 'SI':
            del inventario[id_producto]
            mostrar_exito("¡Producto eliminado exitosamente!")
        else:
            print("❌ Eliminación cancelada")
            
    except KeyboardInterrupt:
        print("\n Operación cancelada por el usuario")
    except Exception as e:
        mostrar_error(f"Inesperado al eliminar producto: {e}")


# ============================================================================
# MÓDULO: GESTIÓN DE VENTAS
# ============================================================================

def invalidar_cache_reportes():
    cache_reportes['valido'] = False
    cache_reportes['datos'] = {}


def calcular_descuento(subtotal, tipo_cliente):
    tasa_descuento = DESCUENTOS_CLIENTE.get(tipo_cliente, 0.0)
    monto_descuento = subtotal * tasa_descuento
    return tasa_descuento, monto_descuento


def registrar_venta():
    try:
        mostrar_encabezado("REGISTRAR NUEVA VENTA")
        
        cliente = input("Nombre del Cliente: ").strip()
        if not cliente:
            mostrar_error("El nombre del cliente no puede estar vacío")
            return
        
        print("\n Tipos de cliente:")
        for tipo, desc in DESCUENTOS_CLIENTE.items():
            print(f"   • {tipo.capitalize()}: {desc*100:.0f}%")
        
        tipo_cliente = input("\nTipo de Cliente: ").strip().lower()
        if tipo_cliente not in DESCUENTOS_CLIENTE:
            mostrar_error("Tipo inválido", f"Válidos: {', '.join(DESCUENTOS_CLIENTE.keys())}")
            return
        
        id_producto = input("ID del Producto: ").strip().upper()
        if id_producto not in inventario:
            mostrar_error(f"Producto '{id_producto}' no existe")
            return
        
        producto = inventario[id_producto]
        mostrar_info_producto(producto)
        
        try:
            cantidad = int(input("\nCantidad a vender: "))
        except ValueError:
            mostrar_error("La cantidad debe ser un entero")
            return
        
        if cantidad <= 0:
            mostrar_error("La cantidad debe ser mayor a cero")
            return
        
        if cantidad > producto['stock']:
            mostrar_error("Stock insuficiente",
                        f"Disponible: {producto['stock']} | Solicitado: {cantidad}")
            return
        
        precio_unitario = producto['precio']
        subtotal = precio_unitario * cantidad
        tasa_descuento, monto_descuento = calcular_descuento(subtotal, tipo_cliente)
        total = subtotal - monto_descuento
        
        producto['stock'] -= cantidad
        
        venta = {
            'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'cliente': cliente,
            'tipo_cliente': tipo_cliente,
            'id_producto': id_producto,
            'nombre_producto': producto['nombre'],
            'marca': producto['marca'],
            'cantidad': cantidad,
            'precio_unitario': precio_unitario,
            'subtotal': subtotal,
            'tasa_descuento': tasa_descuento,
            'monto_descuento': monto_descuento,
            'total': total
        }
        
        historial_ventas.append(venta)
        invalidar_cache_reportes()
        
        mostrar_ticket_venta({
            'cliente': cliente,
            'tipo': tipo_cliente,
            'producto': producto['nombre'],
            'cantidad': cantidad,
            'precio_unitario': precio_unitario,
            'subtotal': subtotal,
            'descuento': monto_descuento,
            'descuento_pct': tasa_descuento * 100,
            'total': total,
            'stock_restante': producto['stock']
        })
        
    except KeyboardInterrupt:
        print("\n Operación cancelada")
    except Exception as e:
        mostrar_error(f"Error: {e}")


def ver_historial_ventas():
    if not historial_ventas:
        mostrar_mensaje_vacio("VENTAS REGISTRADAS", "Use la opción 5 para registrar ventas")
        return
    
    print("\n" + "="*130)
    print(f"{'FECHA':<20} {'CLIENTE':<20} {'TIPO':<12} {'PRODUCTO':<28} {'CANT':<6} {'TOTAL':<12}")
    print("="*130)
    
    for v in historial_ventas:
        print(f"{v['fecha']:<20} {v['cliente']:<20} {v['tipo_cliente']:<12} "
            f"{v['nombre_producto']:<28} {v['cantidad']:<6} ${v['total']:<11.2f}")
    
    total_ingresos = sum(map(lambda v: v['total'], historial_ventas))
    print("="*130)
    print(f"Total: {len(historial_ventas)} ventas | Ingresos: ${total_ingresos:,.2f}")
    print("="*130)


# ============================================================================
# MÓDULO: REPORTES Y ANÁLISIS
# ============================================================================

def generar_datos_reportes():
    if cache_reportes['valido']:
        return cache_reportes['datos']
    
    ventas_por_producto = {}
    ventas_por_marca = {}
    subtotal_total = 0.0
    descuentos_totales = 0.0
    ingresos_netos = 0.0
    
    # Agregar todos los datos en un solo recorrido para mayor eficiencia
    for venta in historial_ventas:
        pid = venta['id_producto']
        marca = venta['marca']
        
        # Agregar estadísticas por producto
        if pid not in ventas_por_producto:
            ventas_por_producto[pid] = {
                'nombre': venta['nombre_producto'],
                'marca': marca,
                'cantidad': 0,
                'ingresos': 0.0
            }
        ventas_por_producto[pid]['cantidad'] += venta['cantidad']
        ventas_por_producto[pid]['ingresos'] += venta['total']
        
        # Agregar estadísticas por marca
        if marca not in ventas_por_marca:
            ventas_por_marca[marca] = {
                'unidades': 0,
                'ingresos': 0.0
            }
        ventas_por_marca[marca]['unidades'] += venta['cantidad']
        ventas_por_marca[marca]['ingresos'] += venta['total']
        
        # Acumular totales financieros
        subtotal_total += venta['subtotal']
        descuentos_totales += venta['monto_descuento']
        ingresos_netos += venta['total']
    
    datos = {
        'ventas_por_producto': ventas_por_producto,
        'ventas_por_marca': ventas_por_marca,
        'totales_financieros': {
            'subtotal': subtotal_total,
            'descuentos': descuentos_totales,
            'neto': ingresos_netos,
            'num_transacciones': len(historial_ventas)
        }
    }
    
    cache_reportes['datos'] = datos
    cache_reportes['valido'] = True
    
    return datos


def top_productos_mas_vendidos():
    if not historial_ventas:
        mostrar_mensaje_vacio("DATOS DE VENTAS DISPONIBLES")
        return
    
    datos = generar_datos_reportes()
    productos = sorted(datos['ventas_por_producto'].items(), 
                    key=lambda x: x[1]['cantidad'], reverse=True)
    
    print("\n" + "="*70)
    print(" TOP 3 PRODUCTOS MÁS VENDIDOS")
    print("="*70)
    
    total_unidades = sum(p[1]['cantidad'] for p in productos)
    
    for i, (_, d) in enumerate(productos[:3], 1):
        pct = (d['cantidad'] / total_unidades) * 100
        print(f"""
{i}. {d['nombre']} ({d['marca']})
Vendidos: {d['cantidad']} | Ingresos: ${d['ingresos']:,.2f} | Participación: {pct:.1f}%""")
    
    print("\n" + "="*70)


def ventas_por_marca():
    if not historial_ventas:
        mostrar_mensaje_vacio("DATOS DE VENTAS DISPONIBLES")
        return
    
    datos = generar_datos_reportes()
    marcas = sorted(datos['ventas_por_marca'].items(), 
                key=lambda x: x[1]['ingresos'], reverse=True)
    
    print("\n" + "="*70)
    print(" REPORTE DE VENTAS POR MARCA")
    print("="*70)
    print(f"{'MARCA':<20} {'UNIDADES':<15} {'INGRESOS':<20} {'%'}")
    print("-" * 70)
    
    total_ing = sum(m[1]['ingresos'] for m in marcas)
    
    for marca, s in marcas:
        pct = (s['ingresos'] / total_ing) * 100 if total_ing > 0 else 0
        print(f"{marca:<20} {s['unidades']:<15} ${s['ingresos']:<19,.2f} {pct:>5.1f}%")
    
    print("="*70)
    print(f"TOTAL: {sum(m[1]['unidades'] for m in marcas)} unidades | ${total_ing:,.2f}")
    print("="*70)


def reporte_financiero():
    if not historial_ventas:
        mostrar_mensaje_vacio("DATOS DE VENTAS DISPONIBLES")
        return
    
    datos = generar_datos_reportes()
    f = datos['totales_financieros']
    
    mostrar_encabezado(" REPORTE FINANCIERO CONSOLIDADO", 70)
    
    ticket_prom = f['neto'] / f['num_transacciones']
    tasa_desc = (f['descuentos'] / f['subtotal']) * 100
    
    print(f"\n Métricas: {f['num_transacciones']} transacciones | Ticket promedio: ${ticket_prom:.2f}")
    print(f"Bruto: ${f['subtotal']:,.2f} | Descuentos: -${f['descuentos']:,.2f} ({tasa_desc:.1f}%)")
    print(f"{'='*70}")
    print(f"NETO: ${f['neto']:,.2f}")
    print(f"{'='*70}")
    
    print(f"\n👥 Por Tipo de Cliente:")
    
    ventas_tipo = {}
    for v in historial_ventas:
        t = v['tipo_cliente']
        if t not in ventas_tipo:
            ventas_tipo[t] = {'cant': 0, 'ing': 0.0, 'desc': 0.0}
        ventas_tipo[t]['cant'] += 1
        ventas_tipo[t]['ing'] += v['total']
        ventas_tipo[t]['desc'] += v['monto_descuento']
    
    for tipo, s in sorted(ventas_tipo.items(), key=lambda x: x[1]['ing'], reverse=True):
        ticket = s['ing'] / s['cant']
        print(f"   {tipo.upper():<12}: {s['cant']:>3} ventas | ${s['ing']:>10,.2f} | "
            f"Desc: ${s['desc']:>8,.2f} | Ticket: ${ticket:.2f}")
    
    print("="*70)


def rendimiento_inventario():
    if not historial_ventas:
        mostrar_mensaje_vacio("DATOS DE VENTAS DISPONIBLES",
                            "Registre algunas ventas para generar este reporte")
        return
    
    datos = generar_datos_reportes()
    vpp = datos['ventas_por_producto']
    
    print("\n" + "="*100)
    print(" REPORTE DE RENDIMIENTO DEL INVENTARIO")
    print("="*100)
    print("\n PRODUCTOS CON VENTAS")
    print("-" * 100)
    print(f"{'PRODUCTO':<30} {'MARCA':<15} {'STOCK':<10} {'VENDIDOS':<12} {'INGRESOS':<15} {'ESTADO'}")
    print("-" * 100)
    
    for pid, s in vpp.items():
        if pid in inventario:
            p = inventario[pid]
            est = "🔴 AGOTADO" if p['stock'] == 0 else "🟡 BAJO" if p['stock'] < 10 else "🟢 NORMAL" if p['stock'] < 20 else "🟢 ÓPTIMO"
            print(f"{s['nombre']:<30} {s['marca']:<15} {p['stock']:<10} "
                f"{s['cantidad']:<12} ${s['ingresos']:<14,.2f} {est}")
    
    print("\n" + "-" * 100)
    print("\n  PRODUCTOS SIN VENTAS")
    print("-" * 100)
    
    sin_ventas = [p for p in inventario.values() if p['id'] not in vpp]
    
    if sin_ventas:
        print(f"{'PRODUCTO':<30} {'MARCA':<15} {'STOCK':<10} {'VALOR'}")
        print("-" * 100)
        valor_est = sum(p['precio'] * p['stock'] for p in sin_ventas)
        for p in sin_ventas:
            print(f"{p['nombre']:<30} {p['marca']:<15} {p['stock']:<10} ${p['precio'] * p['stock']:,.2f}")
        print("-" * 100)
        print(f"Total: {len(sin_ventas)} productos | Valor estancado: ${valor_est:,.2f}")
        print(" Considere estrategias de promoción")
    else:
        print(" Todos los productos tienen ventas")
    
    print("\n" + "="*100)
    print("\n ROTACIÓN")
    print("-" * 100)
    
    alta = [(pid, s) for pid, s in vpp.items() 
            if pid in inventario and s['cantidad'] > inventario[pid]['stock']]
    
    if alta:
        print("\n ALTA ROTACIÓN (reabastecer):")
        for pid, s in sorted(alta, key=lambda x: x[1]['cantidad'], reverse=True):
            p = inventario[pid]
            print(f"   • {s['nombre']}: Stock {p['stock']} | Vendidos {s['cantidad']} "
                f"| Reabastecer: {s['cantidad'] - p['stock']} unidades")
    else:
        print(" No hay necesidad urgente de reabastecimiento")
    
    baja = [(pid, s) for pid, s in vpp.items() 
            if pid in inventario and inventario[pid]['stock'] > s['cantidad'] * 3]
    
    if baja:
        print("\n BAJA ROTACIÓN (exceso):")
        for pid, s in baja:
            p = inventario[pid]
            print(f"   • {s['nombre']}: Stock {p['stock']} | Vendidos {s['cantidad']} "
                  f"| Exceso: {p['stock'] - (s['cantidad'] * 2)} unidades")
    
    print("\n" + "="*100)


# ============================================================================
# MÓDULO: MENÚ Y NAVEGACIÓN
# ============================================================================

def mostrar_menu():
    print(f"""
{'=' * 70}
🏪 SISTEMA DE GESTIÓN DE INVENTARIO Y VENTAS - ELECTRÓNICA
{'=' * 70}

📦 GESTIÓN DE INVENTARIO
   1.  Agregar Producto
   2.  Ver Todos los Productos
   3.  Actualizar Producto
   4.  Eliminar Producto

💳 GESTIÓN DE VENTAS
   5.  Registrar Venta
   6.  Ver Historial de Ventas

📊 REPORTES Y ANÁLISIS
   7.  Top 3 Productos Más Vendidos
   8.  Ventas por Marca
   9.  Reporte Financiero
   10. Rendimiento del Inventario

⚙️  SISTEMA
   0.  Salir del Sistema

{'=' * 70}""")


def limpiar_pantalla():
    print("\n" * 2)


def pausar():
    input("\n Presione Enter para continuar...")


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    mostrar_encabezado(" INICIANDO SISTEMA DE GESTIÓN DE INVENTARIO Y VENTAS", 70)
    
    inicializar_inventario()
    
    print("""
✅ Sistema inicializado correctamente
💡 Tip: Todas las operaciones incluyen validaciones exhaustivas""")
    
    pausar()
    
    # Diccionario de opciones del menú
    opciones_menu = {
        '1': agregar_producto,
        '2': ver_productos,
        '3': actualizar_producto,
        '4': eliminar_producto,
        '5': registrar_venta,
        '6': ver_historial_ventas,
        '7': top_productos_mas_vendidos,
        '8': ventas_por_marca,
        '9': reporte_financiero,
        '10': rendimiento_inventario
    }
    
    while True:
        try:
            limpiar_pantalla()
            mostrar_menu()
            
            opcion = input(" Seleccione una opción (0-10): ").strip()
            
            if opcion in opciones_menu:
                opciones_menu[opcion]()
                pausar()
                
            elif opcion == '0':
                mostrar_encabezado("👋 CERRANDO SISTEMA", 70)
                stats = f"""
✅ Sesión finalizada correctamente
📊 Estadísticas de la sesión:
   • Productos en inventario: {len(inventario)}
   • Ventas registradas: {len(historial_ventas)}"""
                
                if historial_ventas:
                    total_ingresos = sum(map(lambda v: v['total'], historial_ventas))
                    stats += f"\n   • Ingresos totales: ${total_ingresos:,.2f}"
                
                print(stats)
                print(f"\n¡Gracias por usar el sistema! 🎉\n{'=' * 70}\n")
                break
                
            else:
                mostrar_error("Opción inválida. Seleccione un número entre 0 y 10")
                pausar()
        
        except KeyboardInterrupt:
            mostrar_encabezado("⚠️  INTERRUPCIÓN DETECTADA", 70)
            print("""El programa fue interrumpido por el usuario (Ctrl+C)""")
            
            confirmar = input("\n¿Desea salir del sistema? (si/no): ").strip().lower()
            if confirmar == 'si':
                print("\n👋 Saliendo del sistema...")
                break
            else:
                print("\n✅ Continuando con la ejecución normal")
                pausar()
                
        except Exception as e:
            mostrar_encabezado("❌ ERROR INESPERADO", 70)
            print(f"""
Se ha producido un error inesperado: {e}

💡 El programa continuará ejecutándose.
   Si el problema persiste, contacte al administrador.""")
            pausar()


# ============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================================

if __name__ == "__main__":
    main()