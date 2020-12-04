#
# Advent of Code 2020 - Day 4 Part 2
# 4 Dec 2020 Brian Green
#
# Problem:
# Count the number of valid passports - those that have all required fields and valid values
# Continue to treat cid as optional. In your batch file, how many passports are valid?
#
import os
import re


# NOTE: These functions outside the class are static (can be called without creating an object from the class).
def check_year(year, min_year, max_year):
    year = year.strip()
    if re.match(r"\d{4}", year) and min_year <= int(year) <= max_year:
        return True
    return False


def check_birth_year(byr):
    return check_year(byr, 1920, 2002)


def check_issue_year(iyr):
    return check_year(iyr, 2010, 2020)


def check_expiration_year(eyr):
    return check_year(eyr, 2020, 2030)


def check_height(hgt):
    m = re.match(r"(\d+)(cm|in)", hgt)
    if m:
        measure, unit = m.groups()
        if (unit == 'cm' and 150 <= int(measure) <= 193) or (unit == 'in' and 59 <= int(measure) <= 76):
            return True
    return False


def check_hair_color(hcl):
    if re.match(r"#[0-9a-f]{6}", hcl):
        return True
    return False


def check_eye_color(ecl):
    # The rules say this field can only have ONE of the following.  Not sure how to do that in regex.
    if re.match(r"amb|blu|brn|gry|grn|hzl|oth", ecl):
        return True
    return False


def check_passport_id(pid):
    if re.match(r"^\d{9}$", pid):
        return True
    return False


class Aoc04:
    def __init__(self):
        self.req_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
        self.opt_field = ('cid',)
        file_name = "data" + os.sep + "brian_aoc04.dat"
        with open(file_name) as data_file:
            data_set = data_file.readlines()

        self.data = data_set

    def run_it(self):
        # print(self.data)
        records = []
        passport = {}
        for i in self.data:
            if len(i) == 1:
                # print(passport)
                # Finished with the previous record, save it on the list and start a new record.
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
            # Check to see if required key is present in record
            for j in self.req_fields:
                # print(j)
                if j not in i:
                    # print('INVALID')
                    valid = 0
                    break

            if valid == 1 and \
                    check_birth_year(i['byr']) and \
                    check_issue_year(i['iyr']) and \
                    check_expiration_year(i['eyr']) and \
                    check_height(i['hgt']) and \
                    check_hair_color(i['hcl']) and \
                    check_eye_color(i['ecl']) and \
                    check_passport_id(i['pid']):
                pass
            else:
                valid = 0
            total_valid += valid

        print(f"Total Valid: {total_valid}")


if __name__ == "__main__":
    solve_it = Aoc04()
    solve_it.run_it()
