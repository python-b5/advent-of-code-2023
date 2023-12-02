# Advent of Code 2023
# Day 2: Cube Conundrum

id_sum = 0
power_sum = 0

with open("inputs/day_2.txt") as file:
    for i, line in enumerate(file):
        handfuls = [
            [
                {
                    "amount": int((split := color.split(" "))[0]),
                    "color": split[1],
                }
                for color in handful.split(", ")
            ]
            for handful in line.rstrip("\n").split(": ")[1].split("; ")
        ]

        possible = True

        red_max = 0
        green_max = 0
        blue_max = 0

        for handful in handfuls:
            red = 0
            green = 0
            blue = 0

            for color in handful:
                if color["color"] == "red":
                    red += color["amount"]
                elif color["color"] == "green":
                    green += color["amount"]
                elif color["color"] == "blue":
                    blue += color["amount"]

            if red > 12 or green > 13 or blue > 14:
                possible = False

            if red > red_max:
                red_max = red
            if green > green_max:
                green_max = green
            if blue > blue_max:
                blue_max = blue

        if possible:
            id_sum += i + 1

        power_sum += red_max * green_max * blue_max

print(f"Day 1: {id_sum}")
print(f"Day 2: {power_sum}")
