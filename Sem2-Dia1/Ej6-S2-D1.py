H=int(input("Ingrese la hora (0-23) "))

if H<12 or H>18:
    print("No es hora de trabajar")
else:
    print("Es hora de trabajar")
