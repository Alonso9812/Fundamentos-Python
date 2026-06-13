# Millas y kilometros

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

################################################################################

#convertidor de divisas
dolars = 10
colones = 1000

dolar_to_colones = dolars * 511.41
colones_to_dolar = colones / 511.41

#round redondea la salida al número de decimales especificados

print(dolars, "dolars son: ", round(dolar_to_colones, 2), "colones")
print(colones, "colones son: ", round(colones_to_dolar, 2), "dolars")

##################################################################################


x =  -1
x = float(x)
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
print("y =", y)