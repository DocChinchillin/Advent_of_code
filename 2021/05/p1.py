import time
import numpy as np


def main():
    with open("test.txt") as f:
    	lines = f.read().splitlines()
    poti = np.zeros([len(lines),4])
    poti=poti.astype(int)
    
    for i,line in enumerate(lines):
        a,b = line.split(" -> ")
        ax,ay=a.split(",")
        bx,by=b.split(",")
        poti[i] = [ax,bx,ay,by]
    
    minX = np.min(poti[:,0:2])
    maxX = np.max(poti[:,0:2])

    minY = np.min(poti[:,2:4])
    maxY = np.max(poti[:,2:4])

    #print(f"X gre od {minX} do {maxX}")
    #print(f"Y gre od {minY} do {maxY}")
    mapa = np.zeros([maxX+1,maxY+1])
    
    for pot in poti:
        x0,x1,y0,y1 = pot
        print(f"{x0} {x1} , {y0} {y1}")
        if x0 == x1:
            np.add.at(mapa,(x0,(y0,y1)),1)
        if y0 == y1:
            np.add.at(mapa,((x0,x1),y0),1)
        print(mapa)
    
    
    #print((mapa==1).sum())

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")