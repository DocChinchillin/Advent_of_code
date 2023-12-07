import time


def main():
    with open('input.txt') as f:
        lines = f.read().split('\n')

    times = lines[0].split()
    times.pop(0)
    dists = lines[1].split()
    dists.pop(0)
    sum = 1
    for t,d in zip(times,dists):
        #print(t,d)
        t = int(t)
        d = int(d)
        cnt = 0
        for speed in range(0,int(t)+1):
            left = t-speed
            dist = left*speed
            if dist > d:
                cnt +=1
                #print(speed)
        sum *= cnt
    
    print(sum)
        

    


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
