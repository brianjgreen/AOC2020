#
# Advent of Code 2020 - Day 16 Part 1
# 16 Dec 2020 Brian Green
#
# Problem:
# Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?
#
import os
import re


class Aoc16:
    def __init__(self):
        file_name = "data" + os.sep + "brian_aoc16_tickets.dat"
        with open(file_name) as data_file:
            tickets = [x.strip().split(",") for x in data_file.readlines()]
        data_set_tickets = []
        for i in tickets:
            data_set_tickets.append(tuple(int(x) for x in i))
        file_name = "data" + os.sep + "brian_aoc16_rules.dat"
        with open(file_name) as data_file:
            data_set_rules = [x.strip() for x in data_file.readlines()]

        # self.data_rules = test_rules
        # self.data_tickets = test_tickets
        self.data_rules = data_set_rules
        self.data_tickets = data_set_tickets

    def run_it(self):
        rules = {}
        print(self.data_rules)
        p = re.compile(r"([a-z\s]+): (\d+)-(\d+) or (\d+)-(\d+)")
        for r in self.data_rules:
            m = re.match(p, r)
            field, lo_x, hi_x, lo_y, hi_y = m.groups()
            rules[field] = (int(lo_x), int(hi_x), int(lo_y), int(hi_y))
        print(rules)

        print(self.data_tickets)
        bad = []
        for t in self.data_tickets:
            for num in t:
                invalid = True
                for lo_x, hi_x, lo_y, hi_y in rules.values():
                    if lo_x <= num <= hi_x or lo_y <= num <= hi_y:
                        invalid = False
                if invalid:
                    print(f"{num} invalid!")
                    bad.append(num)
        print(bad)
        print(sum(bad))


if __name__ == "__main__":
    solve_it = Aoc16()
    solve_it.run_it()
