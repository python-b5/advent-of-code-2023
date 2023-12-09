# Advent of Code 2023
# Day 9: Mirage Maintenance

histories = []

with open("inputs/day_9.txt") as file:
    for line in file:
        histories.append([int(n) for n in line.split(" ")])

next_prediction_sum = 0
prev_prediction_sum = 0

for history in histories:
    right_ends = [history[-1]]
    left_ends = [history[0]]

    working = history.copy()

    while True:
        for i in range(len(working) - 1, -1, -1):
            if i >= 1:
                working[i] = working[i] - working[i - 1]

        working = working[1:]

        if all(n == working[0] for n in working):
            next_prediction = working[-1]
            prev_prediction = working[0]

            for n in reversed(right_ends):
                next_prediction += n

            for n in reversed(left_ends):
                prev_prediction = n - prev_prediction

            next_prediction_sum += next_prediction
            prev_prediction_sum += prev_prediction

            break
        else:
            right_ends.append(working[-1])
            left_ends.append(working[0])

print(f"Part 1: {next_prediction_sum}")
print(f"Part 2: {prev_prediction_sum}")
