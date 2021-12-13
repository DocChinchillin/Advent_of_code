import time
import numpy as np

def main():
    with open("input") as f:
        lines = f.read().splitlines()
   
    sp = lines.index("")
    dots = lines[:sp]
    folds = lines[sp+1:]

    temp = []
    for fold in folds:
        temp.append(fold.strip("fold along "))

    folds = temp

    y = None
    x = None
    i = 0
    while y == None or x == None:
        smer,index = folds[i].split("=")
        if smer == "y":
            y = int(index)*2+1
        if smer == "x":
            x = int(index)*2+1
        i+=1

    mat = np.zeros((y,x))
    for dot in dots:
        kord = tuple(dot.split(","))
        mat[int(kord[1]),int(kord[0])] = 1

    smer,index = folds[0].split("=")
    index = int(index)

    if smer == "y":
        mat = np.delete(mat,index,0) #y
        print() 
        ar1,ar2 = np.vsplit(mat,2)
        mat = ar1 + np.flip(ar2,0)
    
    if smer == "x":
        mat = np.delete(mat,index,1) 
        ar1,ar2 = np.hsplit(mat,2)
        mat = ar1 + np.flip(ar2,1)

    print(np.count_nonzero(mat))

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}") 