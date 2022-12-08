import time


def main():

    with open('input') as f:
        lines = f.read().splitlines()

    movements, boxs = lines[lines.index("")+1:], lines[:lines.index("")]

    boxs.reverse()
    col = [[] for i in range(int(boxs[0][-2]))]

    for row in boxs[1:]:
        parts = [row[i] for i in range(1, len(row), 4)]
        for n, box in enumerate(parts):
            if box != " ":
                col[n].append(box)

    for move in movements:
        _, num, _, l1, _, l2 = [
            int(a) if a.isdecimal() else None for a in move.split(" ")]
        poped = []
        for n in range(num):
            poped.append(col[l1-1].pop())
        poped.reverse()
        for p in poped:
            col[l2-1].append(p)

    print("".join([c[len(c)-1] for c in col]))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
