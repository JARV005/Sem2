Lista=["Naranja", "Pera", "Manzana","Sandia","Mango"]

print("Lista de frutas:", Lista)

Elim=input("Ingrese la fruta que desea eliminar ")

if Elim in Lista:
    Lista.remove(Elim)
    print(Lista)
