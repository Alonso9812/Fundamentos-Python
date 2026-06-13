dia = str(input("Ingrese el dia (lun, mar, mie, jue, vie, sab, dom): ")).lower() # lower permite minusculas y mayusculas
hora = int(input("Ingrese la hora: "))


if (dia in ["lun", "mar", "mie", "jue", "vie"]) and (6 <= hora <= 21):
    print("tarifa regular")
# Tarifa nocturna: días laborales entre las 22 y las 23 horas
elif (dia in ["lun", "mar", "mie", "jue", "vie"]) and (22 <= hora <= 23):
    print("tarifa nocturna")
# Tarifa reducida: fines de semana o fuera del rango anterior
else:
    print("tarifa reducida")