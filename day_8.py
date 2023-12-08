# Advent of Code 2023
# Day 8: Haunted Wasteland

import math

graph = {}

with open("inputs/day_8.txt") as file:
    for i, line in enumerate(file):
        if i == 0:
            instructions = line.rstrip("\n")
        elif i > 1:
            graph[line[:3]] = (line[7:10], line[12:15])

def next_location(graph, location):
    return graph[location]["LR".index(instructions[steps % len(instructions)])]

steps = 0
location = "AAA"

while location != "ZZZ":
    location = next_location(graph, location)
    steps += 1

print(f"Part 1: {steps}")

locations = [location for location in graph if location[-1] == "A"]
steps_per_location = []

for i in range(len(locations)):
    steps = 0
    z_count = 0

    while z_count < 2:
        locations[i] = next_location(graph, locations[i])
        steps += 1

        if locations[i][-1] == "Z":
            if z_count == 0:
                steps = 0

            z_count += 1

    steps_per_location.append(steps)

print(f"Part 2: {math.lcm(*steps_per_location)}")
