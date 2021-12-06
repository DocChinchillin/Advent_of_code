import time
import numpy as np

def main():
    with open("input") as f:
        fish = np.array(f.read().splitlines()[0].split(","),dtype = np.int64)

    #fish = np.loadtxt("input", dtype=np.int64, delimiter=",") #slower

    c = np.array(range(0,7), dtype = np.int64)
    babies = np.zeros_like(range(0,4), dtype = np.int64)

    for i in range(0,7):
        c[i] = np.count_nonzero(fish == i)
    
    for i in range(0,256):
        paren = c[0]
        babies[3] += paren
        c[6] += babies[0]
        babies[0] = 0
        c = np.roll(c,-1)
        babies = np.roll(babies,-1)

    print(sum(c) + sum(babies)) # 1743335992042
        

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}") #Time is : 0.0059626102447509766