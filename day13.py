with open("day13.txt") as input:
    raw = input.read().split("\n\n")

pairs = []
lines = []
for pair in raw:
    a, b = pair.split("\n")
    pairs.append([eval(a), eval(b)])
    lines.append(eval(a))
    lines.append(eval(b))


def compare(left, right):
    if type(left) == int and type(right) == list:
        return compare([left], right)
    if type(left) == list and type(right) == int:
        return compare(left, [right])
    if type(left) == list and type(right) == list:
        for left_digit, right_digit in zip(left, right):
            x = compare(left_digit, right_digit)
            if x is not None:
                return x
        return compare(len(left), len(right))
    if type(left) == int and type(right) == int:
        if right > left:
            return True
        elif right < left:
            return False
    return None


cnt = 0
part1 = 0

for pair in pairs:
    cnt += 1
    if compare(pair[0], pair[1]):
        part1 += cnt

part2 = [1, 2]

for i, decoder in enumerate([[[2]], [[6]]]):
    for line in lines:
        if compare(line, decoder):
            part2[i] += 1

print(part1)
print(part2[0] * part2[1])
