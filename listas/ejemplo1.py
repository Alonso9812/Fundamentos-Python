numbers = [10, 5, 7, 2, 1]
print("elementos", numbers)

#cambiar el valor de un elemento de la lista 
numbers [0] = 111
print("elementos", numbers)

# copiar el valor del quinto elemento al segundo elemento
numbers [1] = numbers [4]
print("elementos", numbers)

#accediendo al tercer elemenro de la lista
print(numbers[3])

print("La longitud de la lista es: ", len(numbers))

for i in range(3):
    print(numbers[i])

print(numbers[4])
numbers[4] = 1

del numbers[1]  # Eliminando el segundo elemento de la lista.
print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

