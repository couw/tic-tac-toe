# Tic-Tac-Toe

A classic Tic-Tac-Toe game implemented in Python, playable in the command-line interface (CLI).

## Features

-   **Human vs. AI**: Play against a random-move AI opponent.
-   **Turn-Based Gameplay**: Players take turns marking the board.
-   **Win Detection**: Automatically detects horizontal, vertical, and diagonal wins.
-   **Draw Detection**: Detects a full board with no winner.
-   **User-Friendly Interface**: Simple text-based board display and input prompts.

## Getting Started

### Prerequisites

-   Python 3.6 or higher

### Installation

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    cd tic-tac-toe
    ```

### Usage

Run the game from the terminal:

```bash
python app.py
```

## How to Play

1.  When the game starts, you will be asked to choose whether you want to go first or second.
2.  Enter `1` to go first or `2` to go second.
3.  The board will be displayed with numbers 1-9 representing the positions.
    ```
    1|2|3
    4|5|6
    7|8|9
    ```
4.  Enter the number corresponding to the position where you want to place your mark.
5.  The game will alternate turns between you and the AI.
6.  The game ends when a player achieves three marks in a row (horizontally, vertically, or diagonally) or when the board is full (a draw).

## Code Structure

The application is built around a `TicTacToe` class that encapsulates all the game logic.

-   `__init__(self)`: Initializes the game board and defines win conditions.
-   `display_board(self)`: Prints the current state of the board to the console.
-   `get_available_moves(self)`: Returns a list of empty positions on the board.
-   `my_turn(self, player_mark)`: Handles the human player's move, including input validation.
-   `enemy_turn(self, enemy_mark)`: Handles the AI's move by choosing a random available position.
-   `check_winner(self, mark)`: Checks if the given mark has won the game.
-   `is_draw(self)`: Checks if the game is a draw.
-   `play(self)`: The main game loop that orchestrates the game flow.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
