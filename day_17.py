# Advent of Code 2023
# Day 17: Clumsy Crucible

import heapq

with open("inputs/day_17.txt") as file:
    loss_map = [[int(char) for char in line.rstrip("\n")] for line in file]
    width = len(loss_map[0])
    height = len(loss_map)

class Node:
    def __init__(self, x, y, direction, consecutive, heat_loss, part):
        self.x = x
        self.y = y
        self.direction = direction
        self.consecutive = consecutive
        self.heat_loss = heat_loss
        self.part = part

    def __lt__(self, other):
        return self.heat_loss < other.heat_loss

heap = [Node(0, 0, None, 0, 0, 1), Node(0, 0, None, 0, 0, 2)]
heapq.heapify(heap)
seen = set()

end_x = width - 1
end_y = height - 1

while heap:
    current = heapq.heappop(heap)

    if current.x == end_x and current.y == end_y:
        print(f"Part {current.part}: {current.heat_loss}")

        for node in heap.copy():
            if node.part == current.part:
                heap.remove(node)

        continue

    for new_pos in (
        (current.x + 1, current.y, "right"),
        (current.x, current.y + 1, "down"),
        (current.x - 1, current.y, "left"),
        (current.x, current.y - 1, "up")
    ):
        if (
            0 <= new_pos[0] < width and 0 <= new_pos[1] < height
            and not (
                current.direction == "right" and new_pos[2] == "left"
                or current.direction == "down" and new_pos[2] == "up"
                or current.direction == "left" and new_pos[2] == "right"
                or current.direction == "up" and new_pos[2] == "down"
            )
            and not (
                current.direction == new_pos[2]
                and current.consecutive == (3, 10)[current.part - 1]
            )
        ):
            node = Node(
                *new_pos,
                (
                    current.consecutive + 1
                    if current.direction == new_pos[2] else 1
                ),
                current.heat_loss + loss_map[new_pos[1]][new_pos[0]],
                current.part
            )

            if current.part == 2 and node.consecutive == 1:
                if node.direction == "right":
                    change = (1, 0)
                elif node.direction == "down":
                    change = (0, 1)
                elif node.direction == "left":
                    change = (-1, 0)
                else:
                    change = (0, -1)

                for i in range(3):
                    node.x += change[0]
                    node.y += change[1]

                    try:
                        node.heat_loss += loss_map[node.y][node.x]
                    except IndexError:
                        pass

                node.consecutive = 4

            values = (node.x, node.y, node.direction, node.consecutive)

            if values not in seen:
                heapq.heappush(heap, node)
                seen.add(values)
