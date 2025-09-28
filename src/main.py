import random
from typing import List


class TicTacToe():
    """
    A simple Tic Tac Toe game played betweem two players ('X' and 'O').
    """
    def __init__(self) -> None:
        """
        Initialize the Tic Tac Toe board and randomly choose the first player.
        """
        self.board: List[str] = [' '] * 10
        self.player: str = self.first_player()

    def show_board(self) -> None:
        """
        Print the current state of the game board.
        """
        print(f'{self.board[1]} | {self.board[2]} | {self.board[3]}')
        print("----------")
        print(f'{self.board[4]} | {self.board[5]} | {self.board[6]}')
        print("----------")
        print(f'{self.board[7]} | {self.board[8]} | {self.board[9]}')

    def first_player(self) -> str :
        """
        Randomly select the first player.
        """
        return random.choice(['O', 'X'])

    def switch_player(self) -> None:
        """
        Switch the turn to the other player.
        """
        self.player ='O 'if self.player == 'X' else 'X'

    def choice(self) -> None:
        """
        Fix player choice on the board.
        """
        try:
            choice = int(input("Enter number of block : "))
            if choice in range(1, 10) and self.board[choice] not in ['O', 'X']:
                self.board[choice] = self.player
            else:
                print("choose the empty blocks(1-9)!")
        except ValueError:
            print("Invalid input, next player please enter a number between 1 and 9.")

    def is_board_full(self) -> bool:
        """
        Check if the board is full.
        """
        return ' ' not in self.board[1:]
    
    def player_won(self, player: str) -> bool:
        """
        Check if the current player has won the game.

        :param str player: The current player.
        :return: None
        """
        win_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]
        ]
        return any(all(self.board[cell] == player for cell in combo) for combo in win_combinations)
        
    def start(self) -> None:
        """
        Start the game loop and handle player turns until
        a player wins or the game ends in a draw.
        """
        print("Welcome to the Tic Tac Toe game")
        while not(self.is_board_full()):
            self.show_board()
            print(f"It's {self.player} turn: ")
            self.choice()
            if self.player_won(self.player):
                print(f"{self.player} Won! end of the game")
                self.show_board()
                break
            self.switch_player()
        else:
            print("DRAW! end of the game")
            self.show_board()

        
if __name__ == '__main__':
    game = TicTacToe()
    game.start()
