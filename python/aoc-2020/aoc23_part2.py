#
# Advent of Code 2020 - Day 23 Part 2
# 23 Dec 2020 Brian Green
#
# Problem:
# Determine which two cups will end up immediately clockwise of cup 1.
# What do you get if you multiply their labels together?
#


class Aoc23:
    def __init__(self):
        # test_data = [3, 8, 9, 1, 2, 5, 4, 6, 7]
        data_set = [5, 8, 6, 4, 3, 9, 1, 7, 2]

        # self.data = test_data
        self.data = data_set
        self.moves = 10000000

        pad = max(self.data) + 1
        while pad <= 1000000:
            self.data.append(pad)
            pad += 1

    def run_it(self):
        # print(self.data)
        cups = self.data

        for i in range(self.moves):
            if i % 1000 == 0:
                print(i)

            # The crab picks up the three cups that are immediately clockwise of the current cup.
            # They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
            current = cups[0]
            pick_up = []
            for _ in range(3):
                pick_up.append(cups.pop(1))

            # The crab selects a destination cup: the cup with a label equal to the current cup's label minus one.
            dest = current - 1
            while dest >= min(cups):
                if dest in cups:
                    break
                else:
                    # If this would select one of the cups that was just picked up, the crab will keep subtracting one until
                    # it finds a cup that wasn't just picked up.
                    dest -= 1

            # If at any point in this process the value goes below the lowest value on any cup's label,
            # it wraps around to the highest value on any cup's label instead.
            if dest < min(cups):
                dest = max(cups)

            dest_pos = cups.index(dest)

            # The crab places the cups it just picked up so that they are immediately clockwise of the destination cup.
            # They keep the same order as when they were picked up.
            cups = cups[: dest_pos + 1] + pick_up + cups[dest_pos + 1 :]

            # The crab selects a new current cup: the cup which is immediately clockwise of the current cup.
            cups.append(cups.pop(0))

        print(cups[0])
        print(cups[1])
        print(cups[0] * cups[1])


if __name__ == "__main__":
    solve_it = Aoc23()
    solve_it.run_it()
