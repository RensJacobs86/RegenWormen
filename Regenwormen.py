import random

dice = ["1", "2", "3", "4", "5", "Worm"]
board = [{21: 1}, {22: 1}, {23: 1}, {24: 1}, {25: 2}, {26: 2}, {27: 2}, {28: 2}, {29: 3}, {30: 3}, {31: 3}, {32: 3}, {33: 4}, {34: 4}, {35: 4}, {36: 4}]

class Player:

    def __init__(self, name):
        self.name = name
        self.hand_die = []
        self.hand_worm = []


    def turn(self):
        num_dice = 8

        while num_dice > 0:
            dice_throw = []
            points = 0
            for dices in range(num_dice):
                dice_throw.append(random.choice(dice))
            dice_throw.sort()
            print(f"{self.name} throws the dice")
            print(dice_throw)

            #check to see if a player can select a die
            you_lost = all(die in self.hand_die for die in dice_throw)
            if you_lost:
                print(f"{self.name} lost this turn!")
                del board[-1]
                print(board)
                self.hand_die = []
                break

            keep = str(input("Which dice do you want to keep? ")).title()
            #while loop so a player can't select the same dice twice
            while keep in self.hand_die:
                print("You already took those, please select another")
                print(dice_throw)
                keep = str(input("Which dice do you want to keep? ")).title()

            #while loop to prevent invalid input
            while keep not in dice_throw:
                print("Invalid input, please select another")
                keep = str(input("Which dice do you want to keep? ")).title()

            #for loop to put dices in the players hand
            for die in dice_throw:
                if die == keep:
                    self.hand_die.append(die)

            num_chosen_dices = dice_throw.count(keep)
            num_dice -= num_chosen_dices
            print(f"These are {self.name} chosen dices")
            self.hand_die.sort()
            print(self.hand_die)
            print(f"{self.name} has {num_dice} dices left")

            #loop to count the total points in hand
            for die in self.hand_die:
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

            print(f"{self.name} total hand is worth {points} points")
            if num_dice == 0 and "Worm" not in self.hand_die:
                print(f"{self.name} lost, he has no dice left and no worms")
                del board[-1]
                print(board)
                break

            #while loop to check for valid input
            throw_again = input("Do you want to continue throwing? ")
            while throw_again != "yes" and throw_again != "no":
                print("invalid input, please select yes or no")
                throw_again = input("Do you want to continue throwing? ")

            #while loop so you can't throw new dices when you have no dices left
            while num_dice == 0 and "Worm" in self.hand_die and throw_again == "yes":
                print("Invalid input, you have no dice left")
                throw_again = input("Do you want to continue throwing? ")
                continue

            if throw_again == "yes":
                continue
            elif throw_again == "no" and "Worm" not in self.hand_die:
                print("You lose, you have no Worms")
                del board[-1]
                print(board)
                break

            else:
                #show selectable stones
                stone_choice = []
                for stone in board:
                    for key, value in stone.items():
                        if points >= key:
                            stone_choice.append(stone)
                print("you can choose the following stones")
                print(stone_choice)
                stone_keep = input("Which stone do you want to keep? ")

                #loop to prevent wrong choice
                temp_stone_list = []
                for stone in stone_choice:
                    for key, value in stone.items():
                        temp_stone_list.append(key)
                while int(stone_keep) not in temp_stone_list:
                        print("Invalid stone, please select another")
                        stone_keep = input("Which stone do you want to keep? ")

                #adding a stone to the players hand
                for stone in board:
                    for key, value in stone.items():
                        if key == int(stone_keep):
                            self.hand_worm.append(stone)
                            self.hand_die = []


                #loop to remove the chosen stone from the board
                for index, stone in enumerate(self.hand_worm):
                    if stone in board:
                        board.remove(stone)
                print(f"this is {self.name}'s hand {self.hand_worm}")
                print("the following stones are left on the board")
                print(board)
                break




p1 = Player("Player 1")
p2 = Player("Player 2")
while len(board) > 0:
    p1.turn()
    p2.turn()