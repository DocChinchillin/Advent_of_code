import time

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    score = {'X':1,'Y':2,'Z':3}
    convert = {'A':'X','B':'Y','C':'Z'}
    sum = 0
    for line in lines:
        elf, me = line.split(' ')
        sum += score[me]
        sum += win(score[convert[elf]],score[me])
    
    
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

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")