nums = []

def PedirNum ():
    i = len(nums) + 1
    num = int(input(f"Ingresa el numero {i} "))
    nums.append(num)
    return i

def Comparador ():
    print(f"El número mayor es: {max(nums)}")
    print(f"El número mayor es: {min(nums)}")

while True:
    i = PedirNum()
    if i == 3:
        break

print("lista: ",nums)
Comparador()