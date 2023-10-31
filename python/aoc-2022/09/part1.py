# Advent of Code 2022 - Day 9 Part 1
# 9 Dec 2022 Brian Green
#
# Problem:
# Rope Bridge

import math
from collections import Counter

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip().split() for num in data_file.readlines()]

# print(data_set)

head_x = 0
head_y = 0
tail_x = 0
tail_y = 0

tracker = [
    (tail_x, tail_y),
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
        head_x += delta_x
        head_y += delta_y

        distance = int(math.dist([tail_x, tail_y], [head_x, head_y]))
        if distance < 2:
            pass
        else:
            if tail_y == head_y:
                pass
            elif head_y > tail_y:
                tail_y += 1
            else:
                tail_y -= 1

            if tail_x == head_x:
                pass
            elif head_x > tail_x:
                tail_x += 1
            else:
                tail_x -= 1

        tracker.append((tail_x, tail_y))
        # print(f"tail={tail_x},{tail_y} head={head_x},{head_y}")

print(len(Counter(tracker)))
