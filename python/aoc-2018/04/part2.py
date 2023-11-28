#
# Advent of Code 2018 - Day 4 Part 1
# 23 Oct 2023 Brian Green
#
# Problem:
# Find the guard that has the most minutes asleep.
# What minute does that guard spend asleep the most?
#

from part1 import get_data, get_ledger


def get_sleepy_guard_minute(ledger):
    sleepy_guard = 0
    sleepy_minute = 0
    max_days = 0

    for guard in ledger:
        for minute, days in ledger[guard].items():
            if days > max_days:
                sleepy_minute = minute
                sleepy_guard = guard
                max_days = days

    return sleepy_guard, sleepy_minute


if __name__ == "__main__":
    ledger = get_ledger(sorted(get_data()))
    sleepy_guard, sleepy_minute = get_sleepy_guard_minute(ledger)

    print(
        f"Guard #{sleepy_guard} Minute:{sleepy_minute} {int(sleepy_guard) * sleepy_minute}"
    )
