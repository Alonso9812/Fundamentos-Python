nota = int(input("Ingrese la nota: "))

if  nota < 60:
    print("reprobado")
elif nota >= 60 and nota <= 79:
    print("aprobado")
elif nota >= 80 and nota <= 89:
    print("buena calificacion")
elif nota >= 90 and nota <= 100:
    print("exelente")