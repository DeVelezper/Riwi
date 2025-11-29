opciones = ["Suma", "Resta", "Multiplicación", "División"]
print("Seleccione la operación que desea realizar:\n")

while True:
    for i, opcion in enumerate(opciones, start= 1):
        print(f"{i}. {opcion}")

    try:
        eleccion = int(input("\nIngrese el número de la operación (1-4): "))
        if eleccion > 0 and eleccion < 5:
            break

    except ValueError:
        print("Debe ingresar un numero del (1-4)\n")

while True:
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if eleccion == 4 and num2 == 0:
            print("No puedes Dividir entre 0 \n")
            continue
        break
    except ValueError:
        print("Debes ingresar un numero correcto")

if eleccion == 1:
    resultado = num1 + num2
    operacion = "Suma"

elif eleccion == 2:    
    resultado = num1 - num2
    peracion = "Resta"


elif eleccion == 3:
    resultado = num1 * num2
    operacion = "Multiplicación"

elif eleccion == 4:
    resultado = num1 / num2 
    operacion = "División"

print(f"El resultadio de tu {operacion} es {resultado}")
