import time
import numpy as np


def main():

    with open('input') as f:
        lines = f.read().splitlines()

    forest = np.array([np.array([c for c in line]) for line in lines])
    count = 0
    for x in range(forest.shape[0]):
        for y in range(forest.shape[1]):
            a = forest[:x, y] < forest[x, y]
            b = forest[x, :y] < forest[x, y]
            c = forest[x+1:, y] < forest[x, y]
            d = forest[x, y+1:] < forest[x, y]

            if (np.all(a) or np.all(b) or np.all(c) or np.all(d)
                    or a.size == 0 or b.size == 0 or c.size == 0 or d.size == 0):
                count += 1

    print(count)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
