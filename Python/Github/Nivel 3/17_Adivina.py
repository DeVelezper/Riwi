import random
repeticion = int(input("Ingrese la cantida de repeticiones "))

while repeticion > 0:
    num = int(input("\nAdivina el numero del 1 al 10 "))
    aleatorio = random.randint(1,10)
    if num == aleatorio:
        print(f"El numero es {aleatorio} Ganaste! ")
        break
    else:
        print(f"El numero es {aleatorio} Perdiste!")
    repeticion -= 1