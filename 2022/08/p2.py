import time
import numpy as np

def main():

    with open('/home/doc/Desktop/Advent_of_code/2022/08/input') as f:
        lines = f.read().splitlines()
    


    forest = np.array([np.array([c for c in line]) for line in lines])
    max = 0
    for x in range(forest.shape[0]):
        for y in range(forest.shape[1]):
            a = forest[0:x,y] < forest[x,y]
            b = forest[x,0:y] < forest[x,y]
            c = forest[x+1:,y] < forest[x,y]
            d = forest[x,y+1:] < forest[x,y]

            s1, s2 , s3, s4 = 0,0,0,0

            indices = np.argwhere(a == False)
            if indices.size > 0:
                index = indices[-1]
                s1 = x - index[0] 
            elif a.size > 0:
                s1 = a.size
            
            indices = np.argwhere(b == False)
            if indices.size > 0:
                index = indices[-1]
                s2 = y - index[0] 
            elif b.size > 0:
                s2 = b.size

            indices = np.argwhere(c == False)
            if indices.size > 0:
                index = indices[0]
                s3 = index[0] + 1
            elif c.size > 0:
                s3 = c.size
            
            indices = np.argwhere(d == False)
            if indices.size > 0:
                index = indices[0]
                s4 = index[0] + 1
            elif d.size > 0:
                s4 = d.size
            
            newMax = s1 * s2 * s3 * s4
            if newMax > max:
                max = newMax
            

    
    print( max)



        



if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")