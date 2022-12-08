import time

score = {'A': 1, 'B': 2, 'C': 3}


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    sum = 0
    for line in lines:
        elf, result = line.split(' ')
        elf = score[elf]
        chosenMe = choose(elf, result)
        sum += chosenMe
        sum += win(elf, chosenMe)

    print(sum)


def win(elf, me):
    # draw
    if elf == me:
        return 3

    # scissors vs rock
    if elf == 3 and me == 1:
        return 6

    # rock vs scissors
    if elf == 1 and me == 3:
        return 0

    if elf < me:
        return 6
    else:
        return 0


def choose(elf, result):
    # draw
    if result == 'Y':
        return elf
    # lose
    if result == 'X':
        return 3 if elf - 1 < 1 else elf - 1
    # win
    if result == 'Z':
        return 1 if elf + 1 > 3 else elf + 1


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
