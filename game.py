import tkinter as tk

class TicTacToeGame:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe Game")
        self.buttons = []
        self.setup_gui()

    def display_board(self):
        for i in range(9):
            self.buttons[i].config(text=self.board[i])

    def handle_click(self, button_index):
        if self.board[button_index] == ' ':
            self.board[button_index] = self.current_player
            self.display_board()
            if self.check_win(self.current_player):
                self.result_label.config(text=f"Player {self.current_player} wins!")
                return
            self.current_player = 'X' if self.current_player == 'O' else 'O'
            self.turn_label.config(text=f"Turn: Player {self.current_player}")

    def check_win(self, player):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] == player:
                return True
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] == player:
                return True
        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == player:
            return True
        return False

    def handle_reset(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.display_board()
        self.turn_label.config(text="Turn: Player X")
        self.result_label.config(text="")

    def setup_gui(self):
        # Create buttons for the tic-tac-toe grid
        for i in range(9):
            button = tk.Button(self.root, text=' ', width=10, height=3, command=lambda i=i: self.handle_click(i))
            self.buttons.append(button)
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)

        # Create labels for turn and result
        self.turn_label = tk.Label(self.root, text="Turn: Player X")
        self.turn_label.grid(row=3, column=0, columnspan=3)
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=4, column=0, columnspan=3)

        # Create a reset button
        reset_button = tk.Button(self.root, text="Reset Game", command=self.handle_reset)
        reset_button.grid(row=5, column=0, columnspan=3)

    def run(self):
        self.display_board()
        self.root.mainloop()
