import time
import numpy as np

def main():
    with open("input.txt") as f:
    	lines = f.read().splitlines()

    poti = (np.zeros([len(lines),4])).astype(int)
    
    for i,line in enumerate(lines):
        a,b = line.split(" -> ")
        ax,ay = a.split(",")
        bx,by = b.split(",")
        poti[i] = [ax,bx,ay,by]
    
    maxX = np.max(poti[:,0:2])
    maxY = np.max(poti[:,2:4])
    mapa = np.zeros([maxY+1, maxX+1])
    
    for y0,y1,x0,x1 in poti:
        if x0 == x1:
            if y0 > y1:
                y0,y1 = y1,y0
            np.add.at(mapa,(x0,(range(y0,y1 + 1))),1)

        elif y0 == y1:
            if x0 > x1:
                x0,x1 = x1,x0
            np.add.at(mapa,((range(x0,x1 + 1)),y0),1)

       #print(mapa)
    
    print((mapa > 1).sum()) #4826

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}") #Time is : 0.06264328956604004