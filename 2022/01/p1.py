import time


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    sum = [0]
    elf = 0
    for line in lines:
        if line == '':
            elf += 1
            sum.append(0)
            continue
        sum[elf] += int(line)

    print(max(sum))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
