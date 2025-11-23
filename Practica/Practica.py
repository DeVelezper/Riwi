
numeros = []
def IngresarNum(lista,num):
    lista.append(num)
    return(lista)

while True:
    num = int(input("Ingresa un numero "))
    IngresarNum(numeros,num)
    orden = numeros.sort()
    desoreden = numeros.sort(reverse = True)
    print(orden,desoreden)
    salir = input("Ingrese x para salor ")
    if salir == "x":
        break