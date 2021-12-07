import time
import numpy as np

def main():
    with open("input") as f:
        crabs = np.array(f.read().splitlines()[0].split(","),dtype = "int32")

    inital_i, initial_count = np.unique(crabs, return_counts = True)

    size = max(inital_i) + 1

    range_ar = np.arange(0,stop=size)   #array za račun cene [0,1,2,3,4...]

    move_cost = []
    
    avg = int(np.average(crabs))    

    for i in range(avg-1,avg+2):
        delni = abs(inital_i - i)       #tabela dolzin premikov iz pozicije crab-a na trenutni index

        for j in range(0,len(delni)):
            #delni[j] = sum(range(0,delni[j]+1))   
            delni[j] = np.sum(range_ar[0:delni[j]+1])     #izračun naraščojoče cene premika
        move_cost.append(sum(delni * initial_count))  #vsota cene (goriva) za premik na trenutni index

    print(min(move_cost))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")