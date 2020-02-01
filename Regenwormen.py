import random
import operator

dice = ["1", "2", "3", "4", "5", "Worm"]
board = [{"stone": 21, "points": 1}, {"stone": 22, "points": 1}, {"stone": 23, "points": 1}, {"stone": 24, "points": 1},
         {"stone": 25, "points": 2}, {"stone": 26, "points": 2}, {"stone": 27, "points": 2}, {"stone": 28, "points": 2},
         {"stone": 29, "points": 3}, {"stone": 30, "points": 3}, {"stone": 31, "points": 3}, {"stone": 32, "points": 3},
         {"stone": 36, "points": 4}, {"stone": 34, "points": 4}, {"stone": 35, "points": 4}, {"stone": 33, "points": 4}]


class Player:

    def __init__(self, name):
        self.name = name
        self.hand_die = []
        self.hand_worm = []
        self.hand_worm_end_display = []
        self.points = 0

    def turn(self):
        num_dice = 8
        self.hand_die = []
        board_display = []

        print("The following stones are left on the board")
        board.sort(key=operator.itemgetter("stone"))
        for stone in board:
            board_display.append((stone.get("stone"), stone.get("points")))
        print(board_display)

        for player in players:
            if len(player.hand_worm) == 0:
                print(f"{player.name} has no stones in his hand")
            elif len(player.hand_worm) == 1:
                print(f"{player.name} has {len(player.hand_worm)} stone")
                print("{} has {} on top".format(player.name, player.hand_worm[-1].get("stone")))
            else:
                print(f"{player.name} has {len(player.hand_worm)} stones")
                print("{} has {} on top".format(player.name, player.hand_worm[-1].get("stone")))

        while num_dice > 0:
            dice_throw = []
            points = 0
            for dices in range(num_dice):
                dice_throw.append(random.choice(dice))
            dice_throw.sort()
            print(f"{self.name} throws the dice")
            print(dice_throw)

            # check to see if a player can select a die
            you_lost = all(die in self.hand_die for die in dice_throw)
            if you_lost:
                print(f"{self.name} lost this turn!")
                del board[-1]
                if len(self.hand_worm) > 0:
                    board.append(self.hand_worm[-1])
                    del self.hand_worm[-1]
                break

            keep = input("Which dice do you want to keep?: ").title()
            # while loop so a player can't select the same dice twice
            while keep in self.hand_die:
                print("You already took those, please select another")
                print(dice_throw)
                keep = input("Which dice do you want to keep?: ").title()

            # while loop to prevent invalid input
            while keep not in dice_throw:
                print("Invalid input, please select another")
                keep = input("Which dice do you want to keep?: ").title()

            # for loop to put dices in the players hand
            for die in dice_throw:
                if die == keep:
                    self.hand_die.append(die)

            num_chosen_dices = dice_throw.count(keep)
            num_dice -= num_chosen_dices
            print(f"These are {self.name}'s chosen dices")
            self.hand_die.sort()
            print(self.hand_die)
            print(f"{self.name} has {num_dice} dices left")

            # loop to count the total dice points in hand
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
                if len(self.hand_worm) > 0:
                    board.append(self.hand_worm[-1])
                    del self.hand_worm[-1]
                break

            # while loop to check for valid input
            throw_again = input("Do you want to continue throwing?: ").lower()
            while throw_again != "yes" and throw_again != "no":
                print("invalid input, please select yes or no")
                throw_again = input("Do you want to continue throwing?: ").lower()

            # while loop so you can't throw new dices when you have no dices left
            while num_dice == 0 and "Worm" in self.hand_die and throw_again == "yes":
                print("Invalid input, you have no dice left")
                throw_again = input("Do you want to continue throwing?: ").lower()
                continue

            if throw_again == "yes":
                continue
            elif throw_again == "no" and "Worm" not in self.hand_die:
                print("You lose, you have no Worms")
                del board[-1]
                if len(self.hand_worm) > 0:
                    board.append(self.hand_worm[-1])
                    del self.hand_worm[-1]
                break

            else:
                # show selectable stones from the board
                stone_choice = []
                for stone in board:
                    for key, value in stone.items():
                        if key == "stone" and points >= value:
                            stone_choice.append((stone.get("stone"), stone.get("points")))
                # check to see if can steal a stone from another player
                for player in players:
                    if len(player.hand_worm) > 0 and player.hand_worm[-1].get("stone") == points \
                            and points != self.hand_worm[-1].get("stone"):
                        print(f"you can steal the following stone from {player.name}:")
                        stone_choice.append((player.hand_worm[-1].get("stone"), player.hand_worm[-1].get("points")))
                        print(f"{stone_choice[-1]}")

                if len(stone_choice) == 0:
                    print("you can't pick a stone, you lose")
                    del board[-1]
                    if len(self.hand_worm) > 0:
                        board.append(self.hand_worm[-1])
                        del self.hand_worm[-1]
                    break

                print("you can choose the following stones")
                print(stone_choice)
                stone_keep = input("Which stone do you want to keep?: ")

                # loop to prevent wrong choice
                temp_stone_list = []
                for stone in stone_choice:
                    temp_stone_list.append(stone[0])
                while stone_keep not in str(temp_stone_list) or int(stone_keep) not in temp_stone_list:
                    print("Invalid stone, please select another")
                    stone_keep = input("Which stone do you want to keep?: ")

                # adding a stone to the players hand
                for stone in board:
                    for key, value in stone.items():
                        if value == int(stone_keep):
                            self.hand_worm.append(stone)
                # loop to steal a stone from another player
                for player in players:
                    temp_stone_list = []
                    if len(player.hand_worm) > 0 and player.hand_worm[-1].get("stone") == int(stone_keep) \
                            and player.hand_worm[-1] not in self.hand_worm:

                        temp_stone_list.append(player.hand_worm[-1])
                        player.hand_worm.remove(player.hand_worm[-1])
                        self.hand_worm.append(temp_stone_list[0])
                        print(f"{self.name} stole a stone from {player.name}")

                # loop to remove the chosen stone from the board
                for stone in self.hand_worm:
                    if stone in board:
                        board.remove(stone)
                break

    def total_points(self):
        for x in self.hand_worm:
            for key, value in x.items():
                if key == "points":
                    self.points += value

        print(f"{players[index].name} shows his worms")
        for stone in self.hand_worm:
            self.hand_worm_end_display.append((stone.get("stone"), stone.get("points")))
        print(self.hand_worm_end_display)
        print(f"{players[index].name} has {players[index].points} points")


player_names = []
players = []

num_players = input("How many players are playing?: ")
while not num_players.isnumeric():
    print("invalid input, please select a number")
    num_players = input("How many players are playing?: ")

for index in range(int(num_players)):
    player_names.append(input(f"Please enter the name of player {index+1}: ").title())

for player_name in player_names:
    players.append(Player(player_name))

while len(board) > 0:
    for index in range(len(players)):
        players[index].turn()
        if len(board) == 0:
            break

for index in range(len(players)):
    players[index].total_points()
