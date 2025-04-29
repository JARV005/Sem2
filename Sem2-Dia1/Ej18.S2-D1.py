#insert para agregar a lista con posicion y dato
Lista=[2,5,6,7,53]
print("Lista ",Lista)
num=int(input("Ingrese un número que desee agregar "))
pos=int(input("¿En que posicion? (0 a 4) "))
Lista.insert(pos,num)
print("Nueva lista ", Lista)
