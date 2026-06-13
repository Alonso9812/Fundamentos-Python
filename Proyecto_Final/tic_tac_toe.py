import random

# Tablero inicial numerado del 1 al 9
board = [' '] * 10  # ignoramos el índice 0 para facilidad

# Posiciones ganadoras
WIN_POS = [
    (1,2,3), (4,5,6), (7,8,9),   # filas
    (1,4,7), (2,5,8), (3,6,9),   # columnas
    (1,5,9), (3,5,7)             # diagonales
]

def print_board():
    print(f"""
     {board[1]} | {board[2]} | {board[3]} 
    ---+---+---
     {board[4]} | {board[5]} | {board[6]} 
    ---+---+---
     {board[7]} | {board[8]} | {board[9]} 
    """)

def check_winner(player):
    for a, b, c in WIN_POS:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def board_full():
    return all(board[i] != ' ' for i in range(1, 10))

def machine_move():
    free = [i for i in range(1, 9+1) if board[i] == ' ']
    return random.choice(free)

# --- INICIO DEL JUEGO ---
print("Bienvenido al Tic Tac Toe")
print("La máquina juega con X y tú con O.\n")

# Primer movimiento: máquina en el centro
board[5] = 'X'

while True:
    print_board()

    # Movimiento del usuario
    while True:
        try:
            move = int(input("Tu turno (1-9): "))

            if move < 1 or move > 9:
                print("Número fuera de rango. Intenta de nuevo.")
                continue

            if board[move] != ' ':
                print("Esa casilla ya está ocupada. Elige otra.")
                continue

            board[move] = 'O'
            break
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")

    # Verificar si el usuario ganó
    if check_winner('O'):
        print_board()
        print("¡Felicidades! Ganaste 😎")
        break

    if board_full():
        print_board()
        print("Empate 😐")
        break

    # Movimiento de la máquina (random)
    m = machine_move()
    board[m] = 'X'
    print(f"La máquina juega en la casilla {m}")

    # Verificar si la máquina ganó
    if check_winner('X'):
        print_board()
        print("La máquina gana 🤖💀")
        break

    if board_full():
        print_board()
        print("Empate 😐")
        break
