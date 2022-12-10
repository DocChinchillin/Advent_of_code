import time


def addSum(clk, mod, sum, x):
    if clk % mod == 0:
        mod += 40
        sum += x * clk
    return mod, sum


def main():

    with open('input') as f:
        lines = f.read().splitlines()

    clk = 0
    x = 1
    sum = 0
    mod = 20
    for line in lines:
        if line.startswith('noop'):
            clk += 1
            mod, sum = addSum(clk, mod, sum, x)

        if line.startswith('addx'):
            _, val = line.split(" ")
            clk += 1
            mod, sum = addSum(clk, mod, sum, x)

            clk += 1
            mod, sum = addSum(clk, mod, sum, x)

            x += int(val)

    print(sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
