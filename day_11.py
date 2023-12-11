# Advent of Code 2023
# Day 11: Cosmic Expansion

from itertools import combinations

with open("inputs/day_11.txt") as file:
    image = [list(line[:-1]) for line in file.readlines()]

galaxies = []

for y, row in enumerate(image):
    for x, tile in enumerate(row):
        if tile == "#":
            galaxies.append([x, y])

moved_galaxies_part_1 = [galaxy.copy() for galaxy in galaxies]
moved_galaxies_part_2 = [galaxy.copy() for galaxy in galaxies]

for y, row in enumerate(image):
    if "#" not in row:
        for i, galaxy in enumerate(galaxies):
            if galaxy[1] > y:
                moved_galaxies_part_1[i][1] += 1
                moved_galaxies_part_2[i][1] += 999999

for x in range(len(image[0])):
    if not any(image[y][x] == "#" for y in range(len(image))):
        for i, galaxy in enumerate(galaxies):
            if galaxy[0] > x:
                moved_galaxies_part_1[i][0] += 1
                moved_galaxies_part_2[i][0] += 999999

distance_sum_part_1 = 0

for pair in combinations(moved_galaxies_part_1, 2):
    distance_sum_part_1 += (
        abs(pair[1][0] - pair[0][0]) + abs(pair[1][1] - pair[0][1])
    )

print(f"Part 1: {distance_sum_part_1}")

distance_sum_part_2 = 0

for pair in combinations(moved_galaxies_part_2, 2):
    distance_sum_part_2 += (
        abs(pair[1][0] - pair[0][0]) + abs(pair[1][1] - pair[0][1])
    )

print(f"Part 2: {distance_sum_part_2}")
