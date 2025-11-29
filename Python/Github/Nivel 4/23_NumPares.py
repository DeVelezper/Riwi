
pares = []
inpares = []

num = int(input("ingresa un numero "))
if num  % 2 == 2:
    pares.append(num)
else:
    inpares.append(num)

print(f"Pares {pares}, Impares {inpares}")