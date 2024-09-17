#
# AOC 2023 Day 1
# Brian Green
# Part 1 - What is the sum of all of the calibration values?
# Part 2 - What is the sum of all of the calibration values?
# Template: https://realpython.com/python-advent-of-code/#a-starting-template
#
import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.split()


def part1(data):
    """Solve part 1."""
    total_calc = 0
    for value in data:
        found_first = False
        first = 0
        last = 0
        for digit in value:
            if digit.isdigit():
                if not found_first:
                    first = int(digit)
                    found_first = True
                last = int(digit)
        total_calc += (first * 10) + last
    return total_calc


def part2(data):
    """Solve part 2."""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
