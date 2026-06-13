import random
import os
import time

class TicTacToe:
    def __init__(self):
        # Tablero de 1 a 9
        self.board = [" "] * 10  
        self.WIN_POS = [
            (1,2,3), (4,5,6), (7,8,9),
            (1,4,7), (2,5,8), (3,6,9),
            (1,5,9), (3,5,7)
        ]
        # Primer movimiento de la máquina
        self.board[5] = "X"

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def print_header(self):
        print("======================================")
        print("        TIC TAC TOE - MODERNO         ")
        print("======================================")
        print("   Máquina: X      Tú: O              ")
        print("--------------------------------------")

    def print_board(self):
        # Muestra el tablero siempre numerado
        def slot(i):
            return self.board[i] if self.board[i] != " " else str(i)

        print(f"""
         {slot(1)} | {slot(2)} | {slot(3)} 
        ---+---+---
         {slot(4)} | {slot(5)} | {slot(6)} 
        ---+---+---
         {slot(7)} | {slot(8)} | {slot(9)} 
        """)

    def check_winner(self, player):
        return any(self.board[a] == self.board[b] == self.board[c] == player
                   for a, b, c in self.WIN_POS)

    def board_full(self):
        return all(self.board[i] != " " for i in range(1, 10))

    def player_move(self):
        while True:
            try:
                move = int(input("Tu turno (1-9): "))

                if not 1 <= move <= 9:
                    print("⛔ Número fuera de rango. Intenta de nuevo.")
                    continue

                if self.board[move] != " ":
                    print("⛔ Esa casilla ya está ocupada.")
                    continue

                self.board[move] = "O"
                break

            except ValueError:
                print("⛔ Entrada inválida, debes ingresar un número.")

    def machine_move(self):
        free = [i for i in range(1, 10) if self.board[i] == " "]
        move = random.choice(free)
        print(f"\n🤖 La máquina está pensando...")
        time.sleep(0.8)
        print(f"🤖 La máquina jugó en la casilla {move}")
        self.board[move] = "X"

    def game_loop(self):
        while True:
            self.clear()
            self.print_header()
            self.print_board()

            # ✔ Movimiento del usuario
            self.player_move()

            if self.check_winner("O"):
                self.clear()
                self.print_header()
                self.print_board()
                print("🎉 ¡GANASTE! 😎🔥")
                break

            if self.board_full():
                self.clear()
                self.print_header()
                self.print_board()
                print("😐 Empate... buena partida.")
                break

            # ✔ Movimiento de la máquina
            self.machine_move()

            if self.check_winner("X"):
                self.clear()
                self.print_header()
                self.print_board()
                print("💀 La máquina gana… suerte para la próxima.")
                break


if __name__ == "__main__":
    game = TicTacToe()
    game.game_loop()
