print("Welcome to the Game of Sticks!")


class Game:
    def __init__(self, player1, player2):
        self.user_choice = input("How many sticks are there on the table initially (10-100)? \n")
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1
        self.number_of_sticks = 100
        self.winner = True
        self.choice = 0

    def start(self):
        self.get_sticks()
        while self.number_of_sticks > 1:
            self.get_choice()
            self.number_of_sticks -= self.choice
            if self.number_of_sticks != 1:
                print("There are {} sticks left on the board".format(self.number_of_sticks))
            self.switch_players()
        if self.number_of_sticks <= 0:
            print("{} wins".format(self.current_player))
        else:
            self.get_winner()
            print("There is one stick left on the board, {} wins".format(self.winner))

    def get_choice(self):
        self.user_choice = input("{}, how many sticks would you like to pick up (1 - 3)? \n"
                                 .format(self.current_player))
        try:
            int(self.user_choice)
        except ValueError:
            print("Not a valid choice")
            self.get_choice()
        self.user_choice = int(self.user_choice)
        if 1 <= int(self.user_choice) <= 3:
            self.choice = self.user_choice
        else:
            print("Not a valid choice")
            self.get_choice()

    def get_sticks(self):
        try:
            int(self.user_choice)
            self.number_of_sticks = int(self.user_choice)
            if 10 <= int(self.user_choice) <= 100:
                return self.user_choice
        except ValueError:
            print("Not a valid choice")
            self.get_sticks()

    def get_winner(self):
        if self.current_player == self.player1:
            self.winner = self.player2
        else:
            self.winner = self.player1

    def switch_players(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1


class Player:
    def __init__(self, name="Player__"):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


if __name__ == '__main__':
    name1 = input("Player 1, What is your name? \n")
    name2 = input("Player 2, What is your name? \n")
    p1 = Player(name1)
    p2 = Player(name2)
    game = Game(p1, p2)
    game.start()
