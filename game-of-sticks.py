print("Welcome to the Game of Sticks!")

stick_num = []
for sticks_num in range(10, 100):

    while sticks_num > 0:
        remove = int(input("Take between (1-3) sticks"))
        if remove > 4:
            print("That's too many sticks")
        elif remove < 1:
            print("That's not enough sticks")
        elif remove == 1 or 2 or 3:
            stick_num -= remove
        if sticks_num > 0:
            print("you have ", {}, "sticks left")

    print("You lose")

input()