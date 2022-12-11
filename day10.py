with open("day10.txt") as data:
    raw = data.read().strip().split("\n")

cycle = 0
x = 1
part1 = 0


def do_cycle(cycle, part1, x):
    if cycle % 40 == 0:
        print("\n", end="")
    elif cycle % 40 == 20:
        part1 += cycle * x
    pixel = " "
    if abs(x - (cycle % 40)) < 2:
        pixel = "#"
    print(pixel, end="")
    cycle += 1
    return cycle, part1, x


for instruction in raw:
    op, *vals = instruction.strip().split()
    match op:
        case "addx":
            add = int(vals[0])
            cycle, part1, x = do_cycle(cycle, part1, x)
            cycle, part1, x = do_cycle(cycle, part1, x)
            x += add
        case "noop":
            cycle, part1, x = do_cycle(cycle, part1, x)

print(f"\n {part1}")
