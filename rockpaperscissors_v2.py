import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("800x750")  # Further increased window size
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(False, False)
        
        self.player_score = 0
        self.computer_score = 0
        self.choices = ["rock", "paper", "scissors"]
        
        # Load images with much larger size (increased to 250x250)
        self.images = {}
        try:
            for choice in self.choices:
                img_path = f"Projects/Project-RockPapersCissors/images/{choice}.png"
                if os.path.exists(img_path):
                    self.images[choice] = ImageTk.PhotoImage(Image.open(img_path).resize((250, 250)))
                else:
                    self.images = None
                    break
        except:
            self.images = None
        
        # Create frames that will persist
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(fill="both", expand=True)
        
        # Control frame at the bottom that will always be visible
        self.control_frame = tk.Frame(self.root, bg="#f0f0f0", height=50)
        self.control_frame.pack(side=tk.BOTTOM, fill="x", pady=10)
        
        # Create the start screen initially
        self.show_start_screen()
        
    def show_start_screen(self):
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        # Title
        title_label = tk.Label(self.main_frame, text="ROCK PAPER SCISSORS", font=("Arial", 28, "bold"), bg="#f0f0f0")
        title_label.pack(pady=40)
        
        # Start button
        start_button = tk.Button(self.main_frame, text="Start Game", font=("Arial", 18), 
                                command=self.show_game_screen, bg="#4CAF50", fg="white",
                                padx=30, pady=15)
        start_button.pack(pady=30)
        
        # Instructions
        instructions = tk.Label(self.main_frame, text="Beat the computer by choosing the winning move!\n"
                               "Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock",
                               font=("Arial", 14), bg="#f0f0f0", justify="center")
        instructions.pack(pady=30)
        
        # Credits
        credits = tk.Label(self.main_frame, text="@flowstxte", font=("Arial", 10), bg="#f0f0f0")
        credits.pack(pady=10)
        
        # Clear control frame
        for widget in self.control_frame.winfo_children():
            widget.destroy()
        
        # Add quit button to control frame
        quit_button = tk.Button(self.control_frame, text="Quit Game", font=("Arial", 14),
                               command=self.quit_game, bg="#FF6347", padx=10, pady=5)
        quit_button.pack(side=tk.RIGHT, padx=20, pady=5)
        
    def show_game_screen(self):
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        # Score frame
        score_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        score_frame.pack(fill="x", pady=15)
        
        self.player_score_label = tk.Label(score_frame, text=f"Player: {self.player_score}", 
                                     font=("Arial", 18, "bold"), bg="#f0f0f0")
        self.player_score_label.pack(side=tk.LEFT, padx=70)
        
        self.computer_score_label = tk.Label(score_frame, text=f"Computer: {self.computer_score}", 
                                       font=("Arial", 18, "bold"), bg="#f0f0f0")
        self.computer_score_label.pack(side=tk.RIGHT, padx=70)
        
        # Result display
        self.result_var = tk.StringVar()
        self.result_var.set("Make your choice!")
        result_label = tk.Label(self.main_frame, textvariable=self.result_var, font=("Arial", 18, "bold"), bg="#f0f0f0")
        result_label.pack(pady=15)
        
        # Choices display frame
        choices_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        choices_frame.pack(pady=20)
        
        # Player choice display
        player_frame = tk.Frame(choices_frame, bg="#f0f0f0")
        player_frame.pack(side=tk.LEFT, padx=70)  # Increased padding
        
        tk.Label(player_frame, text="Player", font=("Arial", 16, "bold"), bg="#f0f0f0").pack()
        # Remove width and height constraints to allow image to display at full size
        self.player_choice_label = tk.Label(player_frame, bg="#f0f0f0")
        self.player_choice_label.pack(pady=15)
        
        # Computer choice display
        computer_frame = tk.Frame(choices_frame, bg="#f0f0f0")
        computer_frame.pack(side=tk.RIGHT, padx=70)  # Increased padding
        
        tk.Label(computer_frame, text="Computer", font=("Arial", 16, "bold"), bg="#f0f0f0").pack()
        # Remove width and height constraints to allow image to display at full size
        self.computer_choice_label = tk.Label(computer_frame, bg="#f0f0f0")
        self.computer_choice_label.pack(pady=15)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        buttons_frame.pack(pady=30)
        
        # Choice buttons - made larger
        rock_button = tk.Button(buttons_frame, text="Rock", font=("Arial", 14, "bold"),
                               command=lambda: self.play("rock"), width=12, height=2, bg="#e0e0e0")
        rock_button.grid(row=0, column=0, padx=15)
        
        paper_button = tk.Button(buttons_frame, text="Paper", font=("Arial", 14, "bold"),
                                command=lambda: self.play("paper"), width=12, height=2, bg="#e0e0e0")
        paper_button.grid(row=0, column=1, padx=15)
        
        scissors_button = tk.Button(buttons_frame, text="Scissors", font=("Arial", 14, "bold"),
                                   command=lambda: self.play("scissors"), width=12, height=2, bg="#e0e0e0")
        scissors_button.grid(row=0, column=2, padx=15)
        
        # Update control frame
        for widget in self.control_frame.winfo_children():
            widget.destroy()
            
        # Add control buttons - made larger
        back_button = tk.Button(self.control_frame, text="Back to Menu", font=("Arial", 14),
                              command=self.show_start_screen, bg="#3498db", padx=10, pady=5)
        back_button.pack(side=tk.LEFT, padx=20, pady=5)
        
        reset_button = tk.Button(self.control_frame, text="Reset Score", font=("Arial", 14),
                                command=self.reset_score, bg="#FFD700", padx=10, pady=5)
        reset_button.pack(side=tk.LEFT, padx=20, pady=5)
        
        quit_button = tk.Button(self.control_frame, text="Quit Game", font=("Arial", 14),
                               command=self.quit_game, bg="#FF6347", padx=10, pady=5)
        quit_button.pack(side=tk.RIGHT, padx=20, pady=5)
        
    def play(self, player_choice):
        computer_choice = random.choice(self.choices)
        
        # Display choices
        self.display_choice(self.player_choice_label, player_choice)
        self.display_choice(self.computer_choice_label, computer_choice)
        
        # Determine winner
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
            self.player_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1
            
        # Update result and score
        self.result_var.set(f"Computer chose {computer_choice}. {result}")
        self.player_score_label.config(text=f"Player: {self.player_score}")
        self.computer_score_label.config(text=f"Computer: {self.computer_score}")
        
    def display_choice(self, label, choice):
        if self.images and choice in self.images:
            label.config(image=self.images[choice])
        else:
            label.config(text=choice.upper(), font=("Arial", 24, "bold"), image="")
            
    def reset_score(self):
        self.player_score = 0
        self.computer_score = 0
        self.player_score_label.config(text=f"Player: {self.player_score}")
        self.computer_score_label.config(text=f"Computer: {self.computer_score}")
        self.result_var.set("Scores have been reset. Make your choice!")
        
    def quit_game(self):
        if messagebox.askyesno("Quit Game", "Are you sure you want to quit?"):
            self.root.destroy()
            
if __name__ == "__main__":
    # Create image directory if it doesn't exist
    image_dir = "Projects/Project-RockPapersCissors/images"
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
        print(f"Created directory: {image_dir}")
        print("Note: Add rock.png, paper.png, and scissors.png to this directory for images")
    
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
