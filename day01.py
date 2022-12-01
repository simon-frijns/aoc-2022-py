with open("day01.txt") as raw:
    data = raw.read().strip().split("\n\n")
    data = [[int(x) for x in y.split("\n")] for y in data]
sums = [sum(x) for x in data]
print(max(sums))
print(sum(sorted(sums, reverse=True)[:3]))