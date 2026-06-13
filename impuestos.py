#version aprendiz
income = float(input("Introduce el ingreso anual: "))

exc = 85528
resto = income - exc 

if income < 85528:
	tax = income * 0.18 - 556.02
elif income > 85528:
	tax = 14839.02 + resto * 0.32
else:
	tax = 0.0
		
tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
 

# version PRO
income = float(input("Introduce el ingreso anual: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
	tax = (income - 85528) * 0.32 + 14839.02

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")