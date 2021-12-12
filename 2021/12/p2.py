import time
import numpy as np
from collections import Counter

def main():
    with open("input") as f:
        lines = f.read().splitlines()
    poti = dict()

    for line in lines:
        l,r = line.split("-")
        try:
            poti[l].add(r)
        except KeyError:
            poti[l] = {r}
        try:
            poti[r].add(l)
        except KeyError:
            poti[r] = {l}
    
    path = []
    koncne = []
    
    for zac in poti["start"]:
        path.append(["start",zac])

    looked = set(tuple(i) for i in path)
    
    while path:
        p = path.pop()
        if p[-1] == "end":
            koncne.append(p)
            continue
        try:
            for nasledni in poti[p[-1]]:
                a = p.copy()
                if nasledni == "start":
                    continue

                if nasledni.islower() :
                    if nasledni in a:
                        if doubleSmallCave(a):
                            continue
                
                a.append(nasledni)
                if tuple(a) not in looked:
                    path.append(a)
                    looked.add(tuple(a))

        except KeyError:
            if p[-1] == "end":
                koncne.append(p)

    print(len(koncne))

def doubleSmallCave(list):
    for element,count in Counter(list).most_common():
        
        if element.isupper():
            continue
        
        if element == "start":
            continue

        if count == 2:
            return True
        
    return False

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}") 