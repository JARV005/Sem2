Lista=[2,5,6,7,53,8,3,321,58,34,24,1,9,]

N=int(input("Ingrese el número a buscar "))

if N in Lista:
    pos=Lista.index(N)
    print(f"El número {N} está en la posición {pos} ")
else:
    print(f"El número {N} no está en la lista")