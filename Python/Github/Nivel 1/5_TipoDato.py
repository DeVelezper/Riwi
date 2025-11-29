
dato = input("Ingrese un dato ")

if dato.lower() == "true" or dato.lower() == "false":
    dato = dato.lower() == "true"
elif dato.isdigit():
    dato = int(dato)
else:
    try:
        dato = float(dato)
    except ValueError:
        pass

print("El valor ingresado es:", dato)
print(f"El tipo de dato es: {type(dato)}")
