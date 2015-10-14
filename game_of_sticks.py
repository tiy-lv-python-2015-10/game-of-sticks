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
        #current_player = player1
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
        self.running = False
        print("Game over! {} wins and {} loses".format(winner, loser))
        if isinstance(winner, Ai):
            winner.append_win()
        if isinstance(loser, Ai):
            loser.append_loss()

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


class Ai(Player):

    def __init__(self, y):
        super().__init__(y)
        self.hats = {num: [1, 2, 3] for num in range(1, 101)}
        self.dump = {}

    def __str__(self):
        return "Robot"

    def choose_num(self, num_sticks):
        num_choice = 0
        while num_choice == 0:
            try:
                if num_sticks == 1:
                    choice = int(input("Enter 1 to pick up the last stick! > "))
                    if choice == 1:
                        self.dump[num_sticks] = choice
                        return choice
                    else:
                        print("One stick is your only option loser!")
                elif num_sticks == 2:
                    choice = int(input("How many sticks do you want to pick up? (1-2) > "))
                    if 1 <= choice <= 2:
                        self.dump[num_sticks] = choice
                        return choice
                    else:
                        print("Only 1 or 2 sticks please.")
                else:
                    choice = int(input("How many sticks do you want to pick up? (1-3) > "))
                    if 1 <= choice <= 3:
                        self.dump[num_sticks] = choice
                        return choice
                    else:
                        print("Only a number 1 - 3")
            except ValueError:
                print("Please enter only a number")

    def append_win(self):
        for hat, values in self.hats.items():
            for thing, choice in self.dump.items():
                if hat == thing:
                    values.append(choice)
        self.dump = {}

    def append_loss(self):
        for hat, values in self.hats.items():
            for thing, choice in self.dump.items():
                if hat == thing:
                    if values.count(choice) > 1:
                        values.remove(choice)
                        values.sort()
        self.dump = {}

if __name__ == '__main__':
    Peter = Player('Pete')
    Adam = Player('Adam')
    #new_game = Game()
    #new_game.play_game(Peter, Adam)
    Robot = Ai("Mr. Robot")
    game2 = Game()
    game2.play_game(Peter, Robot)
    print(Robot.dump)
    print(Robot.hats)
    game3 = Game()
    game3.play_game(Peter, Robot)
    print(Robot.dump)
    print(Robot.hats)
    game4 = Game()
    game5 = Game()
    game4.play_game(Peter, Robot)
    print(Robot.dump)
    print(Robot.hats)
    game5.play_game(Peter, Robot)
    print(Robot.dump)
    print(Robot.hats)


    #print(Robot.hats)
    #print(type(Robot))
    #if isinstance(Robot, Ai):
        #print("YES YES YES ")
    #print(Robot)