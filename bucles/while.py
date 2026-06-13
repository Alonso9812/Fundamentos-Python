secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

num = int(input("Ingrese un numero: "))

while num != secret_number:

    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    
    if num < secret_number:
        print("Ingresa un numero mas alto")
    else:
        print("Ingrese un numero mas bajo")

    num = int(input("Ingrese un numero: "))
    
print(num, " ¡Bien hecho, muggle! Eres libre ahora."),