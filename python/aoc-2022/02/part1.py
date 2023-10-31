# Advent of Code 2022 - Day 2 Part 1
# 4 Dec 2022 Brian Green
#
# Problem:
# Rock, paper, scissors

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip().split() for num in data_file.readlines()]

# print(data_set)

# A = X = Rock
# B = Y = Paper
# C = Z = Scissors
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.

play_vals = {"X": 1, "Y": 2, "Z": 3}

scores = {
    0: [["A", "Z"], ["C", "Y"], ["B", "X"]],
    3: [
        [
            "A",
            "X",
        ],
        ["B", "Y"],
        ["C", "Z"],
    ],
    6: [["C", "X"], ["B", "Z"], ["A", "Y"]],
}

total = 0

for play in data_set:
    total += play_vals[play[1]]
    for key in scores:
        if play in scores[key]:
            total += key

print(total)
