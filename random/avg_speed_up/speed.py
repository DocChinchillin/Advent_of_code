def main():

    st = int(input("Start index: "))
    end = int(input("End index: "))
    print()
    for i in range(st,end+1):
        gpu = avg("./inputs/sGPU_",i,".out")
        cpu = avg("./inputs/sCPU_",i,".out")

        print(f"Primer {i}")
        print(f"CPU time: {cpu}")
        print(f"GPU time: {gpu}")
        print(f"Pohitritev: {cpu/gpu}\n")
        
    

def avg(name,i,postfix):
    with open(f"{name}{i}{postfix}") as f:
    	times = f.read().splitlines()

    times = list(filter(bool,times))

    return sum([float(time) for time in times]) / len(times)
    

if __name__ == "__main__":
    main()