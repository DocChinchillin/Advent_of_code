import time
import numpy as np


class QItem:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist

    def __repr__(self):
        return f"QItem({self.row}, {self.col}, {self.dist})"


# checking where move is valid or not
def isValid(x, y, grid, visited, cur):

    if ((x >= 0 and y >= 0) and
            (x < np.shape(grid)[1] and y < np.shape(grid)[0]) and (visited[y][x] == 0)):
        next = ord(grid[y][x]) if np.all(grid[y][x] != 'E') else ord('z')
        if next <= cur + 1:
            visited[y][x] = 1
            return True
        else:
            return False

    return False

# Function to perform the BFS traversal


def minDistance(grid, s):
    source = QItem(0, 0, 0)
    source.row = s[1]  # x
    source.col = s[0]  # y

    # To maintain location visit status
    visited = np.zeros(np.shape(grid))

    # applying BFS on matrix cells starting from source
    queue = []
    queue.append(source)

    while len(queue) != 0:
        source = queue.pop(0)
        visited[source.col][source.row] = 1

        # Destination found;
        if (np.any(grid[source.col][source.row] == 'E')):
            return source.dist
        cur = ord(grid[source.col][source.row]) if np.all(
            grid[source.col][source.row] != 'S') else ord('a')
        # moving up
        if isValid(source.row - 1, source.col, grid, visited, cur):
            queue.append(QItem(source.row - 1, source.col, source.dist + 1))

        # moving down
        if isValid(source.row + 1, source.col, grid, visited, cur):
            queue.append(QItem(source.row + 1, source.col, source.dist + 1))

        # moving left
        if isValid(source.row, source.col - 1, grid, visited, cur):
            queue.append(QItem(source.row, source.col - 1, source.dist + 1))

        # moving right
        if isValid(source.row, source.col + 1, grid, visited, cur):
            queue.append(QItem(source.row, source.col + 1, source.dist + 1))

    return -1


def main():

    with open('inputs') as f:
        lines = f.read().splitlines()

    cliff = np.array([np.array([c for c in line]) for line in lines])
    cliff[np.where(cliff == 'S')] = 'a'
    lengths = []
    start = np.where(cliff == 'a')
    for n in zip(start[0], start[1]):
        print(n)
        lengths.append(minDistance(cliff, n))

    print(min([i for i in lengths if i != -1]))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
