# Advent of Code 2023
# Day 25: Snowverload

import networkx

graph = {}

with open("inputs/day_25.txt") as file:
    for line in file:
        component = line[:3]

        if component in graph:
            graph[component].update(set(line[5:].rstrip("\n").split(" ")))
        else:
            graph[component] = set(line[5:].rstrip("\n").split(" "))

        for other in graph[component]:
            if other not in graph:
                graph[other] = set([component])
            else:
                graph[other].add(component)

to_remove = tuple(networkx.minimum_edge_cut(networkx.from_dict_of_lists(graph)))

for edge in to_remove:
    graph[edge[0]].remove(edge[1])
    graph[edge[1]].remove(edge[0])

product = 1

for edge in to_remove[0]:
    queue = [edge]
    seen = set()

    while queue:
        current = queue.pop(0)

        for next_ in graph[current]:
            if next_ not in seen:
                queue.append(next_)
                seen.add(next_)

    product *= len(seen)

print(f"Part 1: {product}")
