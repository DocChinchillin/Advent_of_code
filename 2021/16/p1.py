import time
import numpy as np

def main():
    with open('input') as f:
        lines = f.read().splitlines()
    data = [bin(int(c, 16))[2:].zfill(4) for c in lines[0]]
    all = list("".join(data))
    
    v,l = subVersion(all)
    print(v)



def subVersion(sub):
    if len(sub)<11:
        return 0,len(sub)

    V = int("".join(sub[:3]),2)
    T = int("".join(sub[3:6]),2)
    
    total_ver = V
    if T==4:
        not_last = 1
        start_ind = 6
        total_val = []
        while not_last == 1:
            not_last = int(sub[start_ind])
            total_val.append("".join(sub[start_ind+1:start_ind+5]))
            start_ind +=5
        return V , start_ind
        
    else:
        
        I =  int(sub[6],2)
        
        if not I:
            start_i = 22 
            L =  int("".join(sub[7:7+15]),2)
            l = 22 + L
            while start_i < l:
                ver,leng = subVersion(sub[start_i:])
                total_ver += ver
                start_i += leng
            
        else:
            L =  int("".join(sub[7:7+11]),2)
            start_i = 18
            i = 0
            while i < L:
                ver,leng = subVersion(sub[start_i:]) 
                total_ver += ver
                start_i +=leng
                i+=1

    return total_ver,start_i



if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Time is : {end - start}') 