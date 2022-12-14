import time
import numpy as np


def debugFile(cave):
    strCave = np.empty_like(cave, dtype=str)
    strCave[cave == 0] = ' '
    strCave[cave == 1] = '#'
    strCave[cave == 2] = 'o'

    with open("debug", "w") as f:
        for c in strCave:
            for n in c:
                f.write(str(n))
            f.write("\n")


def tryFall(cave, loc):
    y, x = loc

    if 0 == cave[y+1, x]:
        return 1, (y+1, x)

    if 0 == cave[y+1, x - 1]:
        return 1, (y+1, x - 1)

    if 0 == cave[y+1, x + 1]:
        return 1, (y+1, x + 1)

    cave[y, x] = 2
    if y == 0 and x == 300:
        return 2, None

    return 0, None


def main():

    with open('input') as f:
        lines = f.read().splitlines()
    cave = np.zeros((200, 600), dtype=int)

    offset = -200
    maxY = 0
    for line in lines:
        kords = line.split(' -> ')
        for k1, k2 in zip(kords, kords[1:]):
            x, y = k1.split(',')
            x, y = int(x) + offset, int(y)

            x2, y2 = k2.split(',')
            x2, y2 = int(x2) + offset, int(y2)

            maxY = max(maxY, y, y2)

            if x > x2:
                x, x2 = x2, x

            if y > y2:
                y, y2 = y2, y

            cave[y:y2+1, x:x2+1] = 1

    cave[maxY+2, :] = 1

    fallOut = False
    sandStoped = True

    while not fallOut:
        if sandStoped:
            loc = (0, 500 + offset)
            sandStoped = False

        mov, loc = tryFall(cave, loc)
        if mov == 2:
            fallOut = True
        elif mov == 0:
            sandStoped = True

    print(np.count_nonzero(cave == 2))
    debugFile(cave)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
