import time


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    sums = [0]
    elf = 0
    for line in lines:
        if line == '':
            elf += 1
            sums.append(0)
            continue
        sums[elf] += int(line)

    print(sum(sorted(sums, reverse=True)[:3]))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
