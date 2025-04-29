Lista=[]

for x in range(5):
    num=int(input(f"Ingrese el numero {x+1}: "))
    if num%2==0:
        Lista.append(num)

print("Numeros pares: ", Lista)