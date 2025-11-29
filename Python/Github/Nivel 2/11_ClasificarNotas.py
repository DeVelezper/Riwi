listaNotas = []

def Imprimir():
    print("\nTus notas son:\n")
    for i, nota in enumerate(listaNotas, start=1):
        print(f"Nota {i}: {nota}")
    print()
    return

def CalcularPromedio():
    if len(listaNotas) == 0:
        print("No hay notas registradas.\n")
        return

    promedio = sum(listaNotas) / len(listaNotas)

    if promedio >= 90:
        resultado = "Excelente"
    elif promedio >= 60:
        resultado = "Aprobado"
    else:
        resultado = "Reprobado"

    Imprimir()
    print(f"Tu promedio es: {promedio:.2f}")
    print(f"Clasificación: {resultado}\n")
    return

while True:
    nota = float(input("Ingresa una nota (0 a 100):\n"))
    listaNotas.append(nota)

    opcion = int(input("""
¿Qué deseas hacer?
1. Ingresar otra nota
2. Imprimir notas
3. Calcular clasificación
4. Salir
--> """))

    if opcion == 1:
        continue
    elif opcion == 2:
        Imprimir()
    elif opcion == 3:
        CalcularPromedio()
    elif opcion == 4:
        print("\nSaliendo del programa...")
        break
    else:
        print("Opción inválida, intenta nuevamente.\n")
