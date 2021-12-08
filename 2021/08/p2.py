import time
import numpy as np

def main():
    with open("input") as f:
        digits = np.array(f.read().splitlines())

    sum = 0
    for digit in digits:
        input,output = digit.split(" | ")
        
        inputs = input.split(" ")
        outputs = output.split(" ")

        five = []
        six = []

        for out in inputs+outputs:
            if len(out) == 2:
                one = set(out) 

            if len(out) == 3:
               seven = set(out)

            if len(out) == 4:
                four = set(out)
            
            if len(out) == 5:
                if set(out) not in five:
                    five.append(set(out))

            if len(out) == 6:
                if set(out) not in six:
                    six.append(set(out))

            if len(out) == 7:
                all = set(out) #all = osem

        top = seven - one 
        bottom = all - (four.union(top))
        
        for s in six:
            bottom = bottom.intersection(s)
            if len(s.intersection(one))==1:
                bot_right = s.intersection(one)
                

        top_right = one - bot_right
        bot_left = all - four.union(top) - bottom

        sredina = all - bottom - seven - bot_left  #delna sredina, imamo dve crki sredino in top left
        for f in five:
            sredina = sredina.intersection(f)       #locimo med sredino in top left
        
        top_left = all - bottom - seven  - bot_left  - sredina
        
        #print(f"{top} {top_left} {top_right} {sredina} {bot_left} {bot_right} {bottom}")

        #print(f"0: {all - sredina}") #0
        #print(one)
        #print(all - top_left - bot_right)
        
        #print(f"6: {all - top_right}") #6

        #print(f"9: {all - bot_left}") #9

        stevke = {
            frozenset(all - sredina) : "0",
            frozenset(one) : "1",
            frozenset(all - top_left - bot_right) : "2",
            frozenset(all - top_left - bot_left) : "3",
            frozenset(four) : "4",
            frozenset(all - top_right - bot_left) : "5",
            frozenset(all - top_right) : "6",
            frozenset(seven) : "7",
            frozenset(all) : "8",
            frozenset(all - bot_left) : "9"
        }
        stevilka = []

        for o in outputs:
            stevilka.append(stevke[frozenset(o)])
            
        sum += int("".join(stevilka))
        
    print(sum) #1004688


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}") 