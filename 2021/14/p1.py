import time
import numpy as np
from collections import Counter


def main():
    with open("input") as f:
        lines = f.read().splitlines()
   
    dots = lines[0]
    folds = lines[2:]

    inserts = dict()
    for fold in folds:
        a,b = fold.split(" -> ")
        inserts[a] = b
    
    dots = list(dots)
    for _ in range(10):
        #print(dots)
        check = list()
        vel = len(dots)-1
        for i in range(vel):
            check.append(dots[i]+dots[i+1])
        
        dots = intersperse(dots," ")
        
        for i in range(vel):
            if check[i] in inserts:
                dots[i*2+1] = inserts[check[i]]
        dots = list(filter((" ").__ne__,dots))
        
    c = Counter(dots)
    val = c.values()
    m = max(val)
    n = min(val)
    
    print(m-n)
        

def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result
    


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}") 