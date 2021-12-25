import time

class Rect():
    def __str__(self):
        return "x: ("+str(self.bottom_left["x"]) +" - "+str(self.top_right["x"]) +") "+"y: ("+str(self.bottom_left["y"]) +" - "+str(self.top_right["y"]) +") z: ("+str(self.bottom_left["z"]) +" - "+str(self.top_right["z"])+")"
    
    def __init__(self,x1,x2,y1,y2,z1,z2,command):
        self.bottom_left = {"x":x1,"y":y1,"z":z1}
        self.top_right = {"x":x2,"y":y2,"z":z2}
        self.type = command
    
    def intersects(self, other):
        return not (self.top_right["x"] < other.bottom_left["x"] or
        self.bottom_left["x"] > other.top_right["x"] or

        self.top_right["y"] < other.bottom_left["y"] or
        self.bottom_left["y"] > other.top_right["y"] or

         self.top_right["z"] < other.bottom_left["z"] or
         self.bottom_left["z"] > other.top_right["z"]
        )

    def inter(self,oth):
        x0 = min(self.top_right["x"], oth.top_right["x"]) 
        x1 = max(self.bottom_left["x"], oth.bottom_left["x"]) 
        y0 = min(self.top_right["y"], oth.top_right["y"]) 
        y1= max(self.bottom_left["y"], oth.bottom_left["y"]) 
        z0 = min(self.top_right["z"], oth.top_right["z"]) 
        z1= max(self.bottom_left["z"], oth.bottom_left["z"]) 
        if(x1>x0 or y1>y0 or z1>z0):
            return None
        return Rect(x1,x0,y1,y0,z1,z0,1-self.type)

    def velikost(self):
        return ((self.top_right["x"] - self.bottom_left["x"] + 1) *
        (self.top_right["y"] - self.bottom_left["y"] + 1) *
        (self.top_right["z"] - self.bottom_left["z"] + 1))



def main():
    with open('input') as f:
        lines = f.read().splitlines()

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
        c = 1 if command == "on" else 0
        razponi.append(Rect(int(x1),int(x2),int(y1),int(y2),int(z1),int(z2),c))

    koncni = []

    for kvadr in razponi:
        preseki = [k.inter(kvadr) for k in koncni if k.intersects(kvadr)]

        koncni += preseki
        if kvadr.type == 1:
            koncni.append(kvadr)

    vsota = sum(k.velikost() if k.type else -k.velikost() for k in koncni)

    print(vsota)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Time is : {end - start}') 