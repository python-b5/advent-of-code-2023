# Advent of Code 2023
# Day 1: Trebuchet?!

spelled_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10
}

result_part_1 = 0
result_part_2 = 0

with open("inputs/day_1.txt") as file:
    for line in file:
        digits_part_1 = []
        digits_part_2 = []

        for pos in range(len(line)):
            if line[pos].isdigit():
                digit = int(line[pos])
                digits_part_1.append(digit)
                digits_part_2.append(digit)

            for spelled in spelled_digits:
                if line[pos:].startswith(spelled):
                    digits_part_2.append(spelled_digits[spelled])

        result_part_1 += digits_part_1[0] * 10 + digits_part_1[-1]
        result_part_2 += digits_part_2[0] * 10 + digits_part_2[-1]

print(f"Part 1: {result_part_1}")
print(f"Part 2: {result_part_2}")
