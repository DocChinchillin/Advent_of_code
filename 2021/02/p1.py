def main():
    with open('input.txt') as f:
        lines = f.readlines()

    depth = 0
    pos = 0


    for line in lines:
        sp = line.split(" ")
        com = sp[0]
        number = int(sp[1].replace("\n",""))
        if com == "forward":
            pos += number
        if com == "down":
            depth+=number
        if com == "up":
            depth -= number
    
    print(pos * depth)


if __name__ == "__main__":
    main()