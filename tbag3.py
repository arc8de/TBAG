
import tkinter as tk
from tkinter import messagebox
import time

class AdventureGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text-Based Adventure Game")
        self.geometry("1024x768")
        
        self.create_widgets()

    def create_widgets(self):
        self.text_output = tk.Text(self, wrap=tk.WORD, width=110, height=40)
        self.text_output.pack(pady=10)
        self.text_output.insert(tk.END, "\n                                             *****Hello Adventurer*****\n                                               ***Welcome to TBAG!*** \n")
        self.text_output.insert(tk.END, "                                      (A TEXT BASED ADVENTURE GAME BASED ON PYTHON).\n \n \t \t\t \t\t\t   DESCRIPTION \n In a far away place you find yourself in a Mansion which has a Legendary Treasure. Rain lashes against the iron gates, obscuring the imposing silhouette of Ravencrest Manor. You huddle closer to your tattered cloak, the whispers of forgotten grandeur barely audible over the storm. Legends speak of a legendary treasure hidden within its decaying walls, a promise of fortune enough to rewrite your destiny. Greed, or desperation, pushes you forward. With a trembling hand, you pry open the creaking gate, a rusty groan swallowed by the wind.\n The overgrown path leads to a double-doored entrance, adorned with chipped cherubs and weathered coats of arms. Ivy claws its way through cracks, mocking the faded opulence. A tarnished knocker hangs limp, inviting only silence.\n Do you:\n 1. Brace yourself and pound on the oak, hoping to wake the spirits within.\n 2. Seek a hidden entrance, the whispers of caution urging you against boldness.\n 3. Turn back, the storm's fury mirroring your doubts, and return to the comforts of uncertainty.\n \n Choose wisely, adventurer. The path you take determines your fate, and whispers promise that within Ravencrest, fortune and danger lie in equal measure.\n \n Please specify your choice by number (1 or 2) to continue the story.\n \n I can't wait to see where your adventure leads!")
        self.text_output.insert(tk.END, "\nYou have will have 2 choices from now on.\n \n \t \t \t \t\t\t**CHOOSE WISELY** \n \n (1) Type 1 to go left \n (2) Type 2 to go right")


        self.input_entry = tk.Entry(self, width=30)
        self.input_entry.pack(pady=10)

        self.submit_button = tk.Button(self, text="Submit", command=self.process_input)
        self.submit_button.pack()

    def process_input(self):
        user_input = self.input_entry.get().lower()
        self.text_output.insert(tk.END, f"\n> {user_input}\n")

        if "1" in user_input:
            self.explore_left_path()
        elif "2" in user_input:
            self.explore_right_path()
        else:
            self.text_output.insert(tk.END, "Invalid choice. Try again.\n")

        self.input_entry.delete(0, tk.END) # Clear the input field

    def explore_left_path(self):
        self.text_output.insert(tk.END, "You chose to go left.\n")
        time.sleep(1)
        self.text_output.insert(tk.END, "You find a treasure chest!\n")
        self.show_message("Congratulations!", "You win!")

    def explore_right_path(self):
        self.text_output.insert(tk.END, "You chose to go right.\n")
        time.sleep(1)
        self.text_output.insert(tk.END, "You encounter a dragon.")
        self.show_message("Game Over!", "\n You Died.\n The dragon killed you.")

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

if __name__ == "__main__":
    game = AdventureGame()
    game.mainloop()
