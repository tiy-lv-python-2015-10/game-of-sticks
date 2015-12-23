print("Welcome to the Game of Sticks!")


class Game:

    def __init__(self):
        self.game_play = False
        self.game_sticks = 100

    def game_sticks_chosen(self):
        user_num = 0
        while user_num == 0:
            try:
                user_num = int(input("How many sticks are there on the table initially (10-100)?"))
                if 10 <= user_num <= 100:
                    return user_num
                else:
                    print("Please enter a number between 10 and 100")
            except ValueError:
                print("Told you to choose between 10 -100 sticks")

    def game_start(self, player_1, player_2):
        self.game_running = True
        self.game_sticks = self.game_sticks_chosen()
        while self.game_running:
            print("{}'s turn".format(player_1))
            # self.game_sticks_picked()
            self.game_sticks_removed(player_1.game_sticks_chosen(self.game_sticks))
            if self.game_sticks_empty():
                self.game_end(player_2)
                self.play_again()
                break
            print("{}'s turn".format(player_2))
            # self.game_sticks_picked()
            self.game_sticks_removed(player_2.game_sticks_chosen(self.game_sticks))
            if self.game_sticks_empty():
                self.game_end(player_1)
                self.play_again()

    def game_end(self, player):
        self.game_running = False
        print("{} wins".format(player))

    def play_again(self):
        while True:
            again = input("play again? yes or no?")
            if again == "yes":
                self.game_start(player_1, player_2)
            else:
                print("Thank you for playing")
            break

    def game_sticks_empty(self):
        if self.game_sticks <= 0:
            return True

    def game_sticks_removed(self):
        if self.game_sticks == 1:
            print("{} stick(s) remaining".format(self.game_sticks))
        else:
            print("{} stick(s) remaining".format(self.game_sticks))


class Player:

    def __init__(self, name):
        self.name = name

    def __str__(self, name):
        return self.name

    def game_play(self):
        user_num = 0
        while user_num == 0:
            num = int(input("How many sticks do you take (1-3)? "))
            if 1 <= num <= 3:
                return num
            else:
                print("Please enter a number between 1 and 3")



if __name__== "__main__":
    player_1 = "player_1"
    player_2 = "player_2"
    game_new = Game()
    game_new.game_play(player_1, player_2)

