# Advent of Code 2023
# Day 15: Lens Library

def hash_(s):
    current = 0

    for char in s:
        current += ord(char)
        current *= 17
        current %= 256

    return current

hash_sum = 0
boxes = [[] for _ in range(256)]

with open("inputs/day_15.txt") as file:
    for step in file.read().rstrip("\n").split(","):
        hash_sum += hash_(step)

        label = "".join(char for char in step if char.isalpha())
        label_len = len(label)

        box = boxes[hash_(label)]

        if step[label_len] == "=":
            existing = False

            for lens in box:
                if lens[0] == label:
                    lens[1] = int(step[label_len + 1])
                    existing = True
                    break

            if not existing:
                box.append([label, int(step[label_len + 1])])
        else:
            for lens in box:
                if lens[0] == label:
                    box.remove(lens)
                    break

print(f"Part 1: {hash_sum}")

focusing_power = 0

for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        old = focusing_power
        focusing_power += (i + 1) * (j + 1) * lens[1]

print(f"Part 2: {focusing_power}")
