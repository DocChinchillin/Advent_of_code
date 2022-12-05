import time


def main():

    with open('input') as f:
        lines = f.read().splitlines()

    movements,boxs = lines[lines.index("")+1:],lines[:lines.index("")]

    boxs.reverse()
    col = [ [] for a in boxs[0].replace(" ","")]
    

    for row in boxs[1:]:
        parts = [row[i:i+3] for i in range(0, len(row), 4)]
        for n,box in enumerate(parts):
            b = box.replace("[","").replace("]","")
            if not b.isspace():
                col[n].append(b)

    
    for move in movements:    
        _,num,_,l1,_,l2  = move.split(" ")
        for n in range(int(num)):
            col[int(l2)-1].append(col[int(l1)-1].pop())

    print("".join([c[len(c)-1] for c in col]))
        


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")