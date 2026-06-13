print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?")

#ingresar datos 
anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)

#valor de los catetos
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)

#suma de string 
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")

# el * cuando es aplicado a un string replica el stringe "an * 3 = ananan"
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#convertir numeros a una cadena con str
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))

#LAB
a = float(input("Ingresa el primer valor: "))
b = float(input("Ingresa el segundo valor: "))
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("\n¡Eso es todo, amigos!")

#LAB
x = float(input("Ingresa el valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)



