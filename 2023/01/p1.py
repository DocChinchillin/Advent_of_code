import time

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    sum = 0
    for line in lines:
        first = ''
        last = ''
        for c in line:
            if c.isdigit():
                if first == '':
                    first = c
                    last = c
                else:
                    last = c
        number = int(first + last)
        sum += number

    print(sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
