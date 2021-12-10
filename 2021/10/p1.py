import time
import numpy as np

def main():
    with open("input") as f:
        digits = np.array(f.read().splitlines())

    points = {")": 3, "]":  57,"}": 1197, ">": 25137}
    oklepaji ={ "(": ")", "[": "]","{": "}", "<": ">"}

    err = 0
    for string in digits:
        stack = []
        for char in string:
            if char in {"(","[","{","<"}: stack.append(char)
            else:
                opp = stack.pop()
                if char != oklepaji[opp]:
                    err += points[char]
                    break

    print(err)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}") 