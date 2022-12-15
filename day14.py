with open("day14.txt") as input:
    raw = input.read().split("\n")

rocks = set()

for line in raw:  # parsing is ew
    elems = line.split("->")
    for i in zip(elems, elems[1:]):
        fr, to = [x.strip() for x in i]
        x_fr, y_fr = list(map(int, fr.strip().split(",")))
        x_to, y_to = list(map(int, to.strip().split(",")))
        xs = sorted([x_fr, x_to])
        ys = sorted([y_fr, y_to])
        xr = range(xs[0], xs[1] + 1)
        yr = range(ys[0], ys[1] + 1)
        for x in xr:
            for y in yr:
                rocks.add((x, y))

sand = (500, 0)
directions = [(0, 1), (-1, 1), (1, 1)]
y_void = max(y for _, y in rocks)
for i in range(-5000, 5000):  # lazy solution for floor, ew
    rocks.add((i, y_void + 2))
blocked = set()
for rock in rocks:
    blocked.add(rock)

sand_x, sand_y = sand
part1 = False

while True:
    falling = False
    for dx, dy in directions:
        if (sand_x + dx, sand_y + dy) not in blocked:
            sand_x += dx
            sand_y += dy
            falling = True
            break
    if part1 and sand_y > y_void:
        break
    if not falling:
        blocked.add((sand_x, sand_y))
        if (sand_x, sand_y) == sand:
            break
        sand_x, sand_y = sand

print(len(blocked) - len(rocks))
