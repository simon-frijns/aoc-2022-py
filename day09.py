with open("day09.txt") as data:
    raw = data.read().strip().split("\n")


def move(head, direction):
    match direction:
        case "R":
            head[0] += 1
        case "L":
            head[0] -= 1
        case "U":
            head[1] += 1
        case "D":
            head[1] -= 1
    return head


def follow(head, tail):
    hor_distance = head[0] - tail[0]
    vert_distance = head[1] - tail[1]
    if abs(hor_distance) + abs(vert_distance) > 2:
        if hor_distance > 0 and vert_distance > 0:
            tail[0] += 1
            tail[1] += 1
        if hor_distance > 0 and vert_distance < 0:
            tail[0] += 1
            tail[1] -= 1
        if hor_distance < 0 and vert_distance < 0:
            tail[0] -= 1
            tail[1] -= 1
        if hor_distance < 0 and vert_distance > 0:
            tail[0] -= 1
            tail[1] += 1
    elif abs(hor_distance) > 1 or abs(vert_distance) > 1:
        if hor_distance > 1:
            tail[0] += 1
        if hor_distance < -1:
            tail[0] -= 1
        if vert_distance > 1:
            tail[1] += 1
        if vert_distance < -1:
            tail[1] -= 1
    return tail


def run_snake(snake):
    tailspots = set()
    for line in raw:
        direction, steps = line.split()
        for _ in range(int(steps)):
            snake[0] = move(snake[0], direction)
            for i in range(1, len(snake)):
                snake[i] = follow(snake[i - 1], snake[i])
            tailspots.add(tuple(snake[-1]))
    return len(tailspots)


print(run_snake([[0, 0] for _ in range(2)]))
print(run_snake([[0, 0] for _ in range(10)]))
