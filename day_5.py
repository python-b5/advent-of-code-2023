# Advent of Code 2023
# Day 5: If You Give A Seed A Fertilizer

mappings = []

with open("inputs/day_5.txt") as file:
    current = {}
    waiting_for_nums = True

    for i, line in enumerate(file):
        if i == 0:
            seeds = [int(n) for n in line.split(": ")[1].split()]
        else:
            if line[0] in "0123456789":
                nums = [int(n) for n in line.split()]
                current[range(nums[1], nums[1] + nums[2])] = nums[0] - nums[1]
                waiting_for_nums = False
            elif not waiting_for_nums:
                mappings.append(current)
                current = {}
                waiting_for_nums = True

    mappings.append(current)

def find_lowest_location(seeds, mappings):
    lowest_location = None

    for seed in seeds:
        current = seed

        for depth in mappings:
            for range_ in depth:
                if current in range_:
                    current += depth[range_]
                    break

        if lowest_location is None or current < lowest_location:
            lowest_location = current

    return lowest_location

print(f"Part 1: {find_lowest_location(seeds, mappings)}")

def seeds_part_2():
    for start, length in zip(seeds[0::2], seeds[1::2]):
        for seed in range(start, start + length):
            yield seed

print(f"Part 2: {find_lowest_location(seeds_part_2(), mappings)}")
