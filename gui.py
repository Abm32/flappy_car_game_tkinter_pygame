import tkinter as tk
import os

class GameWindow:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Game Window")
        self.parent.geometry

        # Create a canvas for the background image
        self.canvas = tk.Canvas(self.parent, width=356, height=200)
        self.canvas.pack(fill="both", expand=True)

        # Load the background image
        self.background_image = tk.PhotoImage(file="C:/Users/User/Documents/GitHub/pygame/img/background.png")

        # Display the background image on the canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_image)

        # Create buttons for the games
        self.game1_button = tk.Button(self.parent, text="Flappy", command=self.run_game1)
        self.game1_button.place(x=15, y=150)

        self.game2_button = tk.Button(self.parent, text="Car", command=self.run_game2)
        self.game2_button.place(x=295, y=150)

        # Create an Entry widget for entering player name
        self.player_name_label = tk.Label(self.parent, text="Enter player name:")
        self.player_name_label.place(x=130, y=62)

        self.player_name_entry = tk.Entry(self.parent)
        self.player_name_entry.place(x=120, y=92)

        # Create a button for starting the game with the entered player name
        self.start_game_button = tk.Button(self.parent, text="Start Game", command=self.start_game, bg="green", fg="white")
        self.start_game_button.place(x=150, y=116)

        # Create a label for displaying the selected game
        self.selected_game_label = tk.Label(self.parent, text="")
        self.selected_game_label.pack()

        # Initialize a variable for storing the selected game
        self.selected_game = ""

    def run_game1(self):
        # Set the selected game to game 1
        self.selected_game = "game1"

        # Update the selected game label
        self.selected_game_label.config(text="Selected game: Flappy")

    def run_game2(self):
        # Set the selected game to game 2
        self.selected_game = "game2"

        # Update the selected game label
        self.selected_game_label.config(text="Selected game: Car")

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
