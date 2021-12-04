import time

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    nums = [int(line) for line in lines]

    count =  sum([nums[i - 1] < nums[i] for i in range(1,len(nums))])
    
    print(count)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")