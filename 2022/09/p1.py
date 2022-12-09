import time


def main():

    with open('input') as f:
        lines = f.read().splitlines()

    x, y = 0, 0
    tX, tY = 0, 0
    visited = set()

    for line in lines:
        dir, n = line.split(" ")

        xMov = -1 if dir == "L" else 1 if dir == "R" else 0
        yMov = -1 if dir == "D" else 1 if dir == "U" else 0

        for _ in range(int(n)):

            x += xMov
            y += yMov
            tX, tY = moveToHead(x, y, tX, tY)
            visited.add((tX, tY))

    print(len(visited))


def moveToHead(x, y, tX, tY):
    # straight moves
    if abs(x - tX) > 1 and y == tY:
        tX = tX + 1 if x > tX else tX-1

    if abs(y - tY) > 1 and x == tX:
        tY = tY + 1 if y > tY else tY-1

    # diagonal moves
    if (abs(x - tX) > 1 and y != tY) or (abs(y - tY) > 1 and x != tX):
        tY = tY + 1 if y > tY else tY-1
        tX = tX + 1 if x > tX else tX-1

    return tX, tY


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
