import time
import numpy as np

def main():
    with open("input") as f:
        digits = np.array(f.read().splitlines())

    points = {"(": 1, "[":  2,"{": 3, "<": 4}
    oklepaji ={ "(": ")", "[": "]","{": "}", "<": ">"}

    incompletes = []
    for string in digits:
        stack = []
        for char in string:
            if char in {"(","[","{","<"}: stack.append(char)
            else:
                opp = stack.pop()
                if oklepaji[opp] != char:
                    stack.append(char)
                    break
        if stack[-1] not in {")","]","}",">"}:
            incompletes.append(string)
    
    smaller = reduce(incompletes)

    total = []
    for inc in smaller:
        temp_score = 0
        for op in reversed(inc):
            temp_score *= 5
            temp_score += points[op]
        total.append(temp_score)

    print(np.median(total))
        
def reduce(incompletes):
    ret = []
    oklepaji ={ "(": ")", "[": "]","{": "}", "<": ">"}
    for incomp in incompletes:
        manjsi = []
        
        for i,ch in enumerate(incomp):
            isti = 1
            if ch in {")","]",">","}"}:
                continue
            for j in range(i+1,len(incomp)):
                if incomp[j] == ch: isti+=1
                elif incomp[j] == oklepaji[ch]: isti-=1
                if isti == 0: break
                    
            if isti > 0:
                manjsi.append(ch)
        ret.append(manjsi)

    return ret        

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}") 