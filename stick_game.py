class Player:
    def __init__(self,player_num):
        self.player_num = player_num
        pass

    def remove_stick(self):
        sticks_removen = int(input(("Player {}: How many sticks do you take (1-3)? :".format(self.player_num))))
        return sticks_removen

class Game():
    def __init__(self, first_player, second_player):
        self.greeting = "Welcome to the game of sticks!"
        self.stick_amount = int(input("How many sticks are there on the table initially (10-100)? "))
        self.first_player = first_player
        self.second_player = second_player
        self.start_game()

    def main_game(self):
        print(self.greeting)
        while self.stick_amount >= 0:
            self.sticks_chosen = self.first_player.remove_stick()
            self.stick_amount -= self.sticks_chosen
            if self.stick_amount <= 1:
                print("you lose player 1")
                break
            else:
                print("There are",self.stick_amount, "sticks on the board.")

            self.sticks_chosen = self.second_player.remove_stick()
            self.stick_amount -= self.sticks_chosen
            if self.stick_amount <= 0:
                print("you lose player 2")
                break
            else:
                print("There are",self.stick_amount, "sticks on the board.")

    def start_game(self):
        self.main_game()


if __name__ == '__main__':

    player1 = Player(1)
    player2 = Player(2)
    new_game = Game(player1, player2)
    new_game.start_game()




