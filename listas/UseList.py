#usando una lista 

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)): 
    total += my_list[i] # Sumar cada elemento de la lista a total

print(total)

#lista en accion
my_list = [10, 1, 8, 3, 5]
 
my_list[0], my_list[4] = my_list[4], my_list[0] #Intercambiar el primer y último elemento
my_list[1], my_list[3] = my_list[3], my_list[1] #Intercambiar el segundo y penúltimo elemento
 
print(my_list)

#lista en accion con 100 elementos
my_list = [10, 1, 8, 3, 5]
length = len(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
print(my_list)

my_list = [10, 1, 14, 8, 20, 3, 5]
length = len(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
print(my_list)