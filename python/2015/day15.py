# python day15.py ../../data/2015/day15.dat

import sys


def parse_input(input_data):
    stats = {}
    for ingredient in input_data.strip().split("\n"):
        pantry = ingredient.split()
        name = pantry[0][:-1]
        cap = int(pantry[2][:-1])
        dur = int(pantry[4][:-1])
        fla = int(pantry[6][:-1])
        tex = int(pantry[8][:-1])
        cal = int(pantry[10])
        stats[name] = {
            "capacity": cap,
            "durability": dur,
            "flavor": fla,
            "texture": tex,
            "calories": cal,
        }
    return stats


def part1(stats):
    highest_total = 0
    for sugar in range(101):
        for sprinkles in range(101 - sugar):
            for candy in range(101 - sugar - sprinkles):
                chocolate = 100 - sugar - sprinkles - candy
                cap = max(
                    0,
                    sugar * stats["Sugar"]["capacity"]
                    + sprinkles * stats["Sprinkles"]["capacity"]
                    + candy * stats["Candy"]["capacity"]
                    + chocolate * stats["Chocolate"]["capacity"],
                )
                dur = max(
                    0,
                    sugar * stats["Sugar"]["durability"]
                    + sprinkles * stats["Sprinkles"]["durability"]
                    + candy * stats["Candy"]["durability"]
                    + chocolate * stats["Chocolate"]["durability"],
                )
                fla = max(
                    0,
                    sugar * stats["Sugar"]["flavor"]
                    + sprinkles * stats["Sprinkles"]["flavor"]
                    + candy * stats["Candy"]["flavor"]
                    + chocolate * stats["Chocolate"]["flavor"],
                )
                tex = max(
                    0,
                    sugar * stats["Sugar"]["texture"]
                    + sprinkles * stats["Sprinkles"]["texture"]
                    + candy * stats["Candy"]["texture"]
                    + chocolate * stats["Chocolate"]["texture"],
                )
                total = cap * dur * fla * tex
                highest_total = max(highest_total, total)
    return highest_total


def part2(stats):
    highest_total = 0
    for sugar in range(101):
        for sprinkles in range(101 - sugar):
            for candy in range(101 - sugar - sprinkles):
                chocolate = 100 - sugar - sprinkles - candy
                cal = (
                    sugar * stats["Sugar"]["calories"]
                    + sprinkles * stats["Sprinkles"]["calories"]
                    + candy * stats["Candy"]["calories"]
                    + chocolate * stats["Chocolate"]["calories"]
                )
                if cal != 500:
                    continue
                cap = max(
                    0,
                    sugar * stats["Sugar"]["capacity"]
                    + sprinkles * stats["Sprinkles"]["capacity"]
                    + candy * stats["Candy"]["capacity"]
                    + chocolate * stats["Chocolate"]["capacity"],
                )
                dur = max(
                    0,
                    sugar * stats["Sugar"]["durability"]
                    + sprinkles * stats["Sprinkles"]["durability"]
                    + candy * stats["Candy"]["durability"]
                    + chocolate * stats["Chocolate"]["durability"],
                )
                fla = max(
                    0,
                    sugar * stats["Sugar"]["flavor"]
                    + sprinkles * stats["Sprinkles"]["flavor"]
                    + candy * stats["Candy"]["flavor"]
                    + chocolate * stats["Chocolate"]["flavor"],
                )
                tex = max(
                    0,
                    sugar * stats["Sugar"]["texture"]
                    + sprinkles * stats["Sprinkles"]["texture"]
                    + candy * stats["Candy"]["texture"]
                    + chocolate * stats["Chocolate"]["texture"],
                )
                total = cap * dur * fla * tex
                highest_total = max(highest_total, total)
    return highest_total

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        input_data = """Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8
"""
    stats = parse_input(input_data)
    print("Day 15 Part 1:", part1(stats))
    print("Day 15 Part 2:", part2(stats))
