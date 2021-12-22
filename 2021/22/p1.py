import time
import numpy as np

def main():
    with open('input') as f:
        lines = np.array(f.read().splitlines())

    commands = []
    razponi = []
    for line in lines:
        command, razpon = line.split(" ")
        
        x,y,z =razpon.split(",")
        x = x.removeprefix("x=")
        y = y.removeprefix("y=")
        z = z.removeprefix("z=")
        x1,x2 = x.split("..")
        y1,y2 = y.split("..")
        z1,z2 = z.split("..")

        

        xtup = (int(x1) + 50,int(x2) + 50)
        ytup = (int(y1) + 50,int(y2) + 50)
        ztup = (int(z1) + 50,int(z2) + 50)

        skip = 0

        for a,b in (xtup,ytup,ztup):
            if a > 100 or b > 100 or a < 0 or b < 0:
                skip=1
        if skip == 1:
            continue
        
        commands.append(command)
        razponi.append((xtup,ytup,ztup))
    
    prostor = np.zeros((101,101,101))
    #print(commands)
    for com,raz in zip(commands,razponi):
        #print(f"{com} | {raz}")
        rx,ry,rz = raz
        if com =="on":
            prostor[rx[0]:rx[1]+1,ry[0]:ry[1]+1,rz[0]:rz[1]+1] = 1
        if com =="off":
            prostor[rx[0]:rx[1]+1,ry[0]:ry[1]+1,rz[0]:rz[1]+1] = 0

    
    print(np.count_nonzero(prostor))

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Time is : {end - start}') 