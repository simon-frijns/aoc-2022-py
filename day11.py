import re

with open("day11.txt") as data:
    raw = data.read().strip().split("\n\n")


class Monkey:
    def __init__(self, number, items, operation, test, if_true, if_false):
        self.number = number
        self.items = items
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.total_inspections = 0
        self.lambdaop = staticmethod(lambda old: eval(operation))  # ew

    def __str__(self):
        return f"Monkey {self.number}, test {self.test}, total inspections {self.total_inspections}, items {self.items}"

    def do_lambda_operation(self):
        old = self.items[0]
        self.items.pop(0)
        return self.lambdaop(old)


monkeys = []
mods = []

for monkey_description in raw:
    m = monkey_description.strip().split("\n")
    number = re.search("\d", m[0])
    items = list(map(int, re.findall("\d+", m[1])))
    operation = re.split("=", m[2])[1]
    test = int(re.findall("\d+", m[3])[0])
    if_true = int(re.search("\d", m[4])[0])
    if_false = int(re.search("\d", m[5])[0])
    monkeys.append(Monkey(number, items, operation, test, if_true, if_false))
    mods.append(test)

mod = 1
for i in mods:
    mod *= i

for round in range(10000):
    for monkey in monkeys:
        monkey.total_inspections += len(monkey.items)
        while monkey.items:
            # item = monkey.do_lambda_operation() // 3 # uncomment for part 1
            item = monkey.do_lambda_operation() % mod
            if item % monkey.test == 0:
                monkeys[monkey.if_true].items.append(item)
            else:
                monkeys[monkey.if_false].items.append(item)

inspections = []
for monkey in monkeys:
    inspections.append(monkey.total_inspections)
inspections.sort()

print(inspections[-1] * inspections[-2])
