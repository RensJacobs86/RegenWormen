import random

dice = ["1", "2", "3", "4", "5", "Worm"]
board = {21: 1, 22: 1, 23: 1, 24: 1, 25: 2, 26: 2, 27: 2, 28: 2, 29: 3, 30: 3, 31: 3, 32: 3, 33: 4, 34: 4, 35: 4, 36: 4}

def dice_roll():
    num_dice = 8
    hand_die = []
    hand_stone = {}


    while num_dice > 0:
        dice_throw = []
        points = 0
        for dices in range(num_dice):
            dice_throw.append(random.choice(dice))
        dice_throw.sort()
        print("You throw your dices")
        print(dice_throw)

        #check to see if a player can select a die
        you_lost = all(die in hand_die for die in dice_throw)
        if you_lost:
            print("you lose!")
            break

        keep = str(input("Which dice do you want to keep? ")).title()
        #while loop so a player can't select the same dice twice
        while keep in hand_die:
            print("You already took those, please select another")
            print(dice_throw)
            keep = str(input("Which dice do you want to keep? ")).title()

        #for loop to put dices in the players hand
        for die in dice_throw:
            if die == keep:
                hand_die.append(die)

        num_chosen_dices = dice_throw.count(keep)
        num_dice -= num_chosen_dices
        print("These are your chosen dices")
        hand_die.sort()
        print(hand_die)
        print(f"You have {num_dice} dices left")

        #if statment to count the total points in hand
        for die in hand_die:
            if die == "1":
                points += 1
            elif die == "2":
                points += 2
            elif die == "3":
                points += 3
            elif die == "4":
                points += 4
            elif die == "5":
                points += 5
            elif die == "Worm":
                points += 5

        print(f"your total hand is worth {points} points")

        #choice to continue throwing dices
        throw_again = input("Do you want to continue throwing? ")
        while throw_again != "yes" and throw_again != "no":
            print("invalid input, please select yes or no")
            throw_again = input("Do you want to continue throwing? ")
        if throw_again == "yes":
            continue
        else:
            #show selectable stones
            stone_choice = {}
            for worm_key, worm_value in board.items():
                if points >= worm_key and "Worm" in hand_die:
                    stone_choice[worm_key] = worm_value
            print("you can choose the following stones")
            print(stone_choice)
            stone_keep = input("Which stone do you want to keep? ")

            #loop to prevent wrong choice
            while int(stone_keep) not in stone_choice.keys():
                print("Invalid stone, please select another")
                stone_keep = input("Which stone do you want to keep? ")

            #adding a stone to your hand
            for worm_key, worm_value in board.items():
                if worm_key == int(stone_keep):
                    hand_stone[worm_key] = worm_value

            #loop to remove the chosen stone from the board
            for worm_key in hand_stone.keys():
                if worm_key in board:
                    del board[worm_key]
            print(f"this is your hand {hand_stone}")
            print("the following stones are left on the board")
            print(board)

            break


dice_roll()