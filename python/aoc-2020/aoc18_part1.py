#
# Advent of Code 2020 - Day 18 Part 1
# 18 Dec 2020 Brian Green
#
# Problem:
# Before you can help with the homework, you need to understand it yourself.
# Evaluate the expression on each line of the homework; what is the sum of the resulting values?
import os


class Aoc18:
    def __init__(self):
        file_name = "data" + os.sep + "brian_aoc18.dat"
        with open(file_name) as data_file:
            data_set = [x.strip() for x in data_file.readlines()]

        self.data = data_set

    # https://stackoverflow.com/questions/4284991/parsing-nested-parentheses-in-python-grab-content-by-level
    def parenthetic_contents(self, string):
        # Generate parenthesized contents in string as pairs (level, contents).
        stack = []
        for i, c in enumerate(string):
            if c == "(":
                stack.append(i)
            elif c == ")" and stack:
                start = stack.pop()
                yield (len(stack), string[start + 1 : i])

    def calc(self, formula):
        total = 0
        oper = "+"
        for i in formula.split():
            if i == "+":
                oper = i
            elif i == "-":
                oper = i
            elif i == "*":
                oper = i
            elif i == "/":
                oper = i
            else:
                num = int(i)
                if oper == "+":
                    total += num
                elif oper == "-":
                    total -= num
                elif oper == "*":
                    total *= num
                elif oper == "/":
                    total /= num
        return total

    def calc_formula(self, formula):
        print(formula)
        parens = list(self.parenthetic_contents(formula))
        print(parens)
        sub = {}
        for n, f in parens:
            for k in sub:
                if k in f:
                    f = f.replace(k, sub[k])
            temp = self.calc(f)
            reduce = "(" + f + ")"
            sub[reduce] = str(temp)
            formula = formula.replace(reduce, sub[reduce])
        total = 0
        total = self.calc(formula)
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
