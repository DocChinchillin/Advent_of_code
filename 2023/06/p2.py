import time


def main():
    with open('input.txt') as f:
        lines = f.read().split('\n')

    times = lines[0].split(':')
    dists = lines[1].split(':')

    times = times[1].replace(' ','')
    dists = dists[1].replace(' ','')
    
    sum = 1
    t = int(times)
    d = int(dists)
    cnt = 0
    for speed in range(0,int(t)+1):
        left = t-speed
        dist = left*speed
        if dist > d:
            cnt +=1
    sum *= cnt
    
    print(sum)
        

    


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
