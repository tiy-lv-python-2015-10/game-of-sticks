class Player:
    def __init__(self):
        self.pick_up = 0

    def how_many(self):
        pick_up = input("How many sticks do you take (1-3)? ")
        if 1 <= int(pick_up) <= 3:
            self.pick_up = pick_up


class Game:
    player1 = ""
    player2 = ""

    def __init__(self):
        self.starting_amount = 0
        self.round_amount = 0

    def player_entry(self):
        self.player1 = input("Enter name: ")
        self.player2 = input("Enter name: ")

    def stick_amount(self):
        print("Welcome to the Game of Sticks!")
        starting_amount = int(input("How many sticks are there on the table initially (10-100)?"))
        if 10 <= starting_amount <= 100:
            pass
        else:
            print("Between 10 and 100... not {}".format(starting_amount))
        self.starting_amount = starting_amount

    def sticks_left(self, taken):
        self.round_amount = self.starting_amount - int(taken)

    def __str__(self):
        return self.round_amount


if __name__ == '__main__':
    players = Player()
    game = Game()
    game.player_entry()
    game.stick_amount()
    while True:
        sticks_taken = players.how_many()
        print(game)
        if game == 0:
            break