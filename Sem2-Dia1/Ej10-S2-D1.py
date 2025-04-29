Edad=int(input("Ingrese su edad"))

if Edad<12:
  print("Niño")
elif Edad>=12 and Edad<18:
    print("Adolescente")
elif Edad>=18 and Edad<60:
    print("Adulto")
elif Edad>=60:
    print("Anciano")
