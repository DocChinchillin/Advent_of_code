import time

vrednost = {i:i for i in range(1,10)}
vrednost[0] = 10
rolls = { 3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1 }

def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return memoized_func


def main():
    

    p1_index = 10
    p2_index = 1

    p1_score = 0
    p2_score = 0

    sum1, sum2 = 0,0
    for v in range(3,10):
        a,b = mrek(v,p1_score,p2_score,p1_index,p2_index,1)
        sum1 += a * rolls[v]
        sum2 += b * rolls[v]

    print(f"{max(sum1,sum2)}")
     
def rek(cifra,p1_score,p2_score,p1_index,p2_index,turn):
  
    if turn == 1:
        p1_index += cifra
        p1_index = p1_index % 10
        p1_score += vrednost[p1_index]
    else:
        p2_index += cifra
        p2_index = p2_index % 10
        p2_score += vrednost[p2_index]
    
    if p1_score >= 21:
        return 1,0

    if p2_score >= 21:
        return 0,1

    sum1, sum2 = 0,0
    for v in range(3,10):
        a,b = mrek(v,p1_score,p2_score,p1_index,p2_index,-turn)
        sum1 += a * rolls[v]
        sum2 += b * rolls[v]

    return sum1,sum2
    
if __name__ == '__main__':
    start = time.time()
    mrek = memoize(rek)
    main()
    end = time.time()
    print(f'Time is : {end - start}') 