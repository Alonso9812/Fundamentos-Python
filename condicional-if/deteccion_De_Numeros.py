num = int(input("ingresa el numero: "))

if num > 0:
    print("positivo")
elif num < 0:
    print("Negativo")
else:
    print("cero")

if num % 2 == 0:
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")