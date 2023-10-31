# Advent of Code 2022 - Day 2 Part 2
# 4 Dec 2022 Brian Green
#
# Problem:
# Rock, paper, scissors

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip().split() for num in data_file.readlines()]

# print(data_set)

# A = Rock
# B = Paper
# C = Scissors
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

outcome = {"X": 0, "Y": 3, "Z": 6}

scores = {
    "A": {"X": 3, "Y": 1, "Z": 2},
    "B": {"X": 1, "Y": 2, "Z": 3},
    "C": {"X": 2, "Y": 3, "Z": 1},
}

total = 0

for play in data_set:
    total += outcome[play[1]]
    total += scores[play[0]][play[1]]

print(total)
