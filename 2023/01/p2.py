import time

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    sum = 0
    digits = {'one':'1', 'two': '2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', '0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5','6':'6','7':'7','8':'8','9':'9'}
    for line in lines:
        first = ''
        firstIndex = 100
        last = ''
        lastIndex = -1
        for key,item in digits.items():
            try:
              index = line.index(key)
              bindex = line.rindex(key)
            except ValueError:
                continue
            if index < firstIndex:
                first = item
                firstIndex = index
            if bindex > lastIndex:
                last = item
                lastIndex = bindex
        
        number = int(first + last)
        sum += number

    print(sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
