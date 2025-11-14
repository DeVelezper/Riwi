
frutas = []
continuar = ""

while continuar != "x":
    fruta = input("Ingresa una fruta \n")
    frutas.append(fruta)
    continuar = input("Ingresa x para terminar de ingresar frutas \n")
    if continuar == "x":
        break

print(f"\nEsta es tu lista de frutas {frutas}")