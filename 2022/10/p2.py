import time


def addDisplay(x, clk, display):
    if x-1 <= (clk % 40)-1 <= x+1:
        display += '#'
    else:
        display += ' '
    return display


def flushDisplay(clk, mod, display):
    if clk % mod == 0:
        mod += 40
        print(display)
        display = ""

    return mod, display


def main():

    with open('input') as f:
        lines = f.read().splitlines()

    clk = 0
    x = 1
    mod = 40
    display = ""

    for line in lines:
        if clk == 8:
            print(clk)
        if line.startswith('noop'):
            clk += 1
            display = addDisplay(x, clk, display)
            mod, display = flushDisplay(clk, mod, display)

        if line.startswith('addx'):
            _, val = line.split(" ")

            clk += 1
            display = addDisplay(x, clk, display)
            mod, display = flushDisplay(clk, mod, display)

            clk += 1
            display = addDisplay(x, clk, display)
            mod, display = flushDisplay(clk, mod, display)

            x += int(val)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
