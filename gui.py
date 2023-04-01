import tkinter as tk
import os

class GameWindow:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Game Window")
        self.parent.geometry("400x400")

        # Create buttons for the games
        self.game1_button = tk.Button(parent, text="Game 1", command=self.run_game1)
        self.game1_button.pack(side="left", padx=10)

        self.game2_button = tk.Button(parent, text="Game 2", command=self.run_game2)
        self.game2_button.pack(side="right", padx=10)

        # Create an Entry widget for entering player name
        self.player_name_label = tk.Label(parent, text="Enter player name:")
        self.player_name_label.pack()

        self.player_name_entry = tk.Entry(parent)
        self.player_name_entry.pack()

        # Create a button for starting the game with the entered player name
        self.start_game_button = tk.Button(parent, text="Start Game", command=self.start_game)
        self.start_game_button.pack(pady=10)

        # Create a label for displaying the selected game
        self.selected_game_label = tk.Label(parent, text="")
        self.selected_game_label.pack()

        # Initialize a variable for storing the selected game
        self.selected_game = ""

    def run_game1(self):
        # Set the selected game to game 1
        self.selected_game = "game1"

        # Update the selected game label
        self.selected_game_label.config(text="Selected game: Game 1")

    def run_game2(self):
        # Set the selected game to game 2
        self.selected_game = "game2"

        # Update the selected game label
        self.selected_game_label.config(text="Selected game: Game 2")

    def start_game(self):
        # Get the entered player name
        player_name = self.player_name_entry.get()

        # Check if a game has been selected and a player name has been entered
        if self.selected_game != "" and player_name != "":
            # Run the selected game with the player name as an argument
            if self.selected_game == "game1":
                os.system(f"python C:/Users/User/Documents/GitHub/pygame/flappy.py {player_name}")
            elif self.selected_game == "game2":
                os.system(f"python C:/Users/User/Documents/GitHub/pygame/car-race-python-game-master/game.py {player_name}")
        else:
            # Display an error message if a game has not been selected or a player name has not been entered
            error_message = "Please select a game and enter a player name."
            self.selected_game_label.config(text=error_message)

if __name__ == "__main__":
    root = tk.Tk()
    game_window = GameWindow(root)
    root.mainloop()
