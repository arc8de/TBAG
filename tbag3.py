import tkinter as tk
from tkinter import messagebox
import time

class AdventureGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text-Based Adventure Game")
        self.geometry("400x300")
        
        self.create_widgets()

    def create_widgets(self):
        self.text_output = tk.Text(self, wrap=tk.WORD, width=40, height=15)
        self.text_output.pack(pady=10)
        self.text_output.insert(tk.END, "Welcome to the Adventure Game!\n")
        self.text_output.insert(tk.END, "You find yourself in a dark cave.\n")
        self.text_output.insert(tk.END, "You have 2 choices.\n type left to go left \n type right to go right")


        self.input_entry = tk.Entry(self, width=30)
        self.input_entry.pack(pady=10)

        self.submit_button = tk.Button(self, text="Submit", command=self.process_input)
        self.submit_button.pack()

    def process_input(self):
        user_input = self.input_entry.get().lower()
        self.text_output.insert(tk.END, f"\n> {user_input}\n")

        if "left" in user_input:
            self.explore_left_path()
        elif "right" in user_input:
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
        self.text_output.insert(tk.END, "You encounter a dragon.\n")
        self.show_message("Game Over!", "The dragon breathes fire.")

    def show_message(self, title, message):
        messagebox.showinfo(title, message)
        self.quit()

if __name__ == "__main__":
    game = AdventureGame()
    game.mainloop()
