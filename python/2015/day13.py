# python day13.py ../../data/2015/day13.dat

import itertools
import sys

happiness = {}


def get_happy_path(data):
    global happiness
    for happy in data:
        level = happy.split()
        person = level[0]
        change = level[2]
        gain_loss = 1
        if change == "lose":
            gain_loss = -1
        units = int(level[3]) * gain_loss
        neighbor = level[-1][:-1]
        if person in happiness:
            happiness[person][neighbor] = units
        else:
            happiness[person] = {neighbor: units}


def get_happy(people, total_people):
    left = -1
    right = 1
    happy_people = {p: 0 for p in people}

    for p in people:
        happy_people[p] += happiness[p][people[left]] + happiness[p][people[right]]
        left += 1
        right += 1
        if right >= total_people:
            right = 0

    return sum(happy_people.values())


def parse_input(input_data):
    """
    Parse the input data from the Advent of Code problem.
    Edit this function to fit the day's input format.
    """
    return input_data.strip().split("\n")


def part1(data):
    happiness.clear()
    get_happy_path(data)
    people = list(happiness.keys())
    total_people = len(people)
    most_happy = 0
    all_combos = list(itertools.permutations(people))
    for combo in all_combos:
        total_happiness = get_happy(list(combo), total_people)
        if total_happiness > most_happy:
            most_happy = total_happiness

    return most_happy


def part2(data):
    happiness.clear()
    get_happy_path(data)

    happiness["Brian"] = {}
    for p in happiness:
        happiness[p]["Brian"] = 0
        happiness["Brian"][p] = 0

    people = list(happiness.keys())
    total_people = len(people)
    most_happy = 0
    all_combos = list(itertools.permutations(people))
    for combo in all_combos:
        total_happiness = get_happy(list(combo), total_people)
        if total_happiness > most_happy:
            most_happy = total_happiness

    return most_happy


if __name__ == "__main__":
    # Read input file or use test string
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        # Example test input, replace with actual test data
        input_data = """\
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
"""

    data = parse_input(input_data)
    print("Day 13 Part 1:", part1(data))
    print("Day 13 Part 2:", part2(data))
