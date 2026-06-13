"""
Tic Tac Toe Deluxe - Completo
Features:
- GUI Tkinter
- Sound via pygame (optional)
- Dark/Light mode
- Explosion animation on win
- Difficulties: Random, Easy (random), Impossible (Minimax)
- Mode: vs Machine (machine always starts at center), or 2-players
- Settings window (sound/music on/off)
- Achievements system persisted to 'achievements.json'
- Saveable settings to 'settings.json'
"""

import tkinter as tk
from tkinter import messagebox, ttk
import random
import json
import os
import threading
import time

# Attempt to import pygame for sounds; handle gracefully if not available
try:
    import pygame
    PYGAME_AVAILABLE = True
except Exception:
    PYGAME_AVAILABLE = False

# --- Paths ---
ASSET_DIR = "assets"
SETTINGS_FILE = "settings.json"
ACHIEVEMENTS_FILE = "achievements.json"

# Ensure asset dir exists
if not os.path.isdir(ASSET_DIR):
    os.makedirs(ASSET_DIR, exist_ok=True)

# Default settings
DEFAULT_SETTINGS = {
    "theme": "dark",             # dark or light
    "sound": True,
    "music": True,
    "difficulty": "Random",      # Random, Easy, Impossible
    "mode": "vs_machine"         # vs_machine or two_players
}

# Default achievements structure
DEFAULT_ACHIEVEMENTS = {
    "played_games": 0,
    "player_wins": 0,
    "machine_wins": 0,
    "ties": 0,
    "streak": 0,
    "unlocked": []   # achievement ids
}

# Achievements definitions
ACHIEVEMENT_DEFS = [
    {"id": "first_blood", "title": "Primera victoria", "desc": "Gana tu primera partida."},
    {"id": "machine_down", "title": "Derrotaste a la máquina", "desc": "Gana 5 partidas contra la máquina."},
    {"id": "unstoppable", "title": "Imparable", "desc": "Consigue racha de 3 victorias seguidas."},
    {"id": "no_loss", "title": "Invencible", "desc": "Gana 10 partidas."},
    {"id": "tie_master", "title": "Empate estratégico", "desc": "Consigue 5 empates."}
]

# Utility: load/save settings & achievements
def load_json(path, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default.copy()

def save_json(path, data):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print("Error saving", path, e)

# Sound helper (uses pygame if available)
class SoundPlayer:
    def __init__(self, settings):
        self.settings = settings
        self.bg_loaded = False
        if PYGAME_AVAILABLE:
            try:
                pygame.mixer.init()
            except Exception as e:
                print("pygame init failed:", e)

    def play_sound(self, filename):
        if not self.settings.get("sound", True):
            return
        if not PYGAME_AVAILABLE:
            return
        path = os.path.join(ASSET_DIR, filename)
        if os.path.exists(path):
            try:
                s = pygame.mixer.Sound(path)
                s.play()
            except Exception as e:
                print("Error playing sound", e)

    def start_music(self):
        if not self.settings.get("music", True):
            return
        if not PYGAME_AVAILABLE:
            return
        try:
            path = os.path.join(ASSET_DIR, "018136_funny-music-orchestra-wav-54828.mp3")
            if os.path.exists(path):
                pygame.mixer.music.load(path)
                pygame.mixer.music.set_volume(0.25)
                pygame.mixer.music.play(-1)
                self.bg_loaded = True
        except Exception as e:
            print("Music error:", e)

    def stop_music(self):
        if PYGAME_AVAILABLE:
            try:
                pygame.mixer.music.stop()
            except:
                pass

# ---------- Minimax AI for Impossible mode ----------
def available_moves(board):
    return [i for i in range(1, 10) if board[i] == " "]

def check_winner_board(board, player):
    WIN_POS = [
        (1,2,3), (4,5,6), (7,8,9),
        (1,4,7), (2,5,8), (3,6,9),
        (1,5,9), (3,5,7)
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in WIN_POS)

def evaluate_board(board):
    if check_winner_board(board, "X"):
        return 1
    elif check_winner_board(board, "O"):
        return -1
    else:
        return 0

def minimax(board, maximizing, depth=0):
    # terminal
    score = evaluate_board(board)
    if score != 0:
        return score
    if all(board[i] != " " for i in range(1, 10)):
        return 0

    if maximizing:
        best = -999
        for m in available_moves(board):
            board[m] = "X"
            val = minimax(board, False, depth+1)
            board[m] = " "
            # prefer faster wins: subtract depth (the earlier the win, bigger value)
            if val - depth > best:
                best = val - depth
        return best
    else:
        best = 999
        for m in available_moves(board):
            board[m] = "O"
            val = minimax(board, True, depth+1)
            board[m] = " "
            if val + depth < best:
                best = val + depth
        return best

def best_move_minimax(board):
    best_val = -999
    best_move = None
    for m in available_moves(board):
        board[m] = "X"
        val = minimax(board, False, 0)
        board[m] = " "
        if val > best_val:
            best_val = val
            best_move = m
    return best_move

# ---------- Main App ----------
class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Deluxe Full")
        self.root.geometry("520x640")
        self.root.resizable(False, False)

        # load settings and achievements
        self.settings = load_json(SETTINGS_FILE, DEFAULT_SETTINGS)
        self.achievements = load_json(ACHIEVEMENTS_FILE, DEFAULT_ACHIEVEMENTS)

        # sound player
        self.snd = SoundPlayer(self.settings)
        if self.settings.get("music", True):
            # run music in separate thread not to block
            threading.Thread(target=self.snd.start_music, daemon=True).start()

        self.theme_colors = self.get_theme(self.settings.get("theme", "dark"))
        self.cell_texts = {}
        self.cell_rects = {}
        self.setup_ui()
        self.reset_game(initial=True)

    def get_theme(self, theme):
        if theme == "light":
            return {
                "bg": "#f0f0f0",
                "panel": "#ffffff",
                "fg": "#111111",
                "btn_bg": "#e2e8f0",
                "accent": "#0066cc",
                "x_color": "#cc0000",
                "o_color": "#0055cc"
            }
        else:
            return {
                "bg": "#121212",
                "panel": "#1e1e1e",
                "fg": "#eaeaea",
                "btn_bg": "#2b2b2b",
                "accent": "#00eaff",
                "x_color": "#ff6666",
                "o_color": "#66aaff"
            }

    def setup_ui(self):
        self.root.configure(bg=self.theme_colors["bg"])
        # top frame - title & settings
        top = tk.Frame(self.root, bg=self.theme_colors["panel"])
        top.pack(fill="x", padx=12, pady=(12,6))

        title = tk.Label(top, text="TIC TAC TOE DELUXE", font=("Inter", 18, "bold"),
                         bg=self.theme_colors["panel"], fg=self.theme_colors["accent"])
        title.pack(side="left", padx=10, pady=8)

        btn_settings = tk.Button(top, text="⚙️", font=("Arial", 12, "bold"),
                                 command=self.open_settings, bg=self.theme_colors["btn_bg"])
        btn_settings.pack(side="right", padx=10)

        btn_ach = tk.Button(top, text="🏆 Achievements", command=self.open_achievements,
                            bg=self.theme_colors["btn_bg"])
        btn_ach.pack(side="right", padx=6)

        # score & status
        self.score_var = tk.StringVar()
        self.status_var = tk.StringVar()

        score_frame = tk.Frame(self.root, bg=self.theme_colors["bg"])
        score_frame.pack(pady=(6,4))

        self.lbl_score = tk.Label(score_frame, textvariable=self.score_var,
                                  font=("Inter", 14), fg=self.theme_colors["fg"], bg=self.theme_colors["bg"])
        self.lbl_score.pack()

        self.lbl_status = tk.Label(self.root, textvariable=self.status_var,
                                   font=("Arial", 14), fg=self.theme_colors["fg"], bg=self.theme_colors["bg"])
        self.lbl_status.pack(pady=6)

        # board frame (canvas style to allow animations)
        board_frame = tk.Frame(self.root, bg=self.theme_colors["bg"])
        board_frame.pack(pady=8)
        self.canvas = tk.Canvas(board_frame, width=360, height=360, bg=self.theme_colors["panel"], highlightthickness=0)
        self.board_canvas = tk.Canvas(
        board_frame,
        width=360,
        height=360,
        bg="#111111",      # fondo oscuro
        highlightthickness=0
)

        self.canvas.pack()
        # draw grid
        self.draw_grid()
        
        # a transparent overlay canvas for explosion animation
        self.overlay = tk.Canvas(board_frame, width=360, height=360, bg=board_frame["bg"], highlightthickness=0)

        self.overlay.place(x=0, y=0)

        # control buttons
        ctrl = tk.Frame(self.root, bg=self.theme_colors["bg"])
        ctrl.pack(pady=12)

        self.btn_restart = tk.Button(ctrl, text="Reiniciar partida", command=self.restart_game, bg=self.theme_colors["btn_bg"])
        self.btn_restart.grid(row=0, column=0, padx=6, pady=6)

        self.btn_mode = tk.Button(ctrl, text="Cambiar modo", command=self.toggle_mode, bg=self.theme_colors["btn_bg"])
        self.btn_mode.grid(row=0, column=1, padx=6, pady=6)

        self.btn_diff = tk.Button(ctrl, text="Cambiar dificultad", command=self.cycle_difficulty, bg=self.theme_colors["btn_bg"])
        self.btn_diff.grid(row=0, column=2, padx=6, pady=6)

        # map of cells to rectangles / text IDs
        self.cell_rects = {}
        self.cell_texts = {}

        # bind clicks on canvas
        self.canvas.bind("<Button-1>", self.on_canvas_click)

    # Drawing grid and slots
    def draw_grid(self):
            line_color = "#27f5ff"   # color visible en modo oscuro
        # Líneas verticales
            for i in range(1, 3):
                x = i * 120
                self.board_canvas.create_line(x, 0, x, 360, fill=line_color, width=3)
        # Líneas horizontales
            for i in range(1, 3):
                y = i * 120
                self.board_canvas.create_line(0, y, 360, y, fill=line_color, width=3)


    def reset_game(self, initial=False):
        # board: index 1..9
        self.board = [" "] * 10
        self.current_turn = "O"  # player is O; machine X always starts (we will place X center)
        self.settings = load_json(SETTINGS_FILE, DEFAULT_SETTINGS)  # reload incase changed
        self.theme_colors = self.get_theme(self.settings.get("theme", "dark"))
        self.draw_grid()
        self.overlay.delete("all")
        # update UI texts
        self.update_score_label()
        mode = self.settings.get("mode", "vs_machine")
        self.status_var.set("Tu turno (O)" if mode == "vs_machine" or mode == "two_players" else "Listo")
        # place machine start X in center if vs_machine
        if self.settings.get("mode", "vs_machine") == "vs_machine":
            self.place_mark(5, "X", initial_place=True)  # machine starts in center
        if initial:
            # update scores from achievements
            self.score_player = self.achievements.get("player_wins", 0)
            self.score_machine = self.achievements.get("machine_wins", 0)
        else:
            # keep scores
            pass

    def update_score_label(self):
        player = self.achievements.get("player_wins", 0)
        machine = self.achievements.get("machine_wins", 0)
        ties = self.achievements.get("ties", 0)
        self.score_var.set(f"Jugador (O): {player}    Máquina (X): {machine}    Empates: {ties}")

    def place_mark(self, pos, mark, initial_place=False):
        self.board[pos] = mark
        # update canvas text
        txt_id = self.cell_texts.get(pos)
        if txt_id:
            if mark == "X":
                self.canvas.itemconfigure(txt_id, text="X", fill=self.theme_colors["x_color"])
            elif mark == "O":
                self.canvas.itemconfigure(txt_id, text="O", fill=self.theme_colors["o_color"])
        if not initial_place:
            # play sound
            self.snd.play_sound("click.wav")

    def on_canvas_click(self, event):
        # map x,y to cell index
        pos = self.get_cell_by_coords(event.x, event.y)
        if not pos:
            return
        mode = self.settings.get("mode", "vs_machine")
        if mode == "two_players":
            self.handle_player_vs_player(pos)
        else:
            self.handle_player_vs_machine(pos)

    def get_cell_by_coords(self, x, y):
        pad = 10
        cell_size = 110
        for r in range(3):
            for c in range(3):
                x1 = pad + c * cell_size
                y1 = pad + r * cell_size
                x2 = x1 + cell_size - 10
                y2 = y1 + cell_size - 10
                if x1 <= x <= x2 and y1 <= y <= y2:
                    return 3*r + c + 1
        return None

    # Player vs Player
    def handle_player_vs_player(self, pos):
        if self.board[pos] != " ":
            return
        # alternate between O and X
        # If center is prefilled by machine in other modes, center may be occupied; in two-player we allow starting fresh
        # Here we let Player1 = O (starts), Player2 = X
        # Determine who moves: count marks
        moves_made = sum(1 for i in range(1,10) if self.board[i] != " ")
        current = "O" if moves_made % 2 == 0 else "X"
        self.place_mark(pos, current)
        if self.check_winner(current):
            self.on_game_end(f"{'Jugador O' if current=='O' else 'Jugador X'} gana")
        elif self.board_full():
            self.on_game_end("EMPATE")
        else:
            self.status_var.set(f"Turno: {'Jugador X' if current=='O' else 'Jugador O'}")

    # Player vs Machine
    def handle_player_vs_machine(self, pos):
        if self.board[pos] != " ":
            return
        # place player's move (O)
        self.place_mark(pos, "O")
        if self.check_winner("O"):
            # player wins
            self.achievements["player_wins"] = self.achievements.get("player_wins", 0) + 1
            self.achievements["played_games"] = self.achievements.get("played_games", 0) + 1
            self.achievements["streak"] = self.achievements.get("streak", 0) + 1
            save_json(ACHIEVEMENTS_FILE, self.achievements)
            self.snd.play_sound("you-win-sfx-442128.mp3")
            self.on_game_end("¡GANASTE! 😎🔥")
            return
        if self.board_full():
            self.achievements["ties"] = self.achievements.get("ties", 0) + 1
            self.achievements["played_games"] = self.achievements.get("played_games", 0) + 1
            self.achievements["streak"] = 0
            save_json(ACHIEVEMENTS_FILE, self.achievements)
            self.on_game_end("EMPATE 😐")
            return

        # machine moves after short delay
        self.status_var.set("La máquina piensa...")
        self.root.after(300, self.machine_move)

    def machine_move(self):
        diff = self.settings.get("difficulty", "Random")
        # select free moves
        free = [i for i in range(1, 10) if self.board[i] == " "]
        if not free:
            return

        # Machine always plays X
        if diff == "Random":
            pos = random.choice(free)
        elif diff == "Easy":
            # 70% random, 30% try to win (simple heuristics)
            if random.random() < 0.7:
                pos = random.choice(free)
            else:
                pos = self.try_block_or_win("X") or random.choice(free)
        elif diff == "Impossible":
            # Use minimax but handle trivial: if only center used, minimax handles remaining
            # Copy board for minimax
            bcopy = self.board[:]
            pos = best_move_minimax(bcopy)
            if pos is None:
                pos = random.choice(free)
        else:
            pos = random.choice(free)

        self.place_mark(pos, "X")
        # check winner
        if self.check_winner("X"):
            self.achievements["machine_wins"] = self.achievements.get("machine_wins", 0) + 1
            self.achievements["played_games"] = self.achievements.get("played_games", 0) + 1
            self.achievements["streak"] = 0
            save_json(ACHIEVEMENTS_FILE, self.achievements)
            self.snd.play_sound("win.wav")
            self.on_game_end("La máquina gana 💀")
            return

        if self.board_full():
            self.achievements["ties"] = self.achievements.get("ties", 0) + 1
            self.achievements["played_games"] = self.achievements.get("played_games", 0) + 1
            self.achievements["streak"] = 0
            save_json(ACHIEVEMENTS_FILE, self.achievements)
            self.on_game_end("EMPATE 😐")
            return

        self.status_var.set("Tu turno (O)")

    def try_block_or_win(self, player):
        # try to find immediate win or block opponent
        opponent = "O" if player == "X" else "X"
        for p in available_moves(self.board):
            # try winning move
            self.board[p] = player
            if check_winner_board(self.board, player):
                self.board[p] = " "
                return p
            self.board[p] = " "
        for p in available_moves(self.board):
            self.board[p] = opponent
            if check_winner_board(self.board, opponent):
                self.board[p] = " "
                return p
            self.board[p] = " "
        return None

    def check_winner(self, player):
        return check_winner_board(self.board, player)

    def board_full(self):
        return all(self.board[i] != " " for i in range(1, 10))

    # Called when a game ends
    def on_game_end(self, message):
        self.status_var.set(message)
        # disable further clicks by overlaying (we'll just leave board but ignore clicks by checking state)
        # play explosion animation if win
        if "gana" in message.lower() or "ganaste" in message.lower():
            # explosion at winning cells if win
            winner = "X" if "máquina" in message.lower() else "O"
            win_cells = self.find_winning_cells(winner)
            if win_cells:
                # compute center of win cells and explode there
                x,y = self.center_of_cells(win_cells)
                self.show_explosion(x, y)
            else:
                # generic explosion center
                self.show_explosion(180, 180)
            self.snd.play_sound("explosion.wav")

        # update UI & achievements
        self.update_score_label()
        self.check_achievements()
        # show a small popup dialog offering restart
        self.root.after(700, lambda: messagebox.showinfo("Partida terminada", message))

    def find_winning_cells(self, player):
        WIN_POS = [
            (1,2,3), (4,5,6), (7,8,9),
            (1,4,7), (2,5,8), (3,6,9),
            (1,5,9), (3,5,7)
        ]
        for a,b,c in WIN_POS:
            if self.board[a] == self.board[b] == self.board[c] == player:
                return (a,b,c)
        return None

    def center_of_cells(self, cells):
        # compute approximate center canvas coords of given cells (1..9)
        pad = 10
        cell_size = 110
        xs, ys = [], []
        for cell in cells:
            r = (cell-1) // 3
            c = (cell-1) % 3
            x1 = pad + c * cell_size
            y1 = pad + r * cell_size
            x2 = x1 + cell_size - 10
            y2 = y1 + cell_size - 10
            xs.append((x1 + x2)/2)
            ys.append((y1 + y2)/2)
        return sum(xs)/len(xs), sum(ys)/len(ys)

    def show_explosion(self, cx, cy):
        # simple particle explosion animation on overlay canvas
        overlay = self.overlay
        overlay.delete("all")
        particles = []
        for _ in range(24):
            angle = random.uniform(0, 2*3.14159)
            speed = random.uniform(3, 9)
            life = random.uniform(0.6, 1.2)
            size = random.uniform(6, 14)
            color = random.choice([self.theme_colors["accent"], "#ffcc00", "#ff5555", "#66ff66"])
            p = {"x":cx, "y":cy, "vx":speed*math_cos(angle), "vy":speed*math_sin(angle), "life":life, "age":0, "size":size, "color":color}
            particles.append(p)

        start = time.time()
        fps = 60
        interval = 1.0 / fps
        def step():
            nonlocal particles
            overlay.delete("all")
            now = time.time()
            dt = interval
            for p in particles:
                p["age"] += dt
                if p["age"] > p["life"]:
                    continue
                # simple physics
                p["x"] += p["vx"]
                p["y"] += p["vy"]
                # gravity
                p["vy"] += 0.4
                alpha = max(0, 1 - (p["age"]/p["life"]))
                size = p["size"] * alpha
                overlay.create_oval(p["x"]-size, p["y"]-size, p["x"]+size, p["y"]+size, fill=p["color"], outline="")
            particles = [p for p in particles if p["age"] <= p["life"]]
            if particles:
                overlay.after(int(interval*1000), step)
            else:
                overlay.delete("all")
        step()

    def restart_game(self):
        # reset board but keep achievements scoreboard
        self.snd.play_sound("click.wav")
        # reset board but leave scores
        self.board = [" "] * 10
        self.draw_grid()
        self.overlay.delete("all")
        # place starting X again if vs_machine
        if self.settings.get("mode", "vs_machine") == "vs_machine":
            self.place_mark(5, "X", initial_place=True)
        self.status_var.set("Tu turno (O)")
        save_json(SETTINGS_FILE, self.settings)

    def toggle_mode(self):
        # toggle between vs_machine and two_players
        cur = self.settings.get("mode", "vs_machine")
        self.settings["mode"] = "two_players" if cur == "vs_machine" else "vs_machine"
        save_json(SETTINGS_FILE, self.settings)
        self.snd.play_sound("click.wav")
        messagebox.showinfo("Modo cambiado", f"Modo actual: {self.settings['mode']}")
        self.reset_game()

    def cycle_difficulty(self):
        order = ["Random", "Easy", "Impossible"]
        cur = self.settings.get("difficulty", "Random")
        i = order.index(cur) if cur in order else 0
        nxt = order[(i+1)%len(order)]
        self.settings["difficulty"] = nxt
        save_json(SETTINGS_FILE, self.settings)
        self.snd.play_sound("click.wav")
        messagebox.showinfo("Dificultad", f"Dificultad actual: {nxt}")

    def open_settings(self):
        self.snd.play_sound("click.wav")
        win = tk.Toplevel(self.root)
        win.title("Configuración")
        win.geometry("360x300")
        win.resizable(False, False)
        bg = self.theme_colors["panel"]
        win.configure(bg=bg)

        tk.Label(win, text="Configuración", font=("Arial", 16, "bold"), bg=bg, fg=self.theme_colors["fg"]).pack(pady=8)

        # Theme
        theme_var = tk.StringVar(value=self.settings.get("theme", "dark"))
        tk.Label(win, text="Tema:", bg=bg, fg=self.theme_colors["fg"]).pack(anchor="w", padx=12)
        tk.Radiobutton(win, text="Oscuro", variable=theme_var, value="dark", bg=bg, fg=self.theme_colors["fg"]).pack(anchor="w", padx=20)
        tk.Radiobutton(win, text="Claro", variable=theme_var, value="light", bg=bg, fg=self.theme_colors["fg"]).pack(anchor="w", padx=20)

        # Sound/music toggles
        sound_var = tk.BooleanVar(value=self.settings.get("sound", True))
        music_var = tk.BooleanVar(value=self.settings.get("music", True))
        tk.Checkbutton(win, text="Sonidos", variable=sound_var, bg=bg, fg=self.theme_colors["fg"]).pack(anchor="w", padx=12, pady=6)
        tk.Checkbutton(win, text="Música de fondo", variable=music_var, bg=bg, fg=self.theme_colors["fg"]).pack(anchor="w", padx=12)

        # Difficulty
        tk.Label(win, text="Dificultad:", bg=bg, fg=self.theme_colors["fg"]).pack(anchor="w", padx=12, pady=(10,0))
        diff_var = tk.StringVar(value=self.settings.get("difficulty", "Random"))
        ttk.Combobox(win, textvariable=diff_var, values=["Random", "Easy", "Impossible"], state="readonly").pack(padx=12, pady=6)

        # Mode
        tk.Label(win, text="Modo:", bg=bg, fg=self.theme_colors["fg"]).pack(anchor="w", padx=12, pady=(8,0))
        mode_var = tk.StringVar(value=self.settings.get("mode", "vs_machine"))
        ttk.Combobox(win, textvariable=mode_var, values=["vs_machine", "two_players"], state="readonly").pack(padx=12, pady=6)

        def save_and_close():
            self.settings["theme"] = theme_var.get()
            self.settings["sound"] = bool(sound_var.get())
            self.settings["music"] = bool(music_var.get())
            self.settings["difficulty"] = diff_var.get()
            self.settings["mode"] = mode_var.get()
            save_json(SETTINGS_FILE, self.settings)
            # apply music toggle
            if not self.settings.get("music", False):
                self.snd.stop_music()
            else:
                threading.Thread(target=self.snd.start_music, daemon=True).start()
            self.snd.play_sound("click.wav")
            win.destroy()
            # apply theme changes by recreating UI
            self.reset_game()

        tk.Button(win, text="Guardar", command=save_and_close, bg=self.theme_colors["btn_bg"]).pack(pady=12)

    def open_achievements(self):
        self.snd.play_sound("click.wav")
        win = tk.Toplevel(self.root)
        win.title("Achievements")
        win.geometry("420x360")
        bg = self.theme_colors["panel"]
        win.configure(bg=bg)
        tk.Label(win, text="Achievements", font=("Arial", 16, "bold"), bg=bg, fg=self.theme_colors["fg"]).pack(pady=8)
        frame = tk.Frame(win, bg=bg)
        frame.pack(fill="both", expand=True, padx=10, pady=6)

        unlocked = set(self.achievements.get("unlocked", []))
        for ad in ACHIEVEMENT_DEFS:
            unlocked_mark = "✅" if ad["id"] in unlocked else "❌"
            lbl = tk.Label(frame, text=f"{unlocked_mark} {ad['title']} - {ad['desc']}", anchor="w",
                           bg=bg, fg=self.theme_colors["fg"], wraplength=380, justify="left")
            lbl.pack(anchor="w", pady=4)

    def check_achievements(self):
        # simple checks and unlocking
        unlocked = set(self.achievements.get("unlocked", []))
        changed = False

        # first blood
        if self.achievements.get("player_wins", 0) >= 1 and "first_blood" not in unlocked:
            unlocked.add("first_blood")
            changed = True

        if self.achievements.get("player_wins", 0) >= 5 and "machine_down" not in unlocked:
            unlocked.add("machine_down"); changed = True

        if self.achievements.get("player_wins", 0) >= 10 and "no_loss" not in unlocked:
            unlocked.add("no_loss"); changed = True

        if self.achievements.get("ties", 0) >= 5 and "tie_master" not in unlocked:
            unlocked.add("tie_master"); changed = True

        if self.achievements.get("streak", 0) >= 3 and "unstoppable" not in unlocked:
            unlocked.add("unstoppable"); changed = True

        if changed:
            self.achievements["unlocked"] = list(unlocked)
            save_json(ACHIEVEMENTS_FILE, self.achievements)
            # small popup
            self.snd.play_sound("win.wav")
            messagebox.showinfo("🎉 Nuevo logro desbloqueado", "Revisa la sección de Achievements para ver tus nuevos logros.")

    # Utility: map board index to center coords for clicking externally
    def cell_center_coords(self, idx):
        pad = 10
        cell_size = 110
        r = (idx-1) // 3
        c = (idx-1) % 3
        x1 = pad + c * cell_size
        y1 = pad + r * cell_size
        x2 = x1 + cell_size - 10
        y2 = y1 + cell_size - 10
        return (x1+x2)//2, (y1+y2)//2

import math
# simple wrappers for math cos/sin to avoid many math imports earlier
def math_cos(a): return math.cos(a)
def math_sin(a): return math.sin(a)

# ---------- Run ----------
def main():
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
