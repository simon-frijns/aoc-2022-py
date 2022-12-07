with open("day06.txt") as raw:
    data = raw.read().strip()

num = 14 # 4 for p1

for i in range(len(data)):
    if len(set(data[i:i+num])) == num:
        print(i+num)
        break