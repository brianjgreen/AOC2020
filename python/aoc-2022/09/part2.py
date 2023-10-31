# Advent of Code 2022 - Day 9 Part 2
# 9 Dec 2022 Brian Green
#
# Problem:
# Rope Bridge, 10 knots

import math
from collections import Counter

# filename = "test.dat"
# filename = "test2.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip().split() for num in data_file.readlines()]

# print(data_set)

knots = []
for k in range(10):
    knots.append([0, 0])

tracker = [
    (0, 0),
]


def move_it(direction):
    delta_x = 0
    delta_y = 0
    if direction == "U":
        delta_y = 1
    elif direction == "D":
        delta_y = -1
    elif direction == "R":
        delta_x = 1
    elif direction == "L":
        delta_x = -1
    else:
        print("UNKNOWN DIRECTION!")

    return (delta_x, delta_y)


for direction, steps in data_set:
    # print(f"{direction} {steps}")
    for move in range(int(steps)):
        delta_x, delta_y = move_it(direction)
        knots[0][0] += delta_x
        knots[0][1] += delta_y

        for k in range(len(knots) - 1):
            distance = int(
                math.dist(
                    [knots[k + 1][0], knots[k + 1][1]], [knots[k][0], knots[k][1]]
                )
            )
            if distance < 2:
                pass
            else:
                if knots[k + 1][1] == knots[k][1]:
                    pass
                elif knots[k][1] > knots[k + 1][1]:
                    knots[k + 1][1] += 1
                else:
                    knots[k + 1][1] -= 1

                if knots[k + 1][0] == knots[k][0]:
                    pass
                elif knots[k][0] > knots[k + 1][0]:
                    knots[k + 1][0] += 1
                else:
                    knots[k + 1][0] -= 1

        tracker.append((knots[9][0], knots[9][1]))

print(len(Counter(tracker)))
