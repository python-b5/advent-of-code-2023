# Advent of Code 2023
# Day 13: Point of Incidence

def find_vertical_reflection(pattern, compare):
    for x in range(1, len(pattern[0])):
        left_side = [row[:x] for row in pattern]
        right_side = [list(reversed(row[x:])) for row in pattern]

        left_width = len(left_side[0])
        right_width = len(right_side[0])

        if left_width > right_width:
            difference = left_width - right_width
            left_side_adjusted = [row[difference:] for row in left_side]
            right_side_adjusted = right_side
        elif right_width > left_width:
            difference = right_width - left_width
            left_side_adjusted = left_side
            right_side_adjusted = [row[difference:] for row in right_side]
        else:
            left_side_adjusted = left_side
            right_side_adjusted = right_side

        if compare(left_side_adjusted, right_side_adjusted):
            return left_width

    return 0

def smudged_compare(left_side, right_side):
    left_side = [char for row in left_side for char in row]
    right_side = [char for row in right_side for char in row]

    return sum(
        left_side[i] != right_side[i] for i in range(len(left_side))
    ) == 1

notes_sum = 0
notes_sum_smudged = 0

with open("inputs/day_13.txt") as file:
    for pattern in file.read().split("\n\n"):
        pattern = [list(row.rstrip("\n")) for row in pattern.splitlines()]

        notes_sum += find_vertical_reflection(pattern, list.__eq__)
        notes_sum += find_vertical_reflection(
            [list(row) for row in list(zip(*pattern))[::-1]], list.__eq__
        ) * 100

        notes_sum_smudged += find_vertical_reflection(pattern, smudged_compare)
        notes_sum_smudged += find_vertical_reflection(
            [list(row) for row in list(zip(*pattern))[::-1]], smudged_compare
        ) * 100

print(f"Part 1: {notes_sum}")
print(f"Part 2: {notes_sum_smudged}")
