import random
import time


class Play:
    board = {'1': ' ', '2': ' ', '3': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '7': ' ', '8': ' ', '9': ' '}

    def print_board(self):
        print(self.board['1'] + '|' + self.board['2'] + '|' + self.board["3"])
        print('-+-+-')
        print(self.board['4'] + '|' + self.board['5'] + '|' + self.board["6"])
        print('-+-+-')
        print(self.board['7'] + '|' + self.board['8'] + '|' + self.board["9"])

    def player_user_x(self):
        spot = input("Place an X at a location: ")
        while self.board[spot] != ' ':
            print("Spot already taken, please pick another: ")
            spot = input()
        self.board[spot] = 'X'

    def computer_user_y(self):
        comp_spot = str(random.randint(1, 9))
        while self.board[comp_spot] != ' ':
            comp_spot = str(random.randint(1, 9))
        self.board[comp_spot] = 'O'

    def playing(self):
        count_x = 0
        count_y = 0
        self.print_board()
        for i in range(0, 9):
            self.player_user_x()
            print("Result:")
            self.print_board()
            count_x += 1
            if count_x + count_y == 9:
                self.print_board()
                print("Game ended in a tie, no winner!")
                break
            if count_x >= 3:
                if self.board['1'] == self.board['2'] == self.board['3'] != ' ':
                    self.print_board()
                    print(f"Player {self.board['1']} has won!")
                    break
                elif self.board['4'] == self.board['5'] == self.board['6'] != ' ':
                    self.print_board()
                    print(f"Player {self.board['4']} has won!")
                    break
                elif self.board['7'] == self.board['8'] == self.board['9'] != ' ':
                    self.print_board()
                    print(f"Player {self.board['7']} has won!")
                    break
                elif self.board['1'] == self.board['5'] == self.board['9'] != ' ':
                    self.print_board()
                    print(f"Player {self.board['1']} has won!")
                    break
                elif self.board['2'] == self.board['5'] == self.board['8'] != ' ':
                    self.print_board()
                    print(f"Player {self.board['2']} has won!")
                    break
                elif self.board['3'] == self.board['6'] == self.board['9'] != ' ':
                    self.print_board()
                    print(f"Player {self.board['3']} has won!")
                    break
                elif self.board['3'] == self.board['5'] == self.board['7'] != ' ':
                    self.print_board()
                    print(f"Player {self.board['3']} has won!")
                    break
                elif self.board['1'] == self.board['4'] == self.board['7'] != ' ':
                    self.print_board()
                    print(f"Player {self.board['7']} has won!")
                    break
            print("Computer is thinking about their move...")
            time.sleep(5)
            self.computer_user_y()
            self.print_board()
            count_y += 1
            if count_y >= 3:
                if self.board['1'] == self.board['2'] == self.board['3'] != ' ':
                    self.print_board()
                    print(f"Player {self.board['1']} has won!")
                    break
                elif self.board['4'] == self.board['5'] == self.board['6'] != ' ':
                    self.print_board()
                    print(f"Player {self.board['4']} has won!")
                    break
                elif self.board['7'] == self.board['8'] == self.board['9'] != ' ':
                    self.print_board()
                    print(f"Player {self.board['7']} has won!")
                    break
                elif self.board['1'] == self.board['5'] == self.board['9'] != ' ':
                    self.print_board()
                    print(f"Player {self.board['1']} has won!")
                    break
                elif self.board['2'] == self.board['5'] == self.board['8'] != ' ':
                    self.print_board()
                    print(f"Player {self.board['2']} has won!")
                    break
                elif self.board['3'] == self.board['6'] == self.board['9'] != ' ':
                    self.print_board()
                    print(f"Player {self.board['3']} has won!")
                    break
                elif self.board['3'] == self.board['5'] == self.board['7'] != ' ':
                    self.print_board()
                    print(f"Player {self.board['3']} has won!")
                    break
                elif self.board['1'] == self.board['4'] == self.board['7'] != ' ':
                    self.print_board()
                    print(f"Player {self.board['7']} has won!")
                    break


if __name__ == '__main__':
    game = Play()
    game.playing()

