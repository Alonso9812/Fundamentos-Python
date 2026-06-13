#Agregar elementos a la lista

# Agregar un elemento al final de la lista
hat_list = [1, 2, 3, 4, 5]
hat_list.append(6)
print("Lista después de agregar un elemento:", hat_list)
# Agregar un elemento en una posición específica
hat_list.insert(2, 10)
print("Lista después de agregar un elemento en una posición específica:", hat_list) 
# Extender la lista con otra lista
hat_list.extend([7, 8, 9])
print("Lista después de extenderla con otra lista:", hat_list)


my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1) # Agregando elementos a la lista y suma 1 a cada elemento.

print(my_list) 


my_list = []  

for i in range(5):
    my_list.insert(0, i + 1)  # Agregando elementos al inicio de la lista y suma 1 a cada elemento.

print(my_list)
