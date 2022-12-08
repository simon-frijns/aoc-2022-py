with open("day08.txt") as raw:
    data = raw.read().strip().split("\n")
    data = [[int(tree) for tree in row] for row in data]


part1 = 0
for x in range(len(data)):
    for y in range(len(data[0])):
        cur_height = data[x][y]
        for cardinal in [
            data[x][:y],  # left
            data[x][y + 1 :],  # right
            [tree[y] for tree in data[x + 1 :]],  # down
            [tree[y] for tree in data[:x]],  # up
        ]:
            is_visible = 0 if cardinal and cur_height <= max(cardinal) else 1
            if is_visible == 1:
                part1 += is_visible
                break

part2 = 0
for x in range(len(data)):
    for y in range(len(data[0])):
        cur_height = data[x][y]
        scores = []
        for sightline in [
            data[x][:y][::-1],  # left, mirrored
            data[x][y + 1 :],  # right
            [tree[y] for tree in data[x + 1 :]],  # down
            [tree[y] for tree in data[:x]][::-1],  # up, mirrored
        ]:
            score = 0
            for tree in sightline:
                score += 1
                if tree >= cur_height:
                    break
            scores.append(score)
        res = 1
        for s in scores:
            res *= s
        if res > part2:
            part2 = res

print(part1, part2)
