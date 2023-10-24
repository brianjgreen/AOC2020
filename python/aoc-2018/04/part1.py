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
    if 'Guard' in entry:
        guard = entry.split('#')[1].replace(' begins shift', '')
        if guard not in ledger.keys():
            ledger[guard] = {}
    elif 'falls asleep' in entry:
        sleep_start = int(entry[15:17])
    elif 'wakes up' in entry:
        for minute in range(sleep_start, int(entry[15:17])):
            if minute in ledger[guard]:
                ledger[guard][minute] += 1
            else:
                ledger[guard][minute] = 1
    else:
        print('WHAT!?')

most_sleep = 0
guard_name = None
for guard in ledger:
    sleep_time = sum(ledger[guard].values()) 
    if sleep_time > most_sleep:
        most_sleep = sleep_time
        guard_name = guard

print(f'Guard #{guard_name} number of minutes asleep: {most_sleep}')
sleep_minute = 0
max_minutes = 0
for num_day, minutes in ledger[guard_name].items():
    if minutes > max_minutes:
        max_minutes = minutes
        sleep_minute = num_day

print(f'Minute most often sleeping: {sleep_minute}')
print(sleep_minute * int(guard_name))
