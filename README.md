# Tic Tac Toe (Python)

A simple command-line implementation of the classic Tic Tac Toe game in Python.  
Two players take turns placing `X` and `O` on a 3x3 board until one wins or the game ends in a draw.

---

## Features
- Randomly chooses the first player (`X` or `O`).
- Validates moves (prevents overwriting occupied cells).
- Detects winning conditions (rows, columns, diagonals).
- Detects draws when the board is full.
- Simple CLI-based interface.

---

## Project Structure
```

tictactoe/
│── README.md 
└── src
    ├── main.py   # Main game script
       
```
---

## How to Run

Make sure you have **Python 3.7+** installed.  
Clone this repo or copy the script, then run:

```bash
python src/main.py
```

---

## How to Play

1. The program randomly decides who goes first (`X` or `O`).
2. Players take turns entering a number between **1–9**, representing the board:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

3. If a player chooses an occupied cell or an invalid number, they’ll be asked to try again.
4. The game ends when:

   * A player has three in a row (win).
   * The board is full (draw).

---

## Example Gameplay

```
Welcome to Tic Tac Toe!
  |   |  
---------
  |   |  
---------
  |   |  
It's X's turn.
Enter number of block (1–9): 5

  |   |  
---------
  | X |  
---------
  |   |  
It's O's turn.
...
```

---
