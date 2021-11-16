#
# Advent of Code 2020 - Day 7 Part 1
# 7 Dec 2020 Brian Green
#
# Problem:
# How many bag colors can eventually contain at least one shiny gold bag?
#
import os


class Aoc07:
    def __init__(self):
        self.bag_rules = {}
        self.test_data = ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
                          "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
                          "bright white bags contain 1 shiny gold bag.",
                          "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
                          "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
                          "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
                          "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
                          "faded blue bags contain no other bags.",
                          "dotted black bags contain no other bags."]
        file_name = "data" + os.sep + "brian_aoc07.dat"
        with open(file_name) as data_file:
            data_set = data_file.readlines()

        # self.data = self.test_data
        self.data = data_set

    def get_num_shiny_gold_bags(self, bag):
        if bag == 'shiny gold':
            return 1
        elif self.bag_rules[bag] is not None:
            for i in self.bag_rules[bag]:
                if self.get_num_shiny_gold_bags(i[1]) == 1:
                    return 1
        return 0

    def run_it(self):
        for rule in self.data:
            parts = rule.split(',')
            parse = parts[0].split()
            bag_type = parse[0] + " " + parse[1]
            if bag_type in self.bag_rules:
                print(f"ERROR, bag rule {bag_type} exists!")
                break

            if parse[4] == 'no':
                self.bag_rules[bag_type] = None
            else:
                self.bag_rules[bag_type] = [(int(parse[4]), parse[5] + " " + parse[6]), ]

            if len(parts) > 1:
                for inner_bag in parts[1:]:
                    sub_parse = inner_bag.strip().split()
                    self.bag_rules[bag_type].append((int(sub_parse[0]), sub_parse[1] + " " + sub_parse[2]))

        count = 0
        for i in self.bag_rules:
            if i != 'shiny gold':
                count += self.get_num_shiny_gold_bags(i)
        print(count)


if __name__ == "__main__":
    solve_it = Aoc07()
    solve_it.run_it()
