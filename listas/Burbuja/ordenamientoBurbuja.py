my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

# Ordenador burbuja version interactiva
lista = []
swapped = True
num = int(input("Ingrese la cantidad de elementos: "))

for i in range(num):
    val = float(input("Ingrese el elemento "))
    lista.append(val)

while swapped:
    swapped = False
    for i in range(len(lista) - 1):
        if lista [i] > lista [i + 1]:
            swapped = True
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print("n\Lista ordenada:")
print(lista)
# Ordenamiento burbuja  interactivo                

#De una manera mas sencilla
mylist = []
swapped = True
num = int(input("Ingrese la cantidad de elementos: "))

for i in range(num):
    value = int(input("Ingrese el elemento "))
    mylist.append(value)

mylist.sort()  # Utilizando el método sort para ordenar la lista
print(mylist)
# tambien puede utilizar reverse para invertir la lista