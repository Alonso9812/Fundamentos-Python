import tkinter as tk
from tkinter import messagebox
import random
import pygame

# ---------------- SONIDO ---------------- #

pygame.mixer.init()

def play_sound(sound):
    try:
        pygame.mixer.Sound(sound).play()
    except:
        pass

def play_music():
    try:
        pygame.mixer.music.load("018136_funny-music-orchestra-wav-54828.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
    except:
        pass


# ================ JUEGO ================= #

class TicTacToeDeluxe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe DELUXE")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        play_music()

        self.buttons = {}
        self.board = [" "] * 10

        self.WIN_POS = [
            (1,2,3), (4,5,6), (7,8,9),
            (1,4,7), (2,5,8), (3,6,9),
            (1,5,9), (3,5,7)
        ]

        self.score_player = 0
        self.score_machine = 0

        self.show_start_screen()

    # ---------------- START SCREEN ---------------- #

    def show_start_screen(self):
        self.start_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.start_frame.pack(padx=20, pady=20)

        tk.Label(self.start_frame, text="TIC TAC TOE DELUXE",
                 font=("Arial", 32, "bold"), fg="#00eaff", bg="#1e1e1e").pack(pady=20)

        tk.Button(self.start_frame, text="JUGAR",
                  font=("Arial", 22, "bold"),
                  bg="#00eaff", fg="#000", width=10,
                  activebackground="#00aacc",
                  command=self.start_game).pack(pady=20)

        tk.Label(self.start_frame, text="🤖 La máquina siempre inicia con X\n🎵 Música, animaciones y más",
                 fg="white", bg="#1e1e1e", font=("Arial", 14)).pack(pady=10)

    def start_game(self):
        play_sound("click.wav")
        self.start_frame.destroy()
        self.game_screen()

    # ---------------- GAME SCREEN ---------------- #

    def game_screen(self):
        self.main_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.main_frame.pack()

        # Scoreboard
        self.score_label = tk.Label(self.main_frame,
                                    text=self.score_text(),
                                    font=("Arial", 16, "bold"),
                                    fg="#00eaff", bg="#1e1e1e")
        self.score_label.pack(pady=5)

        # Status
        self.status = tk.Label(self.main_frame, text="Tu turno (O)",
                               font=("Arial", 18), fg="white", bg="#1e1e1e")
        self.status.pack(pady=10)

        # Board
        self.board_frame = tk.Frame(self.main_frame, bg="#1e1e1e")
        self.board_frame.pack()

        for i in range(1, 10):
            btn = tk.Button(self.board_frame, text=" ", font=("Arial", 30, "bold"),
                            width=3, height=1, bg="#2c2c2c", fg="white",
                            activebackground="#555555",
                            command=lambda i=i: self.player_move(i))

            self.buttons[i] = btn
            btn.grid(row=(i-1)//3, column=(i-1)%3, padx=6, pady=6)

            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#3a3a3a"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#2c2c2c"))

        # Machine first move
        self.machine_first_move()

    def score_text(self):
        return f"Jugador (O): {self.score_player}   |   Máquina (X): {self.score_machine}"

    def machine_first_move(self):
        self.board[5] = "X"
        self.buttons[5]["text"] = "X"
        self.buttons[5]["fg"] = "#ff6666"

    # ---------------- PLAYER MOVE ---------------- #

    def player_move(self, pos):
        if self.board[pos] != " ":
            return

        play_sound("click.wav")

        self.board[pos] = "O"
        self.buttons[pos]["text"] = "O"
        self.buttons[pos]["fg"] = "#66aaff"

        if self.check_winner("O"):
            play_sound("you-win-sfx-442128.mp3")
            self.score_player += 1
            self.end_game("¡GANASTE! 😎🔥")
            return

        if self.board_full():
            self.end_game("EMPATE 😐")
            return

        self.root.after(300, self.machine_move)

    # ---------------- MACHINE MOVE ---------------- #

    def machine_move(self):
        free = [i for i in range(1, 10) if self.board[i] == " "]
        pos = random.choice(free)

        self.board[pos] = "X"
        self.buttons[pos]["text"] = "X"
        self.buttons[pos]["fg"] = "#ff6666"

        if self.check_winner("X"):
            play_sound("win.wav")
            self.score_machine += 1
            self.end_game("La máquina gana 💀")
            return

        if self.board_full():
            self.end_game("EMPATE 😐")
            return

    # ---------------- CHECK ---------------- #

    def check_winner(self, p):
        return any(self.board[a] == self.board[b] == self.board[c] == p
                   for a, b, c in self.WIN_POS)

    def board_full(self):
        return all(self.board[i] != " " for i in range(1, 10))

    # ---------------- END GAME ---------------- #

    def end_game(self, msg):
        self.status.config(text=msg)
        for i in self.buttons:
            self.buttons[i]["state"] = "disabled"

        tk.Button(self.main_frame, text="Reiniciar partida",
                  font=("Arial", 16, "bold"),
                  bg="#00eaff",
                  command=self.restart).pack(pady=10)

    def restart(self):
        play_sound("click.wav")
        self.main_frame.destroy()
        self.__init__(self.root)


# MAIN
def main():
    root = tk.Tk()
    TicTacToeDeluxe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
