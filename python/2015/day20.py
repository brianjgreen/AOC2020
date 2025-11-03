# python day20.py ../../data/2015/day20.dat

import sys


def parse_input(input_data):
    return int(input_data.strip())


def part1(min_presents):
    house = 0
    presents = 0
    while presents < min_presents:
        presents = 0
        house += 1
        for i in range(1, int(house ** 0.5) + 1):
            if house % i == 0:
                presents += i * 10
                if i != house // i:
                    presents += (house // i) * 10
    return house


def part2(min_presents):
    house = 0
    presents = 0
    while presents < min_presents:
        presents = 0
        house += 1
        for i in range(1, int(house ** 0.5) + 1):
            if house % i == 0:
                if i * 50 >= house:
                    presents += i * 11
                if i != house // i and (house // i) * 50 >= house:
                    presents += (house // i) * 11
    return house


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        input_data = ""
    input_data = parse_input(input_data)
    print("Day 20 Part 1:", part1(input_data))
    print("Day 20 Part 2:", part2(input_data))
