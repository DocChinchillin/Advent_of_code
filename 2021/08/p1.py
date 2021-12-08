import time
import numpy as np

def main():
    with open("input") as f:
        digits = np.array(f.read().splitlines())

    count = 0
    for digit in digits:
        input,output = digit.split(" | ")
        
        #inputs = np.array(input.split(" "))
        outputs = np.array(output.split(" "))
        for out in outputs:
            if len(out) in [2,3,4,7]:
                count+=1

    print(count) #392


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}") 