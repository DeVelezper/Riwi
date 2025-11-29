
frutas = ["Mango","Banano","Pera","Mora"]
continuar = ""

def ShowFrut(frutas):
    for i, fruta in enumerate(frutas,start=1):
        print(f"{i}.{fruta}")

def Continue ():    
    return input(""" \n
Ingresa (a) para elimiar una fruta de la lsita
Ingresa (x) para terminar de ingresar frutas
Cualquier letra para continuar \n""")


while continuar != "x":
    fruta = input("Ingresa una fruta \n")
    frutas.append(fruta)

    print("\nLista actual:")
    ShowFrut(frutas)

    continuar = Continue()

    if continuar == "a":
        print(f"\nEsta es tu lista de frutas:")
        ShowFrut(frutas)

        eliminar = int(input(f"""\nCual deseas eliminar?\nEscribe el numero de la fruta \n"""))
        print(f"Fruta eliminada ({frutas[eliminar-1]})\n")
        
        frutas.pop(eliminar - 1)
        ShowFrut(frutas)
        continuar = Continue()

    elif continuar == "x":
        break

print(f"\nEsta es tu lista de frutas final:\n")
ShowFrut(frutas)