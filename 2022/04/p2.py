import time


def main():

    with open('input') as f:
        lines = f.read().splitlines()

    count = 0

    for line in lines:
        a, b = line.split(',')

        aMin, aMax = [int(a) for a in a.split('-')]
        bMin, bMax = [int(b) for b in b.split('-')]

        # a contained in b
        if bMin <= aMin and aMax <= bMax:
            count += 1
            continue

        # b contained in a
        if aMin <= bMin and bMax <= aMax:
            count += 1
            continue

        if aMin <= bMax and bMin <= aMax:
            count += 1
            continue

        if bMin <= aMax and aMin <= bMax:
            count += 1
            continue

    print(count)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
