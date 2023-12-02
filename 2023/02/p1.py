import time

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    sum = 0
    limits = {'red': 12, 'green':13, 'blue': 14}
    for id,line in enumerate(lines):
        info = line.split(': ')[1]
        games = info.split(';')
        valid = 1

        for game in games:
            for cubes in game.split(','):
                num, col = cubes.strip().split(' ')
                if limits[col] < int(num):
                    valid = 0
                    break

        if valid == 1:
            sum = sum + 1 + id
        

    print(sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
