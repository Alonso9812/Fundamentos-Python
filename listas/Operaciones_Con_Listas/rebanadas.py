list_1 = [1]
list_2 = list_1[:] # Los dos puntos crean una copia superficial de list_1
list_1[0] = 2
print(list_2)

# Copiando la lista completa.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

