import time
import numpy as np

def main():
    with open("input") as f:
        crabs = np.array(f.read().splitlines()[0].split(","),dtype = "int16")

    inital_i, initial_count = np.unique(crabs, return_counts = True)

    move_cost = []
    
    for i in range(0,max(inital_i) + 1):
        move_cost.append(sum(abs(inital_i - i) * initial_count))

    print(min(move_cost))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")