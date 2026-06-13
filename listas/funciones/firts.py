def message(number):
    print("Ingresa un número:", number)

message(1)

def message(number):
    print("Ingresa un número:", number)

number = 1234
message(1)
print(number)

def message(what, number, age):
    print("Ingresa", what, "número", number, "edad", age)

message("el primer", 1, 14)
message("el segundo", 2, 22)
message("el tercer", 3, 25)

def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)


def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

def address(street, city, postal_code):
    print("Tu dirección es:", street,"St.,", city, postal_code)

s = input("Calle: ")
p_c = input("Código Postal: ")
c = input("Ciudad: ")
address(s, c, p_c)

#Ejemplo 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # salida: 3
subtra(2, 5)    # salida: -3


#Ejemplo 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # salida: 3
subtra(b=2, a=5)    # salida: 3

#Ex. 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # salida: 3
subtra(5, 2)    # salida: 3

def name(first_name, last_name="Pérez"):
    print(first_name, last_name)

name("Andy")    # salida: Andy Pérez
name("Bety", "Rodríguez")    # salida: Bety Rodríguez (el argumento de palabra clave es reemplazado por "Rodríguez")

