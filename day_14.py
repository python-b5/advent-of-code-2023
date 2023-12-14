# Advent of Code 2023
# Day 14: Parabolic Reflector Dish

with open("inputs/day_14.txt") as file:
    platform = [list(line.rstrip("\n")) for line in file.readlines()]
    size = len(platform)

def total_load(platform):
    total_load = 0

    for y, row in enumerate(platform):
        for char in row:
            if char == "O":
                total_load += size - y

    return total_load

seen = {}
part_1_finished = False
iteration = 0

while iteration < 1000000000:
    for _ in range(4):
        for x in range(size):
            for y in range(1, size):
                if platform[y][x] == "O" and platform[y - 1][x] == ".":
                    for new_y in range(y - 1, -1, -1):
                        if platform[new_y][x] != ".":
                            new_y += 1
                            break

                    platform[y][x] = "."
                    platform[new_y][x] = "O"

        if not part_1_finished:
            print(f"Part 1: {total_load(platform)}")
            part_1_finished = True

        platform = [list(reversed(row)) for row in zip(*platform)]

    key = "".join("".join(row) for row in platform)

    if key in seen:
        cycle_length = iteration - seen[key]
        iteration += (1000000000 - iteration) // cycle_length * cycle_length
    else:
        seen[key] = iteration

    iteration += 1

print(f"Part 2: {total_load(platform)}")
