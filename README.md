# Tic Tac Toe in Python 🕹️

This is a simple **Tic Tac Toe** game built in **Python**, designed to be played in the terminal. The game allows two players to compete against each other, making turns to mark their positions on the 3x3 board. It checks for the winner after every turn and displays the result.

## Features ✨
- **Two-player gameplay**: Players take turns to mark "X" or "O".
- **Victory check**: The game automatically checks for a winner after every move.
- **Draw check**: If the board is full and no player has won, the game ends in a draw.
- **Simple terminal interface**: The game runs directly in the terminal or command prompt.

## How to Play ▶️
1. The game will prompt the current player to input the row and column for their move (values between 0 and 2).
2. The players alternate turns between "X" and "O".
3. The game will announce the winner or if the game ends in a draw.

## Requirements 📋
- Python 3.x installed on your system.

## Installation 🛠️

### 1. Clone the repository:
```bash
git clone https://github.com/RafaPython-Creative/Jogo-da-velha
cd tic-tac-toe
2. Run the game:
Simply run the following command in your terminal:

bash
Copiar
Editar
python jogo.py
This will start the game in your terminal, and you can begin playing!

Game Logic 🧠
The game is designed to:

Accept player moves: It accepts row and column inputs between 0 and 2.

Check for valid moves: If a move is invalid (outside the 0-2 range or already taken), it will prompt the player to try again.

Check for a winner: After each move, the game checks:

Rows

Columns

Diagonals

Declare the winner: The first player to align three marks horizontally, vertically, or diagonally wins.

Handle draws: If the board is filled and no one wins, the game will announce a draw.

Example of Gameplay 🎮
markdown
Copiar
Editar
Player X's turn
Enter row: 0
Enter column: 1
X |   |  
-----
   |   |  
-----
   |   |  

Player O's turn
Enter row: 1
Enter column: 1
X |   |  
-----
   | O |  
-----
   |   |  

License 📄
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements 🙏
This game is created for learning purposes, following tutorials and resources from various programming communities. Special thanks to the Python community for providing excellent resources and inspiration.