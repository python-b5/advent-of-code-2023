# Advent of Code 2023
# Day 6: Wait For It

from functools import reduce
from operator import mul

with open("inputs/day_6.txt") as file:
    line_1 = next(file)
    line_2 = next(file)

    races_part_1 = list(zip(
        (int(n) for n in line_1.split()[1:]),
        (int(n) for n in line_2.split()[1:])
    ))

    race_part_2 = (
        int("".join(line_1.split()[1:])),
        int("".join(line_2.split()[1:]))
    )

def find_ways(race):
    ways = 0

    for hold_duration in range(1, race[0]):
        distance = (race[0] - hold_duration) * hold_duration

        if distance > race[1]:
            ways += 1

    return ways

print(f"Part 1: {reduce(mul, (find_ways(race) for race in races_part_1))}")
print(f"Part 2: {find_ways(race_part_2)}")
