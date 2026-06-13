edad = int(input("Ingrese su edad: "))


if edad >= 0 and edad <= 2:
    print("Es un bebe")
elif edad >= 3 and edad <= 12:
    print("Es un nino")
elif edad >= 13 and edad <= 17:
    print("Es un adolescente")
elif edad >= 18 and edad <= 64:
    print("Es un adulto")
else: print("Adulto mayor")
