n = int(input("ingresa un numero: "))
print(n >= 100)


num1 = int(input("ingresa un numero: "))
num2 = int(input("ingresa un numero: "))
num3 = int(input("ingresa un numero: "))

large_num = num1

if num2 > large_num:
    large_num = num2

if num3 > large_num:
    large_num = num3
    
print("el numero mas grande es: ", large_num) 

num1 = int(input("ingresa un numero: "))
num2 = int(input("ingresa un numero: "))
num3 = int(input("ingresa un numero: "))

large_num = max(num1, num2, num3)

print("el numero mas grande es: ", large_num)