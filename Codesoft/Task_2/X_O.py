import tkinter as tk
from tkinter import messagebox
import random
import math

# Initialize
board = [' ' for _ in range(9)]
buttons = []
difficulty = 'medium'

# Check win
def check_winner(brd, player):
    win = [[0,1,2],[3,4,5],[6,7,8],
           [0,3,6],[1,4,7],[2,5,8],
           [0,4,8],[2,4,6]]
    return any(all(brd[i] == player for i in combo) for combo in win)

def is_draw(brd):
    return ' ' not in brd

# Minimax
def minimax(brd, depth, is_max):
    if check_winner(brd, 'O'):
        return 1
    if check_winner(brd, 'X'):
        return -1
    if is_draw(brd):
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                score = minimax(brd, depth+1, False)
                brd[i] = ' '
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                score = minimax(brd, depth+1, True)
                brd[i] = ' '
                best = min(best, score)
        return best

def best_move():
    best = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best:
                best = score
                move = i
    return move

# AI move
def ai_turn():
    if difficulty == 'easy':
        move = random.choice([i for i in range(9) if board[i] == ' '])
    elif difficulty == 'medium':
        move = best_move() if random.random() > 0.5 else random.choice([i for i in range(9) if board[i] == ' '])
    else:
        move = best_move()

    board[move] = 'O'
    buttons[move]['text'] = 'O'
    buttons[move]['fg'] = '#f94144'  # red
    buttons[move]['state'] = 'disabled'
    buttons[move]['bg'] = "#ffeeee"

    if check_winner(board, 'O'):
        end_game("😢 You Lost! AI Wins")
    elif is_draw(board):
        end_game("🤝 It's a Draw!")

# User move
def button_click(index):
    if board[index] == ' ':
        board[index] = 'X'
        buttons[index]['text'] = 'X'
        buttons[index]['fg'] = '#277da1'  # blue
        buttons[index]['state'] = 'disabled'
        buttons[index]['bg'] = "#e0f7fa"

        if check_winner(board, 'X'):
            end_game("🎉 You Win!")
        elif is_draw(board):
            end_game("🤝 It's a Draw!")
        else:
            ai_turn()

# End game
def end_game(result):
    messagebox.showinfo("Game Over", result)
    for btn in buttons:
        btn['state'] = 'disabled'

# Reset
def reset_game():
    global board
    board = [' ' for _ in range(9)]
    for btn in buttons:
        btn['text'] = ' '
        btn['state'] = 'normal'
        btn['bg'] = "#fffde7"  # default bg

# Set difficulty
def set_difficulty(level):
    global difficulty
    difficulty = level
    reset_game()

# GUI setup
root = tk.Tk()
root.title("🎮 Tic-Tac-Toe AI")
root.configure(bg="#f0f0f0")
root.geometry("400x500")
root.resizable(False, False)

# Difficulty selection
top_frame = tk.Frame(root, bg="#f0f0f0")
top_frame.pack(pady=10)
tk.Label(top_frame, text="🎯 Select Difficulty:", font=("Arial", 12, 'bold'), bg="#f0f0f0").pack(side=tk.LEFT)
tk.Button(top_frame, text="Easy", width=6, command=lambda: set_difficulty('easy')).pack(side=tk.LEFT, padx=5)
tk.Button(top_frame, text="Medium", width=6, command=lambda: set_difficulty('medium')).pack(side=tk.LEFT, padx=5)
tk.Button(top_frame, text="Hard", width=6, command=lambda: set_difficulty('hard')).pack(side=tk.LEFT, padx=5)

# Game grid
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

for i in range(9):
    btn = tk.Button(frame, text=' ', font=('Arial', 24, 'bold'), height=2, width=5,
                    bg="#fffde7", activebackground="#fce4ec", relief="raised",
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# Reset button
bottom_frame = tk.Frame(root, bg="#f0f0f0")
bottom_frame.pack(pady=10)
tk.Button(bottom_frame, text="🔄 Restart Game", font=('Arial', 12), command=reset_game).pack()

root.mainloop()