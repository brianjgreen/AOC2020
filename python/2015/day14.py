# python day14.py ../../data/2015/day14.dat

import sys

roster = {}


def get_roster(data):
    global roster
    for deer in data:
        stats = deer.split()
        name = stats[0]
        speed = int(stats[3])
        duration = int(stats[6])
        cooldown = int(stats[13])
        roster[name] = list(
            [speed for i in range(duration)] + [0 for i in range(cooldown)]
        )


def parse_input(input_data):
    """
    Parse the input data from the Advent of Code problem.
    Edit this function to fit the day's input format.
    """
    return input_data.strip().split("\n")


def part1(data):
    global roster
    roster.clear()
    get_roster(data)

    log = {deer: 0 for deer in roster}

    for t in range(2503):
        for deer in roster:
            log[deer] += roster[deer][t % len(roster[deer])]

    return max(log.values())


def part2(data):
    global roster
    roster.clear()
    get_roster(data)

    log = {deer: 0 for deer in roster}
    points = {deer: 0 for deer in roster}

    for t in range(2503):
        for deer in roster:
            log[deer] += roster[deer][t % len(roster[deer])]

        winner = max(log.values())
        awards = [k for k, v in log.items() if v == winner]
        for deer in awards:
            points[deer] += 1

    return max(points.values())


if __name__ == "__main__":
    # Read input file or use test string
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        # Example test input, replace with actual test data
        input_data = """\
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
"""

    data = parse_input(input_data)
    print("Day 14 Part 1:", part1(data))
    print("Day 14 Part 2:", part2(data))
