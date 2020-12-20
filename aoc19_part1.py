#
# Advent of Code 2020 - Day 19 Part 1
# 19 Dec 2020 Brian Green
#
# Problem:
#
#
import os
import re


class Aoc19:
    def __init__(self):
        test_rules = ['0: 4 1 5',
                      '1: 2 3 | 3 2',
                      '2: 4 4 | 5 5',
                      '3: 4 5 | 5 4',
                      '4: "a"',
                      '5: "b"']

        test_message = ['ababbb',
                        'bababa',
                        'abbbab',
                        'aaabbb',
                        'aaaabbb']

        file_name = "data" + os.sep + "brian_aoc19_rules.dat"
        with open(file_name) as data_file:
            data_set_rules = [x.strip() for x in data_file.readlines()]
        file_name = "data" + os.sep + "brian_aoc19_messages.dat"
        with open(file_name) as data_file:
            data_set_messages = [x.strip() for x in data_file.readlines()]

        self.data_rules = test_rules
        self.data_messages = test_message
        # self.data_rules = data_set_rules
        # self.data_messages = data_set_messages

        self.rules = {}
        for rule in self.data_rules:
            num, pattern = rule.split(':')
            self.rules[int(num)] = pattern.strip()

    def sub_letters(self, letters):
        for k, v in self.rules.items():
            for k1, v1 in letters.items():
                b_list = v.split(' ')
                v = self.rules[k] = ' '.join(
                    [item.replace(str(k1), v1) for item in b_list])
                print(b_list)
                print(self.rules[k])
        print(len(self.rules))
        print(self.rules)
        print(letters)

        letters = {}
        for k, v in self.rules.items():
            if not any(str.isdigit(c) for c in v) and k != 0:
                letters[k] = f"({v})"

        for k in letters:
            self.rules.pop(k)

        return letters

    def run_it(self):
        print(self.rules)
        print(self.data_messages)

        letters = {}
        for k, v in self.rules.items():
            if '"' in v:
                # print(k)
                letters[k] = v.strip('"')

        for k in letters:
            self.rules.pop(k)

        while any(str.isdigit(c) for c in self.rules[0]):
            # print(letters)
            letters = self.sub_letters(letters)
            # print(self.rules)

        print(self.rules)
        pattern = '^' + self.rules[0].replace(' ', '') + '$'
        print(pattern)
        p = re.compile(pattern)
        total = 0
        for i in self.data_messages:
            if re.match(p, i):
                print(i)
                total += 1
        print(total)


if __name__ == "__main__":
    solve_it = Aoc19()
    solve_it.run_it()
