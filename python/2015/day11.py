# python day11.py ../../data/2015/day11.dat

import string
import sys


def parse_input(input_data):
    """
    Parse the input data from the Advent of Code problem.
    Edit this function to fit the day's input format.
    """
    return input_data.strip().split("\n")


# Password Rule 1
straight = []
alpha = string.ascii_lowercase
while len(alpha) > 2:
    straight.append(alpha[:3])
    alpha = alpha[1:]

# Password Rule 2
banned = ["i", "o", "l"]

# Password Rule 3
pairs = []
alpha = list(string.ascii_lowercase)
while len(alpha) > 0:
    letter = alpha.pop(0)
    pairs.append(letter + letter)


def is_valid(password):
    for b in banned:
        if b in password:
            return False

    good = False
    for s in straight:
        if s in password:
            good = True
            break
    if not good:
        return False

    count = 0
    for p in pairs:
        if p in password:
            count += 1
    if count < 2:
        return False

    return True


def increment_letter(letter):
    b = bytes(letter, "utf-8")
    b = b[0] + 1
    return chr(b)


def increment_password(password):
    index = -1
    if password[index] == "z":
        password = increment_password(password[:-1]) + "a"
    else:
        password = password[:-1] + increment_letter(password[index])

    return password


def get_next_valid_password(password):
    while not is_valid(password):
        # print(password)
        password = increment_password(password)
    return password


def part1(data):
    return get_next_valid_password(data[0])


def part2(data):
    return get_next_valid_password(increment_password(data))


if __name__ == "__main__":
    # Read input file or use test string
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        # Example test input, replace with actual test data
        input_data = """\
abcdefgh
"""

    data = parse_input(input_data)
    password = part1(data)
    print("Day 11 Part 1:", password)
    print("Day 11 Part 2:", part2(password))
