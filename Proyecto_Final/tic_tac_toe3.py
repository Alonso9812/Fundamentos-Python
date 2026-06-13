import tkinter as tk
import random

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Moderno")
        self.root.resizable(False, False)

        self.buttons = {}
        self.board = [" "] * 10  # de 1 a 9
        self.WIN_POS = [
            (1,2,3), (4,5,6), (7,8,9),
            (1,4,7), (2,5,8), (3,6,9),
            (1,5,9), (3,5,7)
        ]

        self.frame = tk.Frame(self.root, bg="#222222")
        self.frame.pack(padx=20, pady=20)

        self.status = tk.Label(self.root, text="Tu turno (O)", 
                               font=("Arial", 16), fg="white", bg="#222222")
        self.status.pack(pady=10)

        self.create_board()

        # Primer movimiento de la máquina
        self.machine_first_move()

    def create_board(self):
        for i in range(1, 10):
            btn = tk.Button(self.frame, text=" ", font=("Arial", 32, "bold"),
                            width=3, height=1, bg="#333333", fg="white",
                            command=lambda i=i: self.player_move(i))
            self.buttons[i] = btn
            row = (i - 1) // 3
            col = (i - 1) % 3
            btn.grid(row=row, column=col, padx=5, pady=5)

    def machine_first_move(self):
        self.board[5] = "X"
        self.buttons[5]["text"] = "X"
        self.buttons[5]["fg"] = "#ff5555"

    def player_move(self, pos):
        if self.board[pos] != " ":
            return

        self.board[pos] = "O"
        self.buttons[pos]["text"] = "O"
        self.buttons[pos]["fg"] = "#55aaff"

        if self.check_winner("O"):
            self.end_game("GANASTE 😎🔥")
            return

        if self.board_full():
            self.end_game("EMPATE 😐")
            return

        self.root.after(300, self.machine_move)

    def machine_move(self):
        free = [i for i in range(1, 10) if self.board[i] == " "]
        pos = random.choice(free)

        self.board[pos] = "X"
        self.buttons[pos]["text"] = "X"
        self.buttons[pos]["fg"] = "#ff5555"

        if self.check_winner("X"):
            self.end_game("La máquina gana 💀")
            return

        if self.board_full():
            self.end_game("EMPATE 😐")
            return

    def check_winner(self, player):
        return any(self.board[a] == self.board[b] == self.board[c] == player
                   for a, b, c in self.WIN_POS)

    def board_full(self):
        return all(self.board[i] != " " for i in range(1, 10))

    def end_game(self, message):
        self.status["text"] = message

        for i in self.buttons:
            self.buttons[i]["state"] = "disabled"

        restart = tk.Button(self.root, text="Reiniciar", font=("Arial", 14),
                            command=self.restart_game)
        restart.pack(pady=10)

    def restart_game(self):
        self.root.destroy()
        main()

def main():
    root = tk.Tk()
    root.configure(bg="#222222")
    TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
