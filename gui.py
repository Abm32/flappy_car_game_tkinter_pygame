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

    def run_game1(self):
        # Run game 1
        os.system("python C:/Users/User/Documents/GitHub/pygame/flappy.py")

    def run_game2(self):
        # Run game 2
        os.system("python C:/Users/User/Documents/GitHub/pygame/car-race-python-game-master/game.py")

if __name__ == "__main__":
    root = tk.Tk()
    game_window = GameWindow(root)
    root.mainloop()
