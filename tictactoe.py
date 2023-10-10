# Importing the Tkinter module library
import tkinter as tk

# Importing the random function
import random

class TicTacToeGame:
    def __init__(self, root):
        # Creating the basic window interface
        self.window = root
        self.window.title("Tic-Tac-Toe")
        
        # Creating a list of players
        self.players = ["X", "O"]
        
        # Selecting a random player by passing our list of players
        self.current_player = random.choice(self.players)
        
        # Creating a 2D list of buttons
        self.buttons = [[None, None, None],
                        [None, None, None],
                        [None, None, None]]
        
        # Label to display the user's turn
        self.label = tk.Label(text=self.current_player + " turn", font=('consolas', 40))
        self.label.pack(side="top")
        
        # Restart the game button
        self.reset_button = tk.Button(text="Restart", font=('consolas', 20), command=self.new_game)
        self.reset_button.pack(side="top")
        
        # A frame is used as the foundation class to implement complex widgets
        self.frame = tk.Frame(root)
        self.frame.pack()
        
        # Nested for loop to display the buttons on each spot of the grid
        for row in range(3):
            for column in range(3):
                self.buttons[row][column] = tk.Button(self.frame, text="", font=('consolas', 40),
                                                      width=5, height=2, command=lambda row=row, column=column: self.next_turn(row, column))
                self.buttons[row][column].grid(row=row, column=column)

    def next_turn(self, row, column):
        # Access to our player
        global player
        
        # We want to see if the button is empty 
        if self.buttons[row][column]['text'] == "" and not self.check_winner():
            if self.current_player == self.players[0]:
                self.buttons[row][column]['text'] = self.current_player
                
                # If there is no winner, switch user for their turn
                if not self.check_winner():
                    self.current_player = self.players[1]
                    self.label.config(text=(self.players[1] + " turn"))
                elif self.check_winner():
                    self.label.config(text=(self.players[0] + " wins"))
                elif self.check_winner() == "Tie":
                    self.label.config(text=("Tie!"))
            else: 
                self.buttons[row][column]['text'] = self.current_player
                
                # If there is no winner, switch user for their turn
                if not self.check_winner():
                    self.current_player = self.players[0]
                    self.label.config(text=(self.players[0] + " turn"))
                elif self.check_winner():
                    self.label.config(text=(self.players[1] + " wins"))
                elif self.check_winner() == "Tie":
                    self.label.config(text=("Tie!"))    

    def check_winner(self):
        # Check horizontal winners
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != "":
                self.highlight_winner(row, 0, row, 2)
                return True
        
        # Check vertical winners
        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                self.highlight_winner(0, column, 2, column)
                return True
        
        # Check diagonal winners
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            self.highlight_winner(0, 0, 2, 2)
            return True
        elif self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            self.highlight_winner(0, 2, 2, 0)
            return True
        elif not self.empty_spaces():
            self.highlight_draw()
            return "Tie"
        else:
            return False

    def empty_spaces(self):
        spaces = 9
        
        for row in range(3):
            for column in range(3):
                # If buttons are not empty, decrement an empty space
                if self.buttons[row][column]['text'] != "":
                    spaces -= 1
        if spaces == 0:
            return False
        else:
            return True

    def highlight_winner(self, row1, column1, row2, column2):
        for row in range(row1, row2 + 1):
            for column in range(column1, column2 + 1):
                self.buttons[row][column].config(bg="green")

    def highlight_draw(self):
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(bg="yellow")

    def new_game(self):
        global player
        
        # Chooses a random player for their first turn
        self.current_player = random.choice(self.players)
        self.label.config(text=self.current_player + " turn")
        
        # Clears buttons on the grid
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(text="", bg="#F0F0F0")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
