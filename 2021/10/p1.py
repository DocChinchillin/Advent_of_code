import time
import numpy as np

def main():
    with open("input") as f:
        digits = np.array(f.read().splitlines())

    err = 0
    for string in digits:
        stack = []
        for char in string:
            if char in {"(","[","{","<"}: stack.append(char)
            else:
                opp = stack.pop()
                if char == ")":
                    if opp != "(":
                        err += priceER(char)
                        break
                elif char == "]":
                    if opp != "[":
                        err += priceER(char)
                        break
                elif char == "}":
                    if opp != "{":
                        err += priceER(char)
                        break
                elif char == ">":
                    if opp != "<":
                        err += priceER(char)
                        break

    print(err)

def priceER(c):
    if c == ")": return 3
    if c == "]": return 57
    if c == "}": return 1197
    if c == ">": return 25137

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}") 