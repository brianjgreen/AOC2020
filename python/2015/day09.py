# python day09.py ../../data/2015/day09.dat

import itertools
import sys

places = {}


def parse_input(input_data):
    """
    Parse the input data from the Advent of Code problem.
    Edit this function to fit the day's input format.
    """
    return input_data.strip().split("\n")


def get_paths(data):
    global places
    for trip in data:
        travel = trip.split()
        origin = travel[0]
        destination = travel[2]
        distance = int(travel[4])
        if origin in places:
            places[origin][destination] = distance
        else:
            places[origin] = {destination: distance}
        if destination in places:
            places[destination][origin] = distance
        else:
            places[destination] = {origin: distance}
    return list(places.keys())


def get_distance(path):
    distance = 0
    origin = path.pop(0)
    while len(path) > 0:
        destination = path.pop(0)
        distance += places[origin][destination]
        origin = destination
    return distance


def part1(data):
    shortest_distance = 1000000
    places.clear()

    path = get_paths(data)

    all_paths = list(itertools.permutations(path))
    for try_path in all_paths:
        try_path = list(try_path)
        distance = get_distance(try_path.copy())
        if distance < shortest_distance:
            shortest_distance = distance

    return shortest_distance


def part2(data):
    longest_distance = 0
    places.clear()

    path = get_paths(data)

    all_paths = list(itertools.permutations(path))
    for try_path in all_paths:
        try_path = list(try_path)
        distance = get_distance(try_path.copy())
        if distance > longest_distance:
            longest_distance = distance

    return longest_distance


if __name__ == "__main__":
    # Read input file or use test string
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        # Example test input, replace with actual test data
        input_data = """\
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""

    data = parse_input(input_data)
    print("Day 09 Part 1:", part1(data))
    print("Day 09 Part 2:", part2(data))
