acumulado = 0
suma = 0
num = int(input("Ingrese un numero:"))

acumulado = num + acumulado

while acumulado > 0:
    num = int(input("Ingrese un numero:"))
    if num >= 0:
      acumulado = num + acumulado
    else:
       break
print("El resultado es:", acumulado)