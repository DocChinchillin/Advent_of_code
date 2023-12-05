import time

class Converter:
    
    def __init__(self, name):
        self.name = name
        self.ranges = []

    def convert(self, num):
        mini = float("inf")
        for r in self.ranges:
            if r.isIn(num):
                newMin = r.convert(num)
                mini = min(newMin,mini)
        
        if mini == float("inf"):
            return num
        
        return mini
    def __str__(self):
        return f"{self.ranges}"



class Range:
    def __init__(self, dest, source, length):
        self.dest = int(dest)
        self.source = int(source)
        self.length = int(length)
    
    def __str__(self):
        return f"{self.dest} {self.source} {self.length}"
    
    def isIn(self, num):
        return self.source <= num < self.source + self.length

    def convert(self,num):
        place = num - self.source
        if place > self.length:
            raise Exception()
        return self.dest + place 

def main():
    with open('input.txt') as f:
        lines = f.read().split('\n')
    seeds = lines[0].split(':')[1].split()

    lines.pop(0)
    lines.pop(0)
    mapp = []
    mappers = []
    for l in lines:
        if l == '':
            mapper = Converter(mapp[0])
            mapp.pop(0)
            for m in mapp:
                dest,source,length = m.split()
                mapper.ranges.append(Range(dest,source,length))
            mapp = []
            mappers.append(mapper)
            continue
        mapp.append(l)

    # for map in mappers:
    #     print(map.name)
    #     for r in map.ranges:
    #         print(r)

    globalMin = float("inf")
    for seed in seeds:
        seed = int(seed)
        for con in mappers:
            seed = con.convert(seed)
        
        globalMin = min(seed,globalMin)
    

    print(globalMin)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
