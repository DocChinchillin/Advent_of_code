import time

class Rect():
    def __str__(self):
        return str(self.bottom_left["x"]) +" - "+str(self.top_right["x"])
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
    def shatter(self, oth):
        #more jih bit 8
        koti = [
            {"x":oth.bottom_left["x"], "y":oth.bottom_left["y"], "z":oth.bottom_left["z"]}, 
            {"x":oth.bottom_left["x"], "y":oth.top_right["y"], "z":oth.bottom_left["z"]}, 
            {"x":oth.top_right["x"], "y":oth.bottom_left["y"], "z":oth.bottom_left["z"]}, 
            {"x":oth.top_right["x"], "y":oth.top_right["y"], "z":oth.bottom_left["z"]} 


            #{"x":self.bottom_left["x"], "y":self.bottom_left["y"], "z":self.top_right["z"]}, 
            #{"x":self.bottom_left["x"], "y":self.top_right["y"], "z":self.top_right["z"]}, 
           # {"x":self.top_right["x"], "y":self.bottom_left["y"], "z":self.top_right["z"]}, 
           # {"x":self.top_right["x"], "y":self.top_right["y"], "z":self.top_right["z"]} 

        ]
        novi = []
        r1 = Rect(self.bottom_left["x"],koti[0]["x"] ,self.bottom_left["y"],koti[0]["y"],self.bottom_left["z"],koti[0]["z"]) # spodaj levo


        



    def contained(self, other): #ce je other ze popolnoma vsebovan v self
        return (self.bottom_left["x"] <= other.bottom_left["x"] and
        self.top_right["x"] >= other.top_right["x"] and

        self.bottom_left["y"] <= other.bottom_left["y"] and
        self.top_right["y"] >= other.top_right["y"] and

         self.bottom_left["z"] <= other.bottom_left["z"] and
         self.top_right["z"] >= other.top_right["z"]
        )

    def velikost(self):
        return ((self.top_right["x"] - self.bottom_left["x"] + 1) *
        (self.top_right["y"] - self.bottom_left["y"] + 1) *
        (self.top_right["z"] - self.bottom_left["z"] + 1))



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
        print(r,r.velikost())
        for oth in razponi:
            x=1
            #print(r.contained(oth)==r.intersects(oth))
            # if r.contained(oth):
            #     print("contained")
            #     print(r)
            #     print(oth)
            # else:
            #     print("ne contained")
            #     print(r)
            #     print(oth)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Time is : {end - start}') 