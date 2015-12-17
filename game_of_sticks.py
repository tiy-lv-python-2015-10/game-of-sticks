print("Welcome to the Game of Sticks")


class Game:

    def __init__(self):
        self.play_game = False
        self.total_sticks = 100

    def choose(self):
        """lets players decided how many sticks to start game with"""
        while True:
            stick_count = int(input("how many sticks do you want to start with?(10-100) "))
            if 10 <= stick_count <= 100:
                return stick_count
            else:
                print("enter a number between 10 and 100")

    def start_game(self, player_one, player_two):
        """starts game and prints who turn it is and shows how many sticks are left to pick up. also
        ends games if their is no more sticks left to pick up."""
        self.play_game = True
        self.total_sticks = self.choose()
        while self.play_game:
            print("{} turn".format(player_one))
            self.rounds()
            self.total_sticks -= Players.players_choice(player_one)
            if self.total_sticks <= 0:
                self.game_ends(player_two)
                self.play_again()
                break
            print("{} turn".format(player_two))
            self.rounds()
            self.total_sticks -= Players.players_choice(player_two)
            if self.total_sticks <= 0:
                self.game_ends(player_one)
                self.play_again()

    def play_again(self):
        while True:
            again = input("play again? yes or no? ")
            if again == "yes":
                self.start_game(player_one, player_two)
            else:
                print("thanks for playing")
            break

    def game_ends(self, players):
        """ends game and prints winner"""
        self.play_game = False
        print("{} wins".format(players))

    def rounds(self):
        """tells players how many sticks are left"""
        if self.total_sticks == 1:
            print("{} sticks left".format(self.total_sticks))
        else:
            print("{} sticks left". format(self.total_sticks))


class Players:
    def __init__(self, name):
        self.name = name

    def players_choice(self):
        """lets player pick how many sticks to pick up"""
        while True:
            choice = int(input("pick a number between 1 and 3: "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("please inter and number between 1 and 3")


if __name__ == '__main__':
    player_one = "player one"
    player_two = "player two"
    a_game = Game()
    a_game.start_game(player_one, player_two)






