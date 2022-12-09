import time


def main():

    with open('input') as f:
        lines = f.read().splitlines()

    knots = [(0, 0) for _ in range(10)]
    visited = set()

    for line in lines:
        dir, n = line.split(" ")

        xMov = -1 if dir == "L" else 1 if dir == "R" else 0
        yMov = -1 if dir == "D" else 1 if dir == "U" else 0

        for _ in range(int(n)):

            x = xMov + knots[0][0]
            y = yMov + knots[0][1]
            knots[0] = (x, y)
            knots[1] = moveToHead(knots[0][0], knots[0][1],
                                  knots[1][0], knots[1][1])
            for i in range(1, 10):
                knots[i] = moveToHead(
                    knots[i-1][0], knots[i-1][1], knots[i][0], knots[i][1])

            visited.add(knots[9])

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

    return (tX, tY)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
