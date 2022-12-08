import time


class Dir():
    def __init__(self, parent, name, contain):
        self.parent = parent
        self.name = name
        self.contain = contain

    def getSize(self):
        return sum(a.getSize() for a in self.contain)

    def getSmaller(self):
        if self.getSize() > 100000:
            return sum(a.getSmaller() for a in self.contain)
        return sum(a.getSmaller() for a in self.contain) + self.getSize()

    def __eq__(self, other):
        return self.name == other


class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getSize(self):
        return self.size

    def getSmaller(self):
        return self.size


def main():

    with open('input') as f:
        lines = f.read().splitlines()

    root = Dir(None, '/', [])
    curDir = root

    for line in lines:
        if line.startswith("$ cd "):
            if line[5:] == '..':
                curDir = curDir.parent
            elif line[5:] == '/':
                curDir = root
            else:
                curDir = curDir.contain[curDir.contain.index(line[5:])]
            continue

        if line.startswith("dir "):
            curDir.contain.append(Dir(curDir, line[4:], []))
            continue

        if line.startswith("$ ls"):
            continue

        size, name = line.split(" ")
        curDir.contain.append(File(name, int(size)))

    # it just works
    print(root.getSmaller() - root.getSize())


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
