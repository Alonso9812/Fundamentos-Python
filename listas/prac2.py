# remover numeros duplicados y mostrar la lista resultante
list1 = [1, 2, 3, 1, 4, 3, 5]
list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)

print(list2)


# Suma de extremos de una lista

numeros = [10, 20, 30, 40, 50]
if len(numeros) == 0:
    print("La lista está vacía.")
else:
    suma = numeros[0] + numeros[-1]
    print("La suma de los extremos es:", suma)


#copiar lista

colors = ['rojo', 'verde', 'naranja']
 
copy_whole_colors = colors[:]  # copia la lista entera
copy_part_colors = colors[0:2]  # copia parte de la lista

sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # output: ['C', 'D']

