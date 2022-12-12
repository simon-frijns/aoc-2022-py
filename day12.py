with open("day12.txt") as data:
    raw = data.read().strip().split("\n")

nodes = [[x for x in row] for row in raw]
height = len(nodes)
width = len(nodes[0])
starting_items = []
end = ()
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
part2 = True

for y_idx, row in enumerate(nodes):
    for x_idx, char in enumerate(row):
        if char == "S" or (part2 and char == "a"):
            starting_items.append(((x_idx, y_idx), 0))
            char = "a"
        if char == "E":
            end = (x_idx, y_idx)
            char = "z"
        nodes[y_idx][x_idx] = ord(char)


def find_shortest_path(starting_position):
    queue = []
    steps = set()
    queue.append(starting_position)
    while queue:
        cur_node, distance = queue.pop(0)
        if cur_node in steps:
            continue
        steps.add(cur_node)
        if cur_node == end:
            return distance
        for dx, dy in directions:
            old_x, old_y = cur_node
            x = old_x + dx
            y = old_y + dy
            if x in range(width) and y in range(height):
                old_alt = nodes[old_y][old_x]
                alt = nodes[y][x]
                if old_alt + 1 >= alt:
                    queue.append(((x, y), distance + 1))


results = []

for starting_item in starting_items:
    shortest_path = find_shortest_path(starting_item)
    if shortest_path:
        results.append(shortest_path)

print(min(results))
