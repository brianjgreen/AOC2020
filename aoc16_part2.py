#
# Advent of Code 2020 - Day 16 Part 2
# 16 Dec 2020 Brian Green
#
# Problem:
# Once you work out which field is which, look for the six fields on your ticket that start with the word departure.
# What do you get if you multiply those six values together?
#
import os
import re


class Aoc16:
    def __init__(self):
        test_rules = ["class: 1-3 or 5-7",
                      "row: 6-11 or 33-44",
                      "seat: 13-40 or 45-50"]
        test_tickets = [(7, 3, 47), (40, 4, 50), (55, 2, 20), (38, 6, 12)]

        self.my_ticket = [71, 127, 181, 179, 113, 109, 79, 151, 97,
                          107, 53, 193, 73, 83, 191, 101, 89, 149, 103, 197]

        file_name = "data" + os.sep + "brian_aoc16_tickets.dat"
        with open(file_name) as data_file:
            tickets = [x.strip().split(',') for x in data_file.readlines()]
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
        # build the field formatter rules
        rules = {}
        p = re.compile(r"([a-z\s]+): (\d+)-(\d+) or (\d+)-(\d+)")
        for r in self.data_rules:
            m = re.match(p, r)
            field, lo_x, hi_x, lo_y, hi_y = m.groups()
            rules[field] = (int(lo_x), int(hi_x), int(lo_y), int(hi_y))
        print(rules)

        # find and remove bad tickets
        bad_tickets = []
        for t in self.data_tickets:
            for num in t:
                invalid = True
                for lo_x, hi_x, lo_y, hi_y in rules.values():
                    if lo_x <= num <= hi_x or lo_y <= num <= hi_y:
                        invalid = False
                if invalid:
                    if t not in bad_tickets:
                        bad_tickets.append(t)
        print(f"Bad Tickets: {bad_tickets}")
        print(f"{len(self.data_tickets)}")
        for b in bad_tickets:
            self.data_tickets.remove(b)
        print(f"{len(self.data_tickets)}")

        # find all field names whose rules are valid for a field position
        possible_rule = {}
        for r in rules:
            possible_rule[r] = []
            lo_x, hi_x, lo_y, hi_y = rules[r]
            for i in range(len(self.data_tickets[0])):
                good = True
                for t in self.data_tickets:
                    if lo_x <= t[i] <= hi_x or lo_y <= t[i] <= hi_y:
                        pass
                    else:
                        good = False
                        break
                if good:
                    possible_rule[r].append(i)
        print(possible_rule)

        # map the field positions to the possible field names
        field_rule = {}
        for i in range(len(self.data_tickets[0])):
            field = []
            for r in possible_rule:
                if i in possible_rule[r]:
                    field.append(r)
            print(f"{i}: {field}")
            field_rule[i] = field

        # find field positions with only one possible field, save that field / position pair
        # remove that found field from all of the possible fields to uncover the next field position with only one possible field
        field_assign = {}
        for _ in range(len(rules)):
            for f in field_rule:
                if len(field_rule[f]) == 1:
                    field_assign[f] = field_rule[f][0]
            for a in field_assign:
                for f in field_rule:
                    if field_assign[a] in field_rule[f]:
                        field_rule[f].remove(field_assign[a])

        for s in sorted(field_assign):
            print(f"{s+1} {field_assign[s]}")

        # find the field positions for field names starting with 'departure'
        departures = []
        for f in field_assign:
            if 'departure' in field_assign[f]:
                print(f"{f} {field_assign[f]}")
                departures.append(f)
        print(departures)

        # multiply the values on my ticket in the fields that start with "departure"
        total = 1
        for d in departures:
            total *= self.my_ticket[d]
        print(total)


if __name__ == "__main__":
    solve_it = Aoc16()
    solve_it.run_it()
