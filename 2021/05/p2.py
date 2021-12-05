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

    #print(f"X gre od {minX} do {maxX}")
    #print(f"Y gre od {minY} do {maxY}")
    mapa = np.zeros([maxY + 1,maxX + 1])
    
    for y0,y1,x0,x1 in poti:
        #print(f"Y: {y0} {y1}, X: {x0} {x1}")
        #print(f"Od: {y0} {x0}, X: {y1} {x1}")
        #mapa = np.zeros([maxY+1,maxX+1])

        if x0 == x1:
            if y0 > y1:
                y0,y1 = y1,y0
            
            np.add.at(mapa,(x0,(range(y0,y1 + 1))),1)
        
        elif y0 == y1:
            if x0 > x1:
                x0,x1 = x1,x0

            np.add.at(mapa,((range(x0,x1 + 1)),y0),1)

        else:
            stepX = -1 if (x0 > x1) else 1
            stepY = -1 if (y0 > y1) else 1    

            ranX = range(x0,x1 - 1,stepX) if stepX == -1 else range(x0,x1 + 1,stepX)

            ranY = range(y0,y1 - 1 ,stepY)if stepY == -1 else range(y0,y1 + 1,stepY)

            np.add.at(mapa,((ranX),(ranY)),1)

        #print(mapa)
    print((mapa > 1).sum()) #16793

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}") #Time is : 0.10615134239196777