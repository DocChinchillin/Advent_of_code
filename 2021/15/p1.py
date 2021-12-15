import time
import numpy as np
import numpy.ma as ma
from collections import Counter


def main():
    with open("input") as f:
        digits = np.array(f.read().splitlines())

    sizey = digits.shape[0]
    sizex = len(digits[0])
    mat = np.zeros((sizey,sizex),dtype=np.int32)
    price = np.full((sizey,sizex),ma.minimum_fill_value(mat))
    
    
    for i,string in enumerate(digits):
        mat[i] = [num for num in string]
    

    end = (mat.shape[0]-1,mat.shape[1]-1)
    
    koncne = []

    paths = [[(0,1)],[(1,0)]]
    while paths:
        
        path = paths.pop()
        kord = path[len(path)-1]
        if kord == end:
            koncne.append(path)
            continue
        
        #sosedi = set([(i,j) if 0<=i<=mat.shape[0] and 0<=j<=mat.shape[1] else () for i in range(kord[0]-1,kord[0]+2)for j in range(kord[1]-1,kord[1]+2)])
        #sosedi = set([(kord[0]-1,kord[1]),(kord[0]+1,kord[1]),(kord[0],kord[1]-1),(kord[0],kord[1]+1)])
        sosedi = set()
        price_path = cenaPoti(path,mat)
        if price[kord] < price_path: #ce sm do tuki prsu na cenejši način skipi
            continue
        else:
            price[kord] = price_path

        if 0<= kord[0]+1<mat.shape[0]:
            sosedi.add((kord[0]+1,kord[1]))
        
        if 0<= kord[1]+1<mat.shape[0]:
            sosedi.add((kord[0],kord[1]+1))
        
        # if 0<= kord[0]-1<mat.shape[0]:
        #     sosedi.add((kord[0]-1,kord[1]))
        
        # if 0<= kord[1]-1<mat.shape[0]:
        #     sosedi.add((kord[0],kord[1]-1))
        
        
        if end in sosedi:
            sosedi = set()
            sosedi.add(end)
        
        for sos in sosedi:
            if sos not in path:
                #print(f"{sos} ni v {path}")
                
                p = path.copy()
                p.append(sos)
                paths.append(p)
                #path.pop()
        #print(paths)
    rezult = min([cenaPoti(kon,mat) for kon in koncne])
        

    print(f"vseh poti je {len(koncne)}")

    print(rezult)

def cenaPoti(path,mat):
    sum = 0
    for p in path:
        sum += mat[p]
    
    return sum
        



if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}") 