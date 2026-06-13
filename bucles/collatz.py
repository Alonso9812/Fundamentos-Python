
def collatz_sequence(c0):
    if c0 <= 0:
        print("El número debe ser un entero positivo.")
        return
    
    steps = 0
    while c0 != 1:
        print(c0, end=" -> ")  # Mostrar los valores intermedios
        if c0 % 2 == 0:
            c0 //= 2
        else:
            c0 = 3 * c0 + 1
        steps += 1
    
    print(1)  # Mostrar el último valor de la secuencia
    print(f"Número de pasos: {steps}")

# Pedir al usuario un número natural
try:
    num = int(input("Ingresa un número natural: "))
    collatz_sequence(num)
except ValueError:
    print("Debes ingresar un número entero válido.")


