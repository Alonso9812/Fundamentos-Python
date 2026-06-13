year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
    #  Escribe el bloque if-elif-elif-else aquí.
	if year % 4 != 0:
		print("El año es común")
	elif year % 100 != 0:
		print("El año es bisiesto")
	elif year % 400 != 0:
		print("El año es común")
	else:
		print("El año es bisiesto")