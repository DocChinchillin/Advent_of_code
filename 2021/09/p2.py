import time
import numpy as np

def main():
    with open("input") as f:
        digits = np.array(f.read().splitlines())

    sizey = digits.shape[0]
    sizex = len(digits[0])
    mat = np.zeros((sizey,sizex))

    for i,string in enumerate(digits):
        mat[i] = [char for char in string]
    
    low = set()
    for i in range(sizey):
        for j in range(sizex):
            low.add(four_neigh(i,j,mat,sizey-1,sizex-1))
            
    low.remove(0)

    
    sizes = []

    for x,y in low:
        bas = set([(x,y), (x-1,y), (x+1,y), (x,y-1), (x,y+1) ])
        sizes.append(len(rek(bas,sizey-1,sizex-1,mat)))

    print(np.prod(sorted(sizes, reverse=True)[:3]))
        

def four_neigh(i,j,mat,imax,jmax):
    sred = mat[i,j]

    if(i-1 >= 0 and mat[i-1,j] <= sred) or (i+1 <= imax and mat[i+1,j] <= sred) or (j-1 >= 0 and mat[i,j-1] <= sred) or (j+1 <= jmax  and mat[i,j+1] <= sred):
        return 0
    return (i,j)

def rek(basin, imax, jmax, mat):
    pravi = set()
    looked = set()

    while(basin):
        x,y = basin.pop()
        looked.add((x,y))

        if (x < 0 or y < 0 or imax < x or jmax < y):
            continue
        
        if mat[x,y] != 9:
            pravi.add((x,y))
        else:
            continue
        
        if x-1 >=0 and mat[x-1,y] !=9 and (x-1,y) not in looked:
            basin.add((x-1,y))

        if y-1 >=0 and mat[x,y-1] !=9 and (x,y-1) not in looked:
            basin.add((x,y-1))

        if imax >= x+1 and mat[x+1,y] !=9 and (x+1,y) not in looked:
            basin.add((x+1,y))

        if jmax >= y+1 and mat[x,y+1] !=9 and (x,y+1) not in looked:
            basin.add((x,y+1))
        
    return pravi
    
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}") 