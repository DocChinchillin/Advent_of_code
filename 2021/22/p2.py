import time
import numpy as np

class Rect():
    def __str__(self):
        return str(self.top_right) +" "+str(self.bottom_left)
    def __init__(self,x1,x2,y1,y2,z1,z2):
        self.bottom_left = {"x":x1,"y":y1,"z":z1}
        self.top_right = {"x":x2,"y":y2,"z":z2}
    
    def intersects(self, other):
        return not (self.top_right["x"] < other.bottom_left["x"] or
        self.bottom_left["x"] > other.top_right["x"] or

        self.top_right["y"] < other.bottom_left["y"] or
        self.bottom_left["y"] > other.top_right["y"] or

         self.top_right["z"] < other.bottom_left["z"] or
         self.bottom_left["z"] > other.top_right["z"]
        )



def main():
    with open('t1') as f:
        lines = f.read().splitlines()

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
    
        commands.append(command)
        razponi.append(Rect(int(x1),int(x2),int(y1),int(y2),int(z1),int(z2)))
    
    for r in razponi:
        for oth in razponi:
            if r.intersects(oth):
                print("sekata")
                print(r)
                print(oth)
            else:
                print("ne sekata")
                print(r)
                print(oth)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Time is : {end - start}') 