#
# Advent of Code 2020 - Day 10 Part 1
# 10 Dec 2020 Brian Green
#
# Problem:
#
#
import os


class Aoc10:
    def __init__(self):
        self.test_data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        self.test_data_2 = [
            28,
            33,
            18,
            42,
            31,
            14,
            46,
            20,
            48,
            47,
            24,
            23,
            49,
            45,
            19,
            38,
            39,
            11,
            1,
            32,
            25,
            35,
            8,
            17,
            7,
            9,
            4,
            2,
            34,
            10,
            3,
        ]
        file_name = "data" + os.sep + "brian_aoc10.dat"
        with open(file_name) as data_file:
            data_set = [int(x) for x in data_file.readlines()]

        # self.data = self.test_data
        # self.data = self.test_data_2
        self.data = data_set

    """
    def validate_adaptors(self, adaptors):
        valid_gaps = (1, 2, 3)
        adaptors.append(0)
        adaptors.sort()
        # print(adaptors)
        for i in range(1, len(adaptors)):
            gap = adaptors[i] - adaptors[i-1]
            # print(gap)
            if gap not in valid_gaps:
                return False
        return True
    """

    def run_it(self):
        self.data.append(0)
        self.data.sort()
        self.data.append(self.data[-1] + 3)
        position = len(self.data) - 1
        print(position)
        tabulate = [0 for _ in range(len(self.data))]
        tabulate[-1] = 1
        print(tabulate)

        while position >= 0:
            for i in range(1, 4):
                if position + i >= len(self.data):
                    # print("BREAK")
                    break

                if (
                    self.data[position] + 1 == self.data[position + i]
                    or self.data[position] + 2 == self.data[position + i]
                    or self.data[position] + 3 == self.data[position + i]
                ):
                    tabulate[position] += tabulate[position + i]
                # print(f"i:{i} pos:{position} {tabulate}")

            position -= 1
        print(tabulate)
        print(tabulate[0])

        """
        valid_configs = 0
        optional = []
        self.data.sort()
        # print(self.data)
        for i in range(len(self.data) - 1):
            # print(f"{self.data[i]} {self.data[i-1]}")
            adaptors = self.data.copy()
            not_used = adaptors[i]
            # print(f"not used = {not_used}")
            adaptors.remove(not_used)
            if self.validate_adaptors(adaptors):
                optional.append(not_used)

        print(optional)

        bit_field = pow(2, len(optional)) - 1
        print(bit_field)

        for i in range(bit_field + 1):
            not_used = []
            adaptors = self.data.copy()

            bit = 0
            field = i
            while field != 0:
                # print(f"i {i} bit {bit}  field {field} {field & 1}")
                if field & 1:
                    not_used.append(optional[bit])
                bit += 1
                field >>= 1

            # print(f"not_used{not_used}")
            for j in range(len(not_used)):
                adaptors.remove(not_used[j])
            # print(f"adaptors {adaptors}")
            if self.validate_adaptors(adaptors):
                valid_configs += 1

        print(valid_configs)
        """


if __name__ == "__main__":
    solve_it = Aoc10()
    solve_it.run_it()
