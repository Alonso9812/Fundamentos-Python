blocks = int(input("Ingrese el numero de bloques:"))

capaActual = 1
blockUse = 0
altura = 0

while blockUse + capaActual <= blocks:
    blockUse += capaActual
    capaActual += 1
    altura += 1

print("la altura es de: ", altura)