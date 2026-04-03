import random
import time

class TicTacToe:
    def __init__(self):
        self.board = ["-"] * 9
        self.crosses = "x"
        self.noughts = "○"
        self.win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)              # Diagonal
        ]

    def display_board(self):
        print(f"{self.board[0]} {self.board[1]} {self.board[2]}")
        print(f"{self.board[3]} {self.board[4]} {self.board[5]}")
        print(f"{self.board[6]} {self.board[7]} {self.board[8]}")

    def get_available_moves(self):
        return [i for i, val in enumerate(self.board) if val == "-"]

    def my_turn(self, player_mark):
        time.sleep(0.5)
        print("Your turn.")
        time.sleep(0.2)
        print("Please enter the place to put it from 1-9.")
        user_input = input("> ")
        while True:
            if not user_input.isdigit() or int(user_input) < 1 or int(user_input) > 9:
                print("Please enter only numbers from 1 to 9.")
                user_input = input("> ")
                continue
            
            move = int(user_input) - 1
            if move not in self.get_available_moves():
                print("Already entered place.")
                user_input = input("> ")
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
        return "-" not in self.board

    def play(self):
        print("Welcome to Tic-tac-toe!")
        time.sleep(0.5)
        
        turn_input = input("Enter 1 for the first move and 2 for the second move:")
        while turn_input not in ["1", "2"]:
            print("Please enter 1 or 2.")
            turn_input = input("> ")
        turn = int(turn_input)
            
        if turn == 1:
            print("You are the first player.")
            my_mark = self.crosses
            enemy_mark = self.noughts
        else:
            print("You are the Second player.")
            my_mark = self.noughts
            enemy_mark = self.crosses

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
            
            is_my_turn = (current_step % 2 == 1 and turn == 1) or (current_step % 2 == 0 and turn == 2)

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
                
            current_step += 1

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
