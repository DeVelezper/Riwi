def saludo(nombre = "Usuario", edad = 0):
    return f"Hola {nombre}, tienes {edad} años"

print("\nHola bienvenido!\n")
nombre = input("Ingresa tu nombre: ") or "Usuario"

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        break
    except ValueError:
        
        print(f"Hola {nombre}, ingresaste una edad incorrecta.\n"
            "Vuelve a ingresar una edad verdadera.\n")


print(saludo(nombre, edad))