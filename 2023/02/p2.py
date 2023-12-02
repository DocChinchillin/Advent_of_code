import time

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    sum = 0
    for line in lines:
        info = line.split(': ')[1]
        games = info.split(';')
        limits = {'red': 0, 'green':0, 'blue': 0}
        for game in games:
            for cubes in game.split(','):
                num, col = cubes.strip().split(' ')
                if limits[col] < int(num):
                    limits[col] = int(num)

        power = 1
        for vals in limits.values():
            power *= vals
        sum += power
        

    print(sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
