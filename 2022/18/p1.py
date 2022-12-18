import time
import numpy as np


def checkSide(lava, y, x, z):
    if 0 > y or y > 100:
        return 1

    if 0 > x or x > 100:
        return 1

    if 0 > z or z > 100:
        return 1

    if lava[y, x, z] == 0:
        return 1
    return 0


def main():

    with open('input') as f:
        lines = f.read().splitlines()

    lava = np.zeros((100, 100, 100))

    for line in lines:
        x, y, z = line.split(',')
        x = int(x)
        y = int(y)
        z = int(z)
        lava[y, x, z] = 1
    cnt = 0
    for y, x, z in zip(*np.where(lava == 1)):
        cnt += checkSide(lava, y + 1, x, z)
        cnt += checkSide(lava, y - 1, x, z)
        cnt += checkSide(lava, y, x+1, z)
        cnt += checkSide(lava, y, x-1, z)
        cnt += checkSide(lava, y, x, z+1)
        cnt += checkSide(lava, y, x, z-1)

    print(cnt)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
