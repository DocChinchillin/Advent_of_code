import time
import numpy as np

def lowPoint(i,j,mat,imax,jmax):
    sred = mat[i,j]

    if((i - 1 >= 0 and mat[i - 1,j] <= sred) or
    (i + 1 <= imax and mat[i + 1,j] <= sred) or
    (j - 1 >= 0 and mat[i,j - 1] <= sred)    or 
    (j + 1 <= jmax  and mat[i,j + 1] <= sred)):
        return 0
    return sred + 1

def main():
    with open("input") as f:
        digits = np.array(f.read().splitlines())

    sizey = digits.shape[0]
    sizex = len(digits[0])
    mat = np.zeros((sizey,sizex))

    for i,string in enumerate(digits):
        mat[i] = [char for char in string]
    
    sum = 0
    for i in range(sizey):
        for j in range(sizex):
            sum += lowPoint(i,j,mat,sizey - 1,sizex - 1)
    
    print(sum)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}") 