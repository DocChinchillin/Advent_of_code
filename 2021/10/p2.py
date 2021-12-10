import time
import numpy as np

def main():
    with open("input") as f:
        digits = np.array(f.read().splitlines())

    incompletes = []
    for string in digits:
        stack = []
        for char in string:
            if char in {"(","[","{","<"}: stack.append(char)
            else:
                opp = stack.pop()
                if char == ")":
                    if opp != "(":
                        stack.append(char)
                        break
                elif char == "]":
                    if opp != "[":
                        stack.append(char)
                        break
                elif char == "}":
                    if opp != "{":
                        stack.append(char)
                        break
                elif char == ">":
                    if opp != "<":
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
            add = getCloser(op)
            temp_score += add
        total.append(temp_score)

    print(np.median(total))

def getCloser(c):
    if c == "(": return 1
    if c == "[": return 2
    if c == "{": return 3
    if c == "<": return 4
        
def reduce(incompletes):
    ret = []
    for incomp in incompletes:
        manjsi = []
        
        for i,ch in enumerate(incomp):
            isti = 1
            if ch in {")","]",">","}"}:
                continue
            for j in range(i+1,len(incomp)):
                if incomp[j] == ch: isti+=1
                elif incomp[j] == getZaklep(ch): isti-=1
                if isti == 0: break
                    
            if isti > 0:
                manjsi.append(ch)
        ret.append(manjsi)

    return ret

def getZaklep(c):
    if c == "(": return ")"
    if c == "[": return "]"
    if c == "{": return "}"
    if c == "<": return ">"
        

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}") 