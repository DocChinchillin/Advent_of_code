import time
import numpy as np


def checkSide(lava, y, x, z):
    if 0 > y or y > 25:
        return 1

    if 0 > x or x > 25:
        return 1

    if 0 > z or z > 25:
        return 1

    if lava[y, x, z] == 2:
        return 1
    return 0


def expandSteam(lava, y, x, z):
    if 0 > y or y >= 25:
        return

    if 0 > x or x >= 25:
        return

    if 0 > z or z >= 25:
        return

    if lava[y, x, z] == 0:
        lava[y, x, z] = 2  # add steam
        return (y, x, z)
    return


def main():

    with open('input') as f:
        lines = f.read().splitlines()
    # max in every dir is about 20
    lava = np.zeros((25, 25, 25))
    for line in lines:
        x, y, z = line.split(',')
        x = int(x)
        y = int(y)
        z = int(z)
        lava[y, x, z] = 1
    steam = [(0, 0, 0)]
    cnt = 0
    while steam:
        if steam[0] is None:
            steam.pop(0)
            continue
        y, x, z = steam.pop(0)
        steam.append(expandSteam(lava, y + 1, x, z))
        steam.append(expandSteam(lava, y - 1, x, z))
        steam.append(expandSteam(lava, y, x+1, z))
        steam.append(expandSteam(lava, y, x-1, z))
        steam.append(expandSteam(lava, y, x, z+1))
        steam.append(expandSteam(lava, y, x, z-1))

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
