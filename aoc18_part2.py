#
# Advent of Code 2020 - Day 18 Part 2
# 18 Dec 2020 Brian Green
#
# Problem:
# ...addition is evaluated before multiplication.
# What do you get if you add up the results of evaluating the homework problems using these new rules?
import os


class Aoc18:
    def __init__(self):
        test_data = "1 + 2 * 3 + 4 * 5 + 6"  # 231
        test_data1 = "1 + (2 * 3) + (4 * (5 + 6))"  # 51
        test_data2 = "2 * 3 + (4 * 5)"  # 46
        test_data3 = "5 + (8 * 3 + 9 + 3 * 4 * 3)"  # 1445
        test_data4 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"  # 669060
        test_data5 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"  # 23340

        file_name = "data" + os.sep + "brian_aoc18.dat"
        with open(file_name) as data_file:
            data_set = [x.strip() for x in data_file.readlines()]

        # self.data = [test_data5, ]
        self.data = data_set

    # https://stackoverflow.com/questions/4284991/parsing-nested-parentheses-in-python-grab-content-by-level
    def parenthetic_contents(self, string):
        # Generate parenthesized contents in string as pairs (level, contents).
        stack = []
        for i, c in enumerate(string):
            if c == '(':
                stack.append(i)
            elif c == ')' and stack:
                start = stack.pop()
                yield (len(stack), string[start + 1: i])

    def calc(self, formula):
        total = 0
        oper = '+'
        for i in formula.split():
            if i == '+':
                oper = i
            elif i == '-':
                oper = i
            elif i == '*':
                oper = i
            elif i == '/':
                oper = i
            else:
                num = int(i)
                if oper == '+':
                    total += num
                elif oper == '-':
                    total -= num
                elif oper == '*':
                    total *= num
                elif oper == '/':
                    total /= num
        return total

    def new_math(self, formula):
        total = 1
        for i in formula.split('*'):
            total *= self.calc(i)
        return total

    def calc_formula(self, formula):
        print(formula)
        parens = list(self.parenthetic_contents(formula))
        sub = {}
        for n, f in parens:
            for k in sub:
                if k in f:
                    f = f.replace(k, sub[k])
            temp = self.new_math(f)
            reduce = '('+f+')'
            sub[reduce] = str(temp)
            formula = formula.replace(reduce, sub[reduce])
        total = 0
        total = self.new_math(formula)
        return total

    def run_it(self):
        totals = []
        formula = self.data
        for f in formula:
            totals.append(self.calc_formula(f))

        print(sum(totals))


if __name__ == "__main__":
    solve_it = Aoc18()
    solve_it.run_it()
