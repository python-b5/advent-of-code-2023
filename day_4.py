# Advent of Code 2023
# Day 4: Scratchcards

point_sum = 0
copy_amounts = {}

with open("inputs/day_4.txt") as file:
    for i, line in enumerate(file):
        halves = line.split(": ")[1].split("|")
        winning_nums = [int(num) for num in halves[0].split()]

        points = 0
        winning_amount = 0

        for num in [int(num) for num in halves[1].split()]:
            if num in winning_nums:
                if points == 0:
                    points = 1
                else:
                    points *= 2

                winning_amount += 1

        point_sum += points
        copy_amounts[i] = winning_amount

print(f"Part 1: {point_sum}")

amounts = {card: 1 for card in copy_amounts}

for card in amounts:
    for i in range(copy_amounts[card]):
        amounts[card + i + 1] += amounts[card]

print(f"Part 2: {sum(amounts.values())}")
