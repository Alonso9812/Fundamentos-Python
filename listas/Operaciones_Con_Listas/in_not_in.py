# Verificar si un elemento está en la lista
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

#################################

# Encontrar el numero mayor en la lista
num = [0, 3, 12, 8, 2]
mayor = num[0]

for i in range(1, len(num)):
    if num[i] > mayor:
        mayor = num[i]
print("El número mayor es:", mayor)

# encontrar un elemento en la lista

elementos = [15, 8, 10, 3, 5, 7]
num = 37
done = False

for i in range(len(elementos)):
    done = elementos[i] == num
    if done:
        break

if done:
    print("El número", num, "se encuentra en la lista.")
else:
    print("El número", num, "no se encuentra en la lista.")    

# verificar mas de un elemento en diferentes listas
listas = [1, 2, 3, 4, 5, 9, 25]
mynum = [8, 3, 17, 8, 25, 10, 9]
fav = 0

for i in listas:
    if i in mynum:
        fav += 1

print("Hay", fav, "números favoritos en la lista.")  # Resultado: Hay 3 números favoritos en la lista.


# imprimir los numeros ganadores
listas = [1, 2, 3, 4, 5, 9, 25]
mynum = [8, 3, 17, 8, 25, 10, 9]
fav = []

for i in listas:
    if i in mynum:
        fav.append(i)
    
if fav:
    print("Los numeros favorecidos son: ", fav)
else:
    print("No has ganado nada")

