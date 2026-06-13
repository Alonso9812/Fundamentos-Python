numeros = [10, 25, 87, 52, 63]

mayor = numeros[0]
mayor2 = numeros[0]


for num in numeros[1:]:
    if num > mayor:
        mayor2 = mayor
        mayor = num
    elif num > mayor2 and num != mayor:
        mayor2 = num
 
print("El mayor es:", mayor)
print("El segundo mayor es:", mayor2)


#contar elementos repetidos
elementos = [1, 2, 3, 4, 5, 1, 2, 3]
buscar = 1
contador = 0

for i in elementos:
    if i == buscar:
        contador +=1

print(f"El elemento {buscar} se repite {contador} veces en la lista.")


