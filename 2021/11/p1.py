import time
import numpy as np

def main():
    with open("input") as f:
        digits = np.array(f.read().splitlines())

    sizey = digits.shape[0]
    sizex = len(digits[0])
    mat = np.zeros((sizey,sizex),dtype=np.int8)

    for i,string in enumerate(digits):
        mat[i] = [char for char in string]
        
    flash = 0
    
    for i in range(100):

        mat = mat + 1
        cooldown = set()
        blink = np.transpose((mat>9).nonzero()).tolist()

        while blink:
            
            kord = blink.pop()

            if tuple(kord) in cooldown:
                continue

            flash +=1
            cooldown.add(tuple(kord))
            sosedi = set([(i,j) for i in range(kord[0]-1,kord[0]+2)for j in range(kord[1]-1,kord[1]+2)])
            sosedi.remove((kord[0],kord[1]))

            for k in sosedi.copy():
                    if k[0] < 0 or k[1] < 0 or k[0] >= sizex or k[1] >= sizey:
                        sosedi.remove((k))

            for sos in sosedi:
                mat[sos] += 1
                if mat[sos] > 9 and tuple(sos) not in cooldown:
                    blink.append(sos)
            
        for col in cooldown:
            mat[col] = 0

    print(flash)
            
            


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}") 