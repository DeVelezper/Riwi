# Escriba un programa que escriba los numeros de 1 al  100
# Si es divisible por 3 print fizz
# Si es de 5 bozz
# Si es divisible por los dos imprimir fizz bozz
# Otro caso el numero
fizz = []
bozz = []
fizzBozz = []
OtroCaso = []

# def mod(i,num):
#     mod = i % num
#     return mod

for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        fizzBozz.append(i)
        # print("fizz bozz")
    if i % 3 == 0:
        fizz.append(i)    
        # print("fizz")
    if i % 5 == 0:
        bozz.append(i)
        # print("bozz")
    else:
        OtroCaso.append(i)

print(f"Numeros fizz {fizz}\n")
print(f"Numeros bozz {bozz}\n")
print(f"Numeros fizz & bozz {fizzBozz}\n")
print(f"Numeros bozz {OtroCaso}\n")
