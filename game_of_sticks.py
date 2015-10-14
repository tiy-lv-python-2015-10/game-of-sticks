class Game:

    def __init__(self):
        self.running = False
        self.num_sticks = 100

    def choose_num_sticks(self):
        user_num = 0
        while user_num == 0:
            try:
                user_num = int(input("How many sticks do you want in the game? (10-100) > "))
                if 10 <= user_num <= 100:
                    return user_num
                else:
                    print("Only a number 10 - 100")
            except ValueError:
                print("Please enter only a number 10 - 100")

    def play_game(self, player1, player2):
        self.running = True
        self.num_sticks = self.choose_num_sticks()
        while self.running:
            print("{} it is your turn.".format(player1))
            self.show_sticks()
            self.remove_sticks(player1.choose_num(self.num_sticks))
            if self.is_sticks_empty():
                self.end_game(player2)
                break
            print("{} it is your turn.".format(player2))
            self.show_sticks()
            self.remove_sticks(player2.choose_num(self.num_sticks))
            if self.is_sticks_empty():
                self.end_game(player1)

    def end_game(self, player):
        self.running = False
        print("Game over! {} wins".format(player))

    def is_sticks_empty(self):
        if self.num_sticks <= 0:
            return True

    def remove_sticks(self, turn_sticks):
        self.num_sticks -= turn_sticks

    def show_sticks(self):
        if self.num_sticks == 1:
            print("There is {} stick remaining".format(self.num_sticks))
        else:
            print("There are {} sticks remaining".format(self.num_sticks))


class Player:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def choose_num(self, num_sticks):
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


if __name__ == '__main__':
    Peter = Player('Pete')
    Adam = Player('Adam')
    new_game = Game()
    new_game.play_game(Peter, Adam)
