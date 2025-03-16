import tkinter as tk
from tkinter import messagebox

def check_winner():
    for row in board:
        if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
            return row[0]['text']
    
    for col in range(3):
        if board[0][col]['text'] == board[1][col]['text'] == board[2][col]['text'] != "":
            return board[0][col]['text']
    
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != "":
        return board[0][0]['text']
    
    if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != "":
        return board[0][2]['text']
    
    return None

def is_full():
    return all(board[row][col]['text'] != "" for row in range(3) for col in range(3))

def update_turn_label():
    turn_label.config(text=f"Turn: {turn}")

def on_click(row, col):
    global turn
    if board[row][col]['text'] == "" and not game_over:
        board[row][col]['text'] = turn
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"{winner} wins!")
            reset_board()
            return
        elif is_full():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
            return
        turn = "O" if turn == "X" else "X"
        update_turn_label()

def reset_board():
    global turn, game_over
    for row in range(3):
        for col in range(3):
            board[row][col]['text'] = ""
    turn = "X"
    game_over = False
    update_turn_label()

root = tk.Tk()
root.title("Tic Tac Toe")
board = [[None for _ in range(3)] for _ in range(3)]
turn = "X"
game_over = False

for row in range(3):
    for col in range(3):
        board[row][col] = tk.Button(root, text="", font=('Arial', 24), height=2, width=5,
                                    command=lambda r=row, c=col: on_click(r, c))
        board[row][col].grid(row=row, column=col)

turn_label = tk.Label(root, text=f"Turn: {turn}", font=('Arial', 14))
turn_label.grid(row=3, column=0, columnspan=3)

reset_button = tk.Button(root, text="Reset", font=('Arial', 14), command=reset_board)
reset_button.grid(row=4, column=0, columnspan=3)

update_turn_label()
root.mainloop()