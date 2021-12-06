import time
import numpy as np

def main():
    with open("test") as f:
        fish = np.array(f.read().splitlines()[0].split(","),dtype = "byte")
    c = 0
    
    for i in range(0,80):
        fish = fish - 1
        fish = np.append(fish,np.array(c*[8],dtype = "byte"))
        c = np.count_nonzero(fish==0)
        fish = np.where(fish >= 0, fish , fish+7)
    print(len(fish))
        

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")