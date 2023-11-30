#assign3, Q1
import random
def roll_two_dice():
    return random.randint(1, 6)
def craps():
    try1 = roll_two_dice()
    try2 = roll_two_dice()
    first_roll = try1 + try2
    print(f"You rolled {try1} + {try2} = {first_roll}")

    if first_roll in [7, 11]:
        print(first_roll)
        print("You win natural")
    elif first_roll in [2, 3, 12]:
        print("You lose")
    else:
        print(f"point is {first_roll}")
        while True:
            try1while = roll_two_dice()
            try2while = roll_two_dice()
            next_roll = try1while + try2while
            print(f"You rolled {try1while} + {try2while} = {next_roll}")

            if next_roll == 7:
                print("You've lost after point")
                break
            elif next_roll == first_roll:
                print("You've won after point")
                break
craps()
