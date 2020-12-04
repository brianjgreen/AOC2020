#
# Advent of Code 2020 - Day 4 Part 1
# 4 Dec 2020 Brian Green
#
# Problem:
# Count the number of valid passports - those that have all required fields.
# Treat cid as optional. In your batch file, how many passports are valid?
#
import os


class Aoc04:
    def __init__(self):
        self.req_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
        self.opt_field = ('cid',)
        """
        test_data = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n', 'byr:1937 iyr:2017 cid:147 hgt:183cm\n', '\n',
                     'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\n', 'hcl:#cfa07d byr:1929\n', '\n',
                     'hcl:#ae17e1 iyr:2013\n', 'eyr:2024\n', 'ecl:brn pid:760753108 byr:1931\n', 'hgt:179cm\n', '\n',
                     'hcl:#cfa07d eyr:2025 pid:166559648\n', 'iyr:2011 ecl:brn hgt:59in\n', '\n']
        """
        file_name = "data" + os.sep + "brian_aoc04.dat"
        with open(file_name) as data_file:
            data_set = data_file.readlines()

        # self.data = test_data
        self.data = data_set

    def run_it(self):
        # print(self.data)
        records = []
        passport = {}
        for i in self.data:
            if len(i) == 1:
                # Finished with the previous record, save it on the list and start a new record.
                # print(passport)
                records.append(passport)
                passport = {}
                # print(records)
            else:
                # Parse the string to create a dictionary (key/value pair)
                new_fields = dict(field.split(':') for field in i.split(' '))
                # Add the new key/value pairs to the dictionary
                passport.update(new_fields)
                # print(passport)

        total_valid = 0
        for i in records:
            valid = 1
            # print(i)
            for j in self.req_fields:
                # print(j)
                # Check to see if required key is present in record
                if j not in i:
                    # print('INVALID')
                    valid = 0
                    break
            total_valid += valid

        print(f"Total Valid: {total_valid}")


if __name__ == "__main__":
    solve_it = Aoc04()
    solve_it.run_it()
