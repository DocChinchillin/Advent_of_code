import time
import string


def main():
    priority = {c:n+1 for n,c in enumerate(string.ascii_letters)} 

    with open('input') as f:
        lines = f.read().splitlines()

    groups = [lines[i:i + 3] for i in range(0, len(lines), 3)]


    sum = 0
    for bp1,bp2,bp3 in groups:
        
        for char in bp1:
            if char in bp2 and char in bp3:
                sum += priority[char]
                break

    
    
    print(sum)



if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")