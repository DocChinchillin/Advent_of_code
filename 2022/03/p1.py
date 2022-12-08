import time
import string


def main():
    priority = {c: n+1 for n, c in enumerate(string.ascii_letters)}

    with open('input') as f:
        lines = f.read().splitlines()

    sum = 0
    for backpack in lines:
        firstpart, secondpart = backpack[:len(
            backpack)//2], backpack[len(backpack)//2:]
        for char in firstpart:
            if char in secondpart:
                sum += priority[char]
                break

    print(sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
