def main():
    with open('input.txt') as f:
        lines = f.readlines()

    depth = 0
    pos = 0
    aim = 0


    for line in lines:
        sp = line.split(" ")
        com = sp[0]
        number = int(sp[1].replace("\n",""))
        if com == "forward":
            pos += number
            depth += number * aim
        if com == "down":
            aim += number
        if com == "up":
            aim -= number
    
    print(pos * depth)


if __name__ == "__main__":
    main()