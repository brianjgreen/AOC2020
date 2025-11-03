# python day21.py ../../data/2015/day21.dat

import itertools
import sys


def parse_input(input_data):
    stats = {}
    for line in input_data.strip().split("\n"):
        key, value = line.split(": ")
        stats[key] = int(value)
    return stats["Hit Points"], stats["Damage"], stats["Armor"]


def player_wins(boss_hp, boss_def, boss_att, player_def, player_att):
    player_hp = 100
    while player_hp > 0 and boss_hp > 0:
        boss_hp -= max(1, player_att - boss_def)
        if boss_hp > 0:
            player_hp -= max(1, boss_att - player_def)
    return player_hp > 0


def part1(boss_hp, boss_damage, boss_armor):
    weapons = [
        {"cost": 8, "damage": 4, "armor": 0},
        {"cost": 10, "damage": 5, "armor": 0},
        {"cost": 25, "damage": 6, "armor": 0},
        {"cost": 40, "damage": 7, "armor": 0},
        {"cost": 74, "damage": 8, "armor": 0},
    ]
    armor = [
        {"cost": 0, "damage": 0, "armor": 0},
        {"cost": 13, "damage": 0, "armor": 1},
        {"cost": 31, "damage": 0, "armor": 2},
        {"cost": 53, "damage": 0, "armor": 3},
        {"cost": 75, "damage": 0, "armor": 4},
        {"cost": 102, "damage": 0, "armor": 5},
    ]
    rings = [
        {"cost": 0, "damage": 0, "armor": 0},
        {"cost": 25, "damage": 1, "armor": 0},
        {"cost": 50, "damage": 2, "armor": 0},
        {"cost": 100, "damage": 3, "armor": 0},
        {"cost": 20, "damage": 0, "armor": 1},
        {"cost": 40, "damage": 0, "armor": 2},
        {"cost": 80, "damage": 0, "armor": 3},
    ]

    min_cost = float('inf')
    for w in weapons:
        for a in armor:
            for r1, r2 in itertools.combinations(rings, 2):
                if r1["cost"] == 0 and r2["cost"] == 0:
                    continue
                if r1["cost"] == r2["cost"]:
                    continue
                player_att = w["damage"] + r1["damage"] + r2["damage"]
                player_def = a["armor"] + r1["armor"] + r2["armor"]
                cost = w["cost"] + a["cost"] + r1["cost"] + r2["cost"]
                if player_wins(boss_hp, boss_armor, boss_damage, player_def, player_att) and cost < min_cost:
                    min_cost = cost
    return min_cost


def part2(boss_hp, boss_damage, boss_armor):
    weapons = [
        {"cost": 8, "damage": 4, "armor": 0},
        {"cost": 10, "damage": 5, "armor": 0},
        {"cost": 25, "damage": 6, "armor": 0},
        {"cost": 40, "damage": 7, "armor": 0},
        {"cost": 74, "damage": 8, "armor": 0},
    ]
    armor = [
        {"cost": 0, "damage": 0, "armor": 0},
        {"cost": 13, "damage": 0, "armor": 1},
        {"cost": 31, "damage": 0, "armor": 2},
        {"cost": 53, "damage": 0, "armor": 3},
        {"cost": 75, "damage": 0, "armor": 4},
        {"cost": 102, "damage": 0, "armor": 5},
    ]
    rings = [
        {"cost": 0, "damage": 0, "armor": 0},
        {"cost": 25, "damage": 1, "armor": 0},
        {"cost": 50, "damage": 2, "armor": 0},
        {"cost": 100, "damage": 3, "armor": 0},
        {"cost": 20, "damage": 0, "armor": 1},
        {"cost": 40, "damage": 0, "armor": 2},
        {"cost": 80, "damage": 0, "armor": 3},
    ]

    max_cost = 0
    for w in weapons:
        for a in armor:
            for r1, r2 in itertools.combinations(rings, 2):
                if r1["cost"] == 0 and r2["cost"] == 0:
                    continue
                if r1["cost"] == r2["cost"]:
                    continue
                player_att = w["damage"] + r1["damage"] + r2["damage"]
                player_def = a["armor"] + r1["armor"] + r2["armor"]
                cost = w["cost"] + a["cost"] + r1["cost"] + r2["cost"]
                if not player_wins(boss_hp, boss_armor, boss_damage, player_def, player_att) and cost > max_cost:
                    max_cost = cost
    return max_cost


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        input_data = ""
    boss_hp, boss_damage, boss_armor = parse_input(input_data)
    print("Day 21 Part 1:", part1(boss_hp, boss_damage, boss_armor))
    print("Day 21 Part 2:", part2(boss_hp, boss_damage, boss_armor))
