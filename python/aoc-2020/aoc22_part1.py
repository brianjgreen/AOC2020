#
# Advent of Code 2020 - Day 22 Part 1
# 22 Dec 2020 Brian Green
#
# Problem:
# Play the small crab in a game of Combat using the two decks you just dealt. What is the winning player's score?
#
import os


class Aoc22:
    def __init__(self):
        test_player_1 = [9, 2, 6, 3, 1]
        test_player_2 = [5, 8, 4, 7, 10]

        file_name = "data" + os.sep + "brian_aoc22_p1.dat"
        with open(file_name) as data_file:
            data_player_1 = [int(x.strip()) for x in data_file.readlines()]

        file_name = "data" + os.sep + "brian_aoc22_p2.dat"
        with open(file_name) as data_file:
            data_player_2 = [int(x.strip()) for x in data_file.readlines()]

        # self.player_1 = test_player_1
        # self.player_2 = test_player_2
        self.player_1 = data_player_1
        self.player_2 = data_player_2

    def run_it(self):
        print(self.player_1)
        print(self.player_2)
        while len(self.player_1) > 0 and len(self.player_2) > 0:
            p1 = self.player_1.pop(0)
            p2 = self.player_2.pop(0)
            if p1 > p2:
                self.player_1.append(p1)
                self.player_1.append(p2)
            else:
                self.player_2.append(p2)
                self.player_2.append(p1)
        print(self.player_1)
        print(self.player_2)

        if len(self.player_1) > 0:
            calc = self.player_1
        else:
            calc = self.player_2

        total = 0
        for i in range(len(calc)):
            total += (len(calc) - i) * calc[i]
        print(total)


if __name__ == "__main__":
    solve_it = Aoc22()
    solve_it.run_it()
