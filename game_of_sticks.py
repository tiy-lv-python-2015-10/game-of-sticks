import random


class Game:

    def __init__(self):
        self.running = False
        self.num_sticks = 100

    def setup(self):
        """
        Sets up game vs. friend or computer
        :return: String to use in comparison
        """
        user_choice = 0
        while user_choice == 0:
            print("Options:")
            print("    Play against a friend (1)")
            print("    Play against a computer (2)")
            try:
                user_choice = int(input("Which option do you take? (1 or 2)"))
                if user_choice == 1:
                    return 'friend'
                elif user_choice == 2:
                    return 'comp'
                else:
                    user_choice = 0
            except ValueError:
                print("Please enter only a number 1 - 2")

    def choose_num_sticks(self):
        """
        Request number of sticks to start game
        :return: int between 10-100
        """
        user_num = 0
        while user_num == 0:
            try:
                user_num = int(input("How many sticks do you want in the game? (10-100) > "))
                if 10 <= user_num <= 100:
                    return user_num
                else:
                    print("Only a number 10 - 100")
                    user_num = 0
            except ValueError:
                print("Please enter only a number 10 - 100")

    def play_game(self, player1, player2):
        """
        Game Function.
        :param player1: Player type or Ai inheritance
        :param player2: Player type or Ai inheritance
        :return:
        """
        print("Welcome to the Game of Sticks")
        self.running = True
        self.num_sticks = self.choose_num_sticks()
        while self.running:
            print("{} it is your turn.".format(player1))
            self.show_sticks()
            self.remove_sticks(player1.choose_num(self.num_sticks))
            if self.is_sticks_empty():
                self.end_game(player2, player1)
            else:
                print("{} it is your turn.".format(player2))
                self.show_sticks()
                self.remove_sticks(player2.choose_num(self.num_sticks))
                if self.is_sticks_empty():
                    self.end_game(player1, player2)

    def end_game(self, winner, loser):
        """
        Ends game. Adds talent to robot
        :param winner: Player type or Ai inheritance
        :param loser: Player type or Ai inheritance
        :return:
        """
        self.running = False
        print("Game over! {} wins and {} loses".format(winner, loser))
        if isinstance(winner, Ai):
            winner.append_win()
        if isinstance(loser, Ai):
            loser.append_loss()

    def is_sticks_empty(self):
        """
        Checks to see if there are no more sticks
        :return: True if there are no more sticks
        """
        if self.num_sticks <= 0:
            return True

    def remove_sticks(self, turn_sticks):
        """
        Subtracts sticks in turn from game sticks left
        :param turn_sticks:
        :return: None
        """
        self.num_sticks -= turn_sticks

    def show_sticks(self):
        """
        prints how many sticks remaining
        :return: None
        """
        if self.num_sticks == 1:
            print("There is {} stick remaining".format(self.num_sticks))
        else:
            print("There are {} sticks remaining".format(self.num_sticks))

    def play_again(self):
        """
        returns boolean whether to play again or not
        :return: boolean
        """
        play = None
        while play is None:
            play = input("Would you like to play again? [Y]es or [N]o > ").lower()
            if play == 'y' or play == 'yes':
                return True
            elif play == 'n' or play == 'no':
                return False
            else:
                print("Only [Y]es or [N]o please")
                play = None


class Player:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def choose_num(self, num_sticks):
        """
        Prompts for a number between 1 - 3. Checks for good input
        :param num_sticks: int representing number of game sticks remaining
        :return: int of their choice (1-3) unless < 3 sticks remaining
        """
        num_choice = 0
        while num_choice == 0:
            try:
                if num_sticks == 1:
                    choice = int(input("Enter 1 to pick up the last stick! > "))
                    if choice == 1:
                        return choice
                    else:
                        print("One stick is your only option loser!")
                elif num_sticks == 2:
                    choice = int(input("How many sticks do you want to pick up? (1-2) > "))
                    if 1 <= choice <= 2:
                        return choice
                    else:
                        print("Only 1 or 2 sticks please.")
                else:
                    choice = int(input("How many sticks do you want to pick up? (1-3) > "))
                    if 1 <= choice <= 3:
                        return choice
                    else:
                        print("Only a number 1 - 3")
            except ValueError:
                print("Please enter only a number")


class Ai(Player):

    def __init__(self, y):
        super().__init__(y)
        self.hats = {num: [1, 2, 3] for num in range(1, 101)}
        self.dump = {}

    def __str__(self):
        return "Robot"

    def choose_num(self, num_sticks):
        """
        chooses num at random from its hats.
        :param num_sticks: number of sticks left in the game
        :return: int of random (1-3) if unless < 3 sticks remaining
        """
        if num_sticks == 1:
            choice = 1
            self.dump[num_sticks] = choice
            return choice
        elif num_sticks == 2:
            choice = 0
            while not 1 <= choice <= 2:
                choice = random.choice(self.hats[num_sticks])
                if not choice == 3:
                    self.dump[num_sticks] = choice
                    return choice
        else:
            choice = random.choice(self.hats[num_sticks])
            self.dump[num_sticks] = choice
            return choice

    def append_win(self):
        """
        Adds choices to hats if a winner
        :return: None
        """
        for hat, values in self.hats.items():
            for thing, choice in self.dump.items():
                if hat == thing:
                    values.append(choice)
        self.dump = {}

    def append_loss(self):
        """
        Subtracts choices from hats if loser. Leaves at least one instance of 1, 2, and 3 per hat
        :return: None
        """
        for hat, values in self.hats.items():
            for thing, choice in self.dump.items():
                if hat == thing:
                    if values.count(choice) > 1:
                        values.remove(choice)
                        values.sort()
        self.dump = {}

if __name__ == '__main__':
    happy = Player("Happy Gilmore")
    shooter = Player("Shooter McGavin")
    robot = Ai("Mr. Robot")

    new_game = Game()
    play_now = True
    game = new_game.setup()
    if game == 'friend':
        while play_now:
            new_game.play_game(happy, shooter)
            play_now = new_game.play_again()
    else:
        while play_now:
            new_game.play_game(happy, robot)
            print(robot.hats)
            play_now = new_game.play_again()
