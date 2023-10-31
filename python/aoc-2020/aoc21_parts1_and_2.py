#
# Advent of Code 2020 - Day 21 Parts 1 and 2
# 21 Dec 2020 Brian Green
#
# Problem:
# 1.) Determine which ingredients cannot possibly contain any of the allergens in your list.
# How many times do any of those ingredients appear?
#
# 2.) Time to stock your raft with supplies. What is your canonical dangerous ingredient list?
#
import os


class Aoc21:
    def __init__(self):
        file_name = "data" + os.sep + "brian_aoc21.dat"
        with open(file_name) as data_file:
            data_set = [x.strip() for x in data_file.readlines()]

        # self.data = test_data.split('\n')
        self.data = data_set

    def run_it(self):
        print(self.data)
        bad = {}
        all_foreign = []
        for food in self.data:
            i = []
            allergen = False
            for ingredient in food.split():
                if ingredient == "(contains":
                    allergen = True
                elif allergen:
                    if ingredient[-1] == ")" or ingredient[-1] == ",":
                        ingredient = ingredient[:-1]
                    if ingredient in bad:
                        bad[ingredient].append(i)
                    else:
                        bad[ingredient] = [
                            i,
                        ]
                else:
                    i.append(ingredient)
                    all_foreign.append(ingredient)
        print(bad)

        trans = {}
        for bk, bv in bad.items():
            result = set(bv[0])
            for s in bv[1:]:
                result.intersection_update(s)
            print(f"{bk} {result}")
            trans[bk] = list(result)
        print(trans)

        lang = {}
        for tk, tv in trans.items():
            if len(tv) == 1:
                lang[tk] = tv[0]
        print(lang)
        for elem in lang:
            print(elem)
            trans.pop(elem)
        print(trans)

        while len(trans) > 0:
            for tk, tv in trans.items():
                for lk, lv in lang.items():
                    if lv in tv:
                        trans[tk].remove(lv)
            print(trans)
            for tk, tv in trans.items():
                if len(tv) == 1:
                    lang[tk] = tv[0]
            print(lang)
            for elem in lang:
                print(elem)
                if elem in trans:
                    trans.pop(elem)
            print(trans)
            print(len(trans))
        print(lang)

        for v in lang.values():
            all_foreign[:] = [x for x in all_foreign if x != v]
        print(all_foreign)
        print(len(all_foreign))

        # Part 2 adds this code
        print(lang)
        print(lang.keys())
        print(sorted(lang.keys()))
        for i in sorted(lang.keys()):
            print(lang[i], end="")
            print(",", end="")  # omit the final comma before submitting answer


if __name__ == "__main__":
    solve_it = Aoc21()
    solve_it.run_it()
