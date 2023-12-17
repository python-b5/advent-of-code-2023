# Advent of Code 2023
# Day 16: The Floor Will Be Lava

with open("inputs/day_16.txt") as file:
    machine = [list(line.rstrip("\n")) for line in file]
    width = len(machine[0])
    height = len(machine)

def energized_tiles(x, y, direction):
    beams = [[x, y, direction]]
    seen_beams = set()
    energized = set()

    while beams:
        for beam in beams.copy():
            if (
                beam[0] < 0 or beam[0] >= width
                or beam[1] < 0 or beam[1] >= height
                or tuple(beam) in seen_beams
            ):
                beams.remove(beam)
                continue

            seen_beams.add(tuple(beam))
            energized.add((beam[0], beam[1]))

            tile = machine[beam[1]][beam[0]]

            if tile == "/":
                if beam[2] == "right":
                    beam[2] = "up"
                elif beam[2] == "down":
                    beam[2] = "left"
                elif beam[2] == "left":
                    beam[2] = "down"
                else:
                    beam[2] = "right"
            elif tile == "\\":
                if beam[2] == "right":
                    beam[2] = "down"
                elif beam[2] == "down":
                    beam[2] = "right"
                elif beam[2] == "left":
                    beam[2] = "up"
                else:
                    beam[2] = "left"
            elif tile == "|" and beam[2] in ("right", "left"):
                beam[2] = "down"
                beams.append([beam[0], beam[1] - 1, "up"])
            elif tile == "-" and beam[2] in ("down", "up"):
                beam[2] = "right"
                beams.append([beam[0] - 1, beam[1], "left"])

            if beam[2] == "right":
                beam[0] += 1
            elif beam[2] == "down":
                beam[1] += 1
            elif beam[2] == "left":
                beam[0] -= 1
            else:
                beam[1] -= 1

    return len(energized)

print(f"Part 1: {energized_tiles(0, 0, 'right')}")

starts = []

for x in range(width):
    starts.append([x, 0, "down"])
    starts.append([x, height - 1, "up"])

for y in range(height):
    starts.append([0, y, "right"])
    starts.append([width - 1, y, "left"])

print(f"Part 2: {max(energized_tiles(*start) for start in starts)}")
