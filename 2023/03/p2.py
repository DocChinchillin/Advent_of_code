import time
import numpy as np

def checkArea(mat: np.array,oind,ind,startN):
    maxY,maxX = np.shape(mat)
    y0 = max(0,oind - 1)
    y1 = min(maxY,oind + 2)
    x0 = max(0,startN-1)
    x1 = min(maxX, ind+1)
    
    digits = np.char.isdigit(mat[y0:y1,x0:x1])
    digits = digits == False
    dots = np.char.find(mat[y0:y1,x0:x1],b'.') != 0
    both = np.logical_and(digits,dots)
    print(mat[y0:y1,x0:x1])
    print(digits)
    # print()
    # print(dots)
    # print()
    # print(both)
    # print()
    return np.any(both)
    

def main():
    with open("input.txt") as f:
        digits = np.array(f.read().splitlines())

    sizey = digits.shape[0]
    sizex = len(digits[0])
    mat = np.zeros((sizey,sizex),dtype='S1')

    for i,string in enumerate(digits):
        mat[i] = [char for char in string]

    sum = 0

    for oind,line in enumerate(mat):
        number = ''
        for ind,c in enumerate(line):
            if c.isdigit():
                number += c.decode('UTF-8')
            elif number != '':
                startN = ind - len(number)
                if checkArea(mat,oind,ind,startN):
                    sum += int(number)
                    print(int(number))
                number = ''
        if number != '':
                startN = ind - len(number)
                if checkArea(mat,oind,ind,startN):
                    sum += int(number)
                    print(int(number))
                number = ''

        

    print(sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
