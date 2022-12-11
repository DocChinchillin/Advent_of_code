import time


class Monkey():
    combinedMod = 1

    def __init__(self, items: list[int], operation, mod: int,
                 throwTrue: int, throwFalse: int, n):
        self.count = 0
        self.items = items
        self.op = operation
        self.mod = mod
        self.throwTrue = throwTrue
        self.throwFalse = throwFalse
        self.n = n
        Monkey.combinedMod *= mod

    def inspectItems(self, monList: list):
        for item in self.items:
            self.count += 1
            n = self.n if self.n else item
            item = self.doCalc(item, n)
            item = item % Monkey.combinedMod

            if item % self.mod == 0:
                monList[self.throwTrue].items.append(item)
            else:
                monList[self.throwFalse].items.append(item)

        self.items = []

    def doCalc(self, old, n):
        if self.op == '+':
            return old + n
        if self.op == '*':
            return old * n


def readMonkey(lines):
    monList: list(Monkey) = []

    # read monkey
    for monkey in lines:
        monkey = monkey.split('\n')
        items = [int(item) for item in monkey[1].removeprefix(
            "  Starting items:").split(",")]

        operation = monkey[2].split(" ")[6]
        mod = monkey[3].split(" ")[-1]
        throwTrue = monkey[4].split(" ")[-1]
        throwFalse = monkey[5].split(" ")[-1]

        n = monkey[2].split(" ")[-1]

        if n == 'old':
            n = None
        else:
            n = int(n)

        m = Monkey(items, operation, int(mod), int(
            throwTrue), int(throwFalse), n)
        monList.append(m)

    return monList


def main():

    with open('input') as f:
        lines = f.read().split("\n\n")

    monList = readMonkey(lines)

    i = 0
    while i < 10000:
        m: Monkey
        for m in monList:
            m.inspectItems(monList)

        i += 1
    counts = []
    m: Monkey
    for m in monList:
        counts.append(m.count)

    counts.sort(reverse=True)

    print(counts[0] * counts[1])


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
