# Advent of Code 2023
# Day 19: Aplenty

from copy import deepcopy
from functools import reduce
from json import loads
from operator import mul
from re import sub

workflows = {}
parts = []

with open("inputs/day_19.txt") as file:
    half = 0

    for line in file:
        if half == 0:
            if line == "\n":
                half = 1
            else:
                halves = line.split("{")
                halves[1] = halves[1].rstrip("\n")[:-1]

                conditions = []

                for condition in halves[1].split(","):
                    if condition == "A":
                        conditions.append(True)
                    elif condition == "R":
                        conditions.append(False)
                    elif ":" not in condition:
                        conditions.append(condition)
                    else:
                        condition_halves = condition.split(":")

                        if condition_halves[1] == "A":
                            result = True
                        elif condition_halves[1] == "R":
                            result = False
                        else:
                            result = condition_halves[1]

                        conditions.append((
                            condition_halves[0][1],
                            "xmas".index(condition_halves[0][0]),
                            int(condition_halves[0][2:]),
                            result
                        ))

                workflows[halves[0]] = conditions
        else:
            parts.append(list(loads(sub(
                r"([xmas])=", r'"\g<1>": ', line.rstrip("\n")
            )).values()))

rating_sum = 0

for part in parts:
    workflow = workflows["in"]
    done = False

    while not done:
        for condition in workflow:
            if condition == True:
                rating_sum += sum(part)
                done = True
                break
            elif condition == False:
                done = True
                break
            elif isinstance(condition, str):
                workflow = workflows[condition]
            else:
                if condition[0] == "<":
                    pass_ = part[condition[1]] < condition[2]
                else:
                    pass_ = part[condition[1]] > condition[2]

                if pass_:
                    if condition[3] == True:
                        rating_sum += sum(part)
                        done = True
                    elif condition[3] == False:
                        done = True
                    else:
                        workflow = workflows[condition[3]]

                    break

print(f"Part 1: {rating_sum}")

states = [["in", [1, 4000], [1, 4000], [1, 4000], [1, 4000]]]
combinations = 0

while states:
    new_states = []

    for state in states:
        for condition in workflows[state[0]]:
            if condition == True:
                combinations += reduce(
                    mul, (range_[1] - range_[0] + 1 for range_ in state[1:])
                )

                break
            elif isinstance(condition, str):
                state[0] = condition
                new_states.append(state)
                break
            elif condition != False:
                state_pass = deepcopy(state)
                range_pass = state_pass[condition[1] + 1]

                range_pass[condition[0] == "<"] = (
                    condition[2] + (1, -1)[condition[0] == "<"]
                )

                state[condition[1] + 1][condition[0] == ">"] = condition[2]

                if range_pass[0] <= range_pass[1]:
                    if condition[3] == True:
                        combinations += reduce(mul, (
                            range_[1] - range_[0] + 1
                            for range_ in state_pass[1:]
                        ))
                    elif condition[3] != False:
                        state_pass[0] = condition[3]
                        new_states.append(state_pass)

    states = new_states

print(f"Part 2: {combinations}")
