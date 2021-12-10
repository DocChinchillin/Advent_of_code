import time
import numpy as np

def main():
    with open("input") as f:
        digits = np.array(f.read().splitlines())

    points = {"(": 1, "[":  2,"{": 3, "<": 4}
    oklepaji ={ "(": ")", "[": "]","{": "}", "<": ">"}

    total = []

    for string in digits:
        stack = []
        broken = False
        for char in string:
            if char in {"(","[","{","<"}: stack.append(char)
            else:
                opp = stack.pop()
                if oklepaji[opp] != char:
                    broken = True
                    break
        if broken:
            continue

        temp_score = 0

        for oklep in reversed(stack):
            temp_score *= 5
            temp_score += points[oklep]
        
        total.append(temp_score)

    print(np.median(total))
 
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}") 