import random
import time

class TicTacToe:
    EMPTY = "-"
    CROSS = "x"
    NOUGHT = "○"

    def __init__(self):
        self.board = [self.EMPTY] * 9
        self.win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)              # Diagonal
        ]

    def display_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} {self.board[i+1]} {self.board[i+2]}")

    def get_available_moves(self):
        return [i for i, val in enumerate(self.board) if val == self.EMPTY]

    def my_turn(self, player_mark):
        time.sleep(0.5)
        print("Your turn.")
        time.sleep(0.2)
        print("Please enter the place to put it from 1-9.")
        while True:
            user_input = input("> ")
            if not user_input.isdigit() or not (1 <= int(user_input) <= 9):
                print("Please enter only numbers from 1 to 9.")
                continue
            
            move = int(user_input) - 1
            if self.board[move] != self.EMPTY:
                print("Already entered place.")
                continue
            
            self.board[move] = player_mark
            self.display_board()
            break

    def enemy_turn(self, enemy_mark):
        time.sleep(0.5)
        print("AI turn.")
        available = self.get_available_moves()
        move = random.choice(available)
        self.board[move] = enemy_mark
        self.display_board()

    def check_winner(self, mark):
        for combo in self.win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == mark:
                return True
        return False

    def is_draw(self):
        return self.EMPTY not in self.board

    def play(self):
        print("Welcome to Tic-tac-toe!")
        time.sleep(0.5)
        
        while True:
            self.board = [self.EMPTY] * 9
            
            turn_input = input("Enter 1 for the first move and 2 for the second move:")
            while turn_input not in ["1", "2"]:
                print("Please enter 1 or 2.")
                turn_input = input("> ")
            turn = int(turn_input)
                
            if turn == 1:
                print("You are the first player.")
                my_mark = self.CROSS
                enemy_mark = self.NOUGHT
                is_my_turn = True
            else:
                print("You are the Second player.")
                my_mark = self.NOUGHT
                enemy_mark = self.CROSS
                is_my_turn = False

            print("1|2|3")
            print("4|5|6")
            print("7|8|9")
            print("Enter the location and the corresponding number.")
            time.sleep(1.0)
            print("----------------")
            self.display_board()

            current_step = 1
            while True:
                time.sleep(0.5)

                if current_step % 2 == 1:
                    print("TURN:" + str((current_step + 1) // 2))

                if is_my_turn:
                    self.my_turn(my_mark)
                    if self.check_winner(my_mark):
                        time.sleep(0.5)
                        print(f"{my_mark} WIN")
                        break
                else:
                    self.enemy_turn(enemy_mark)
                    if self.check_winner(enemy_mark):
                        time.sleep(0.5)
                        print(f"{enemy_mark} WIN")
                        break
                
                if self.is_draw():
                    print("DRAW")
                    break
                    
                is_my_turn = not is_my_turn
                current_step += 1
            
            print("Play again? (y/n)")
            retry = input("> ").lower()
            if retry != 'y':
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
