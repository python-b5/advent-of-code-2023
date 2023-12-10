# Advent of Code 2023
# Day 10: Pipe Maze

with open("inputs/day_10.txt") as file:
    sketch = [list(line[:-1]) for line in file.readlines()]

for y, row in enumerate(sketch):
    for x, tile in enumerate(row):
        if tile == "S":
            start_x = x
            start_y = y

width = len(sketch[0])
height = len(sketch)

current_x = start_x
current_y = start_y

if current_x < len(sketch[0]) and sketch[current_y][current_x + 1] in "-J7":
    current_x += 1
    current_dir = "right"
elif current_y < height and sketch[current_y + 1][current_x] in "|LJ":
    current_y += 1
    current_dir = "down"
elif current_x > 0 and sketch[current_y][current_x - 1] in "-LF":
    current_x -= 1
    current_dir = "left"
else:
    current_y -= 1
    current_dir = "up"

start_dir = current_dir
loop = [(current_x, current_y)]

while current_x != start_x or current_y != start_y:
    tile = sketch[current_y][current_x]

    if tile == "|":
        if current_dir == "down":
            current_y += 1
        elif current_dir == "up":
            current_y -= 1
    elif tile == "-":
        if current_dir == "right":
            current_x += 1
        elif current_dir == "left":
            current_x -= 1
    elif tile == "L":
        if current_dir == "down":
            current_x += 1
            current_dir = "right"
        elif current_dir == "left":
            current_y -= 1
            current_dir = "up"
    elif tile == "J":
        if current_dir == "right":
            current_y -= 1
            current_dir = "up"
        elif current_dir == "down":
            current_x -= 1
            current_dir = "left"
    elif tile == "7":
        if current_dir == "right":
            current_y += 1
            current_dir = "down"
        elif current_dir == "up":
            current_x -= 1
            current_dir = "left"
    elif tile == "F":
        if current_dir == "left":
            current_y += 1
            current_dir = "down"
        elif current_dir == "up":
            current_x += 1
            current_dir = "right"

    loop.append((current_x, current_y))

print(f"Part 1: {len(loop) // 2}")

if current_dir == "right":
    if start_dir == "right":
        sketch[start_y][start_x] = "-"
    elif start_dir == "down":
        sketch[start_y][start_x] = "7"
    elif start_dir == "up":
        sketch[start_y][start_x] = "J"
elif current_dir == "down":
    if start_dir == "right":
        sketch[start_y][start_x] = "L"
    elif start_dir == "down":
        sketch[start_y][start_x] = "|"
    elif start_dir == "left":
        sketch[start_y][start_x] = "J"
elif current_dir == "left":
    if start_dir == "down":
        sketch[start_y][start_x] = "F"
    elif start_dir == "left":
        sketch[start_y][start_x] = "-"
    elif start_dir == "up":
        sketch[start_y][start_x] = "L"
elif start_dir == "right":
    sketch[start_y][start_x] = "F"
elif start_dir == "left":
    sketch[start_y][start_x] = "7"
else:
    sketch[start_y][start_x] = "|"

detailed = [[False for _ in range(width * 3)] for _ in range(height * 3)]

for y, row in enumerate(sketch):
    for x, tile in enumerate(row):
        if (x, y) in loop:
            if tile == "|":
                detailed[y * 3][x * 3:x * 3 + 3] = False, True, False
                detailed[y * 3 + 1][x * 3:x * 3 + 3] = False, True, False
                detailed[y * 3 + 2][x * 3:x * 3 + 3] = False, True, False
            elif tile == "-":
                detailed[y * 3][x * 3:x * 3 + 3] = False, False, False
                detailed[y * 3 + 1][x * 3:x * 3 + 3] = True, True, True
                detailed[y * 3 + 2][x * 3:x * 3 + 3] = False, False, False
            elif tile == "L":
                detailed[y * 3][x * 3:x * 3 + 3] = False, True, False
                detailed[y * 3 + 1][x * 3:x * 3 + 3] = False, True, True
                detailed[y * 3 + 2][x * 3:x * 3 + 3] = False, False, False
            elif tile == "J":
                detailed[y * 3][x * 3:x * 3 + 3] = False, True, False
                detailed[y * 3 + 1][x * 3:x * 3 + 3] = True, True, False
                detailed[y * 3 + 2][x * 3:x * 3 + 3] = False, False, False
            elif tile == "7":
                detailed[y * 3][x * 3:x * 3 + 3] = False, False, False
                detailed[y * 3 + 1][x * 3:x * 3 + 3] = True, True, False
                detailed[y * 3 + 2][x * 3:x * 3 + 3] = False, True, False
            elif tile == "F":
                detailed[y * 3][x * 3:x * 3 + 3] = False, False, False
                detailed[y * 3 + 1][x * 3:x * 3 + 3] = False, True, True
                detailed[y * 3 + 2][x * 3:x * 3 + 3] = False, True, False

queue = []

for y, row in enumerate(detailed):
    if y in (0, height * 3 - 1):
        search = range(width * 3)
    else:
        search = (0, width * 3 - 1)

    for x in search:
        if not row[x]:
            queue.append((x, y))

visited = set()

while queue:
    pos = queue.pop(0)

    for new_pos in (
        (pos[0] + 1, pos[1]),
        (pos[0], pos[1] + 1),
        (pos[0] - 1, pos[1]),
        (pos[0], pos[1] - 1)
    ):
        try:
            if not detailed[new_pos[1]][new_pos[0]] and new_pos not in visited:
                queue.append(new_pos)
                visited.add(new_pos)
        except IndexError:
            pass

inside = 0

for y in range(height):
    for x in range(width):
        if (
            (x * 3 + 1, y * 3 + 1) not in visited
            and not detailed[y * 3 + 1][x * 3 + 1]
        ):
            inside += 1

print(f"Part 2: {inside}")
