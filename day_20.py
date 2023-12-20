# Advent of Code 2023
# Day 20: Pulse Propagation

from math import lcm

class FlipFlop:
    def __init__(self, destinations):
        self.destinations = destinations
        self.on = False

    def recieve(self, name, pulse):
        if pulse == "low":
            self.on = not self.on

            if self.on:
                return [(name, "high") for name in self.destinations]
            else:
                return [(name, "low") for name in self.destinations]
        else:
            return []

class Conjunction:
    def __init__(self, destinations):
        self.destinations = destinations
    
    def init_memory(self, connected_modules):
        self.memory = {name: "low" for name in connected_modules}

    def recieve(self, name, pulse):
        self.memory[name] = pulse

        if all(pulse == "high" for pulse in self.memory.values()):
            return [(name, "low") for name in self.destinations]
        else:
            return [(name, "high") for name in self.destinations]

modules = {}
conjunctions = {}

with open("inputs/day_20.txt") as file:
    for line in file:
        if line.startswith("broadcaster"):
            starting_destinations = (
                line.split(" -> ")[1].rstrip("\n").split(", ")
            )
        else:
            halves = line.split(" -> ")
            kind = (FlipFlop, Conjunction)[halves[0][0] == "&"]
            name = halves[0][1:]
            destinations = halves[1].rstrip("\n").split(", ")

            modules[name] = kind(destinations)

            if kind == Conjunction:
                conjunctions[name] = modules[name]

            if "rx" in destinations:
                final_conjunction = modules[name]

for conjunction_name, conjunction in conjunctions.items():
    connected_modules = []

    if conjunction_name in starting_destinations:
        connected_modules.append("broadcaster")

    for name, module in modules.items():
        if conjunction_name in module.destinations:
            connected_modules.append(name)

    conjunction.init_memory(connected_modules)

low_pulses = 1000
high_pulses = 0

presses = 1
cycles = {name:None for name in final_conjunction.memory}

while presses <= 1000 or any(cycle is None for cycle in cycles.values()):
    pulses = [("broadcaster", name, "low") for name in starting_destinations]

    while pulses:
        next_pulses = []

        for pulse in pulses:
            if (
                pulse[0] in cycles and pulse[2] == "high"
                and cycles[pulse[0]] is None
            ):
                cycles[pulse[0]] = presses

            if pulse[1] in modules:
                for next_pulse in modules[pulse[1]].recieve(
                    pulse[0], pulse[2]
                ):
                    next_pulses.append((pulse[1],) + next_pulse)

            if presses <= 1000:
                if pulse[2] == "low":
                    low_pulses += 1
                else:
                    high_pulses += 1

        pulses = next_pulses

    presses += 1

print(f"Part 1: {low_pulses * high_pulses}")
print(f"Part 2: {lcm(*cycles.values())}")
