#
# Advent of Code 2018 - Day 4 Part 1
# 23 Oct 2023 Brian Green
#
# Problem:
# Find the guard that has the most minutes asleep.
# What minute does that guard spend asleep the most?
#

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

guard_log = sorted(data_set)

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

sleepy_guard = 0
sleepy_minute = 0
max_days = 0

for guard in ledger:
    for minute, days in ledger[guard].items():
        if days > max_days:
            sleepy_minute = minute
            sleepy_guard = guard
            max_days = days

print(
    f"Guard #{sleepy_guard} Minute:{sleepy_minute} {int(sleepy_guard) * sleepy_minute}"
)
