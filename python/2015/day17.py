# python day17.py ../../data/2015/day17.dat

import sys
import itertools


def parse_input(input_data):
    numbers = [int(x) for x in input_data.strip().split("\n")]
    return numbers


def part1(numbers):
    target = 150
    result = [
        seq
        for i in range(len(numbers), 0, -1)
        for seq in itertools.combinations(numbers, i)
        if sum(seq) == target
    ]
    return len(result)


def part2(numbers):
    target = 150
    result = [
        seq
        for i in range(len(numbers), 0, -1)
        for seq in itertools.combinations(numbers, i)
        if sum(seq) == target
    ]
    fewest = min(len(seq) for seq in result)
    return sum(1 for seq in result if len(seq) == fewest)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        input_data = """11
30
47
31
32
36
3
1
5
3
32
36
15
11
46
26
28
1
19
3
"""
    numbers = parse_input(input_data)
    print("Day 17 Part 1:", part1(numbers))
    print("Day 17 Part 2:", part2(numbers))
