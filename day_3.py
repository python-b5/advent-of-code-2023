# Advent of Code 2023
# Day 3: Gear Ratios

with open("inputs/day_3.txt") as file:
    schematic = [line.rstrip("\n") for line in file]

used_positions = []
part_sum = 0
ratio_sum = 0

for y, line in enumerate(schematic):
    for x, char in enumerate(line):
        if char not in ".0123456789":
            adj_count = 0
            ratio = 1

            for pos in (
                (x + 1, y), (x + 1, y + 1), (x, y + 1), (x - 1, y + 1),
                (x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)
            ):
                if 0 <= pos[0] < len(line) and 0 <= pos[1] < len(schematic):
                    if (
                        schematic[pos[1]][pos[0]] in "0123456789"
                        and pos not in used_positions
                    ):
                        part = schematic[pos[1]][pos[0]]
                        used_positions.append(pos)

                        check_x = pos[0] - 1

                        while (
                            check_x >= 0
                            and schematic[pos[1]][check_x] in "0123456789"
                            and (check_x, pos[1]) not in used_positions
                        ):
                            part = schematic[pos[1]][check_x] + part
                            used_positions.append((check_x, pos[1]))
                            check_x -= 1

                        check_x = pos[0] + 1

                        while (
                            check_x < len(line)
                            and schematic[pos[1]][check_x] in "0123456789" 
                            and (check_x, pos[1]) not in used_positions
                        ):
                            part = part + schematic[pos[1]][check_x]
                            used_positions.append((check_x, pos[1]))
                            check_x += 1

                        part_sum += int(part)

                        if char == "*" and adj_count < 2:
                            adj_count += 1
                            ratio *= int(part)

            if adj_count == 2:
                ratio_sum += ratio

print(f"Part 1: {part_sum}")
print(f"Part 2: {ratio_sum}")
