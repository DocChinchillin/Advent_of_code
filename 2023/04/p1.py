import time

def getPoints(num):
    if num < 1:
        return 0
    else:
        return 2**(num-1)


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
    sum = 0
    for line in lines:
        card,info =line.split(':')
        part1,part2 = info.split('|')
        winners = set(part1.strip().split())
        numbers = set(part2.strip().split())
  
        
        numberOfWinners = len(numbers.intersection(winners))
        sum += getPoints(numberOfWinners)
   

    print(sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
