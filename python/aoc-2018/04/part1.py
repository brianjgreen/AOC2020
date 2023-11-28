#
# Advent of Code 2018 - Day 4 Part 1
# 23 Oct 2023 Brian Green
#
# Problem:
# Find the guard that has the most minutes asleep.
# What minute does that guard spend asleep the most?
#


def get_data():
    """Read the data file and return a list of stripped strings of each line"""
    filename = "data.dat"
    with open(filename) as data_file:
        data_set = [num.strip() for num in data_file.readlines()]

    return data_set


def get_ledger(guard_log):
    guard = 0
    sleep_start = 0
    ledger = {}

    for entry in guard_log:
        if "Guard" in entry:
            guard = entry.split("#")[1].replace(" begins shift", "")
            if guard not in ledger.keys():
                ledger[guard] = {}
        elif "falls asleep" in entry:
            sleep_start = int(entry[15:17])
        elif "wakes up" in entry:
            for minute in range(sleep_start, int(entry[15:17])):
                if minute in ledger[guard]:
                    ledger[guard][minute] += 1
                else:
                    ledger[guard][minute] = 1
        else:
            print("WHAT!?")

    return ledger


def get_sleepy_guard(ledger):
    most_sleep = 0
    guard_name = None
    for guard in ledger:
        sleep_time = sum(ledger[guard].values())
        if sleep_time > most_sleep:
            most_sleep = sleep_time
            guard_name = guard

    print(f"Guard #{guard_name} number of minutes asleep: {most_sleep}")
    return guard_name


def get_most_sleep_minute(ledger, guard_name):
    sleep_minute = 0
    max_minutes = 0
    for num_day, minutes in ledger[guard_name].items():
        if minutes > max_minutes:
            max_minutes = minutes
            sleep_minute = num_day

    return sleep_minute


if __name__ == "__main__":
    ledger = get_ledger(sorted(get_data()))
    guard_name = get_sleepy_guard(ledger)
    sleepy_minute = get_most_sleep_minute(ledger, guard_name)
    print(f"Minute most often sleeping: {sleepy_minute}")
    print(sleepy_minute * int(guard_name))
