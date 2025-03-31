# Rock Paper Scissors Game

## Overview

This is a graphical implementation of the classic Rock Paper Scissors game built with Python and Tkinter. The game features a clean, user-friendly interface where players can compete against the computer in the timeless game of chance and strategy.

## Features

- Intuitive graphical user interface
- Score tracking for both player and computer
- Visual representation of choices with images
- Reset score functionality
- Game instructions on the start screen
- Responsive controls

## Requirements

- Python 3.x
- Tkinter (usually comes with Python)
- PIL (Python Imaging Library) / Pillow

## Installation

1. Clone or download this repository.
2. Install the required dependencies:
   ```sh
   pip install pillow
   ```
3. Make sure you have the image files in the correct directory:
   - Create a folder named `images` in the project directory.
   - Add three image files: `rock.png`, `paper.png`, and `scissors.png`.

## How to Play

1. Run the game:
   ```sh
   python rockpaperscissors_v2.py
   ```
2. Click "Start Game" on the welcome screen.
3. Choose your move by clicking one of the three buttons: **Rock**, **Paper**, or **Scissors**.
4. The computer will randomly select its move.
5. The winner is determined by the classic rules:
   - **Rock** crushes **Scissors**
   - **Scissors** cuts **Paper**
   - **Paper** covers **Rock**
6. The score is updated after each round.
7. Use the "Reset Score" button to start over.
8. Use the "Back to Menu" button to return to the start screen.
9. Use the "Quit Game" button to exit.

## Game Rules

- **Rock beats Scissors**
- **Scissors beats Paper**
- **Paper beats Rock**
- If both players choose the same option, it's a tie.

## Credits

Created by **@flowstxte**
