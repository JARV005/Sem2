# Determinar estado de aprobación de una sola calificación
while True:
    try:
        Calificacion = float(input("Ingrese una calificación para saber si aprueba (0 a 100): "))
        if Calificacion < 0 or Calificacion > 100:
            print("Ingrese una calificación entre 0 y 100")
        elif Calificacion >= 50:
            print("Aprobado")
            break
        else:
            print("Reprobado")
            break
    except ValueError:
        print("Ingrese un valor numérico.")

# Lista de calificaciones
ListaC = []

# Menú principal
while True:
    print("\n   Menú    ")
    print("1. Agregar lista de notas")
    print("2. Promedio de calificaciones en lista")
    print("3. Contar cuántas notas hay mayores a una nota a ingresar")
    print("4. Contar cuántas veces está una nota")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == '1':
        calificaciones = input("Ingresa las calificaciones separadas por comas (0-100): ")
        for C in calificaciones.split(','):
            try:
                calificacion = float(C.strip())
                if calificacion >= 0 and calificacion <= 100:
                    ListaC.append(calificacion)
                else:
                    print(f"La calificación {calificacion} no es válida. Debe estar entre 0 y 100.")
            except ValueError:
                print(f"{C} no es un número válido.")
        print(f"Lista actualizada: {ListaC}")

    elif opcion == '2':
        if len(ListaC) == 0:
            print("La lista está vacía.")
        else:
            suma = sum(ListaC)
            cantidad = len(ListaC)
            promedio = suma / cantidad
            print(f"Promedio calificaciones en lista: {promedio:.2f}")

    elif opcion == '3':
        if len(ListaC) == 0:
            print("La lista está vacía.")
        else:
            try:
                valor = float(input("Ingrese una nota para comparar (entre 0 y 100): "))
                if valor < 0 or valor > 100:
                    print("Valor fuera de rango.")
                else:
                    cont = 0
                    mayores = []
                    for C in ListaC:
                        if C > valor:
                            mayores.append(C)
                            cont += 1
                    print(f"Las calificaciones mayores a {valor} son: {mayores} (Total: {cont})")
            except ValueError:
                print("Ingrese un número válido.")

    elif opcion == '4':
        if len(ListaC) == 0:
            print("La lista está vacía.")
        else:
            try:
                buscar = float(input("Ingrese una calificación a buscar (entre 0 y 100): "))
                if buscar < 0 or buscar > 100:
                    print("Valor fuera de rango.")
                else:
                    contador = 0
                    for C in ListaC:
                        if C == buscar:
                            contador += 1
                    print(f"La calificación {buscar} está {contador} veces en la lista.")
            except ValueError:
                print("Ingrese un número válido.")

    elif opcion == '5':
        print("Saliendo del programa")
        break

    else:
        print("Opción no válida. Por favor elija entre 1 y 5.")
