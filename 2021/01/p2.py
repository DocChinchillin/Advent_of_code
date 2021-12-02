def main():
    with open('input.txt') as f:
        lines = f.readlines()

    nums = [int(line.replace("\n","")) for line in lines]

    sums =  [nums[i-2]+nums[i-1]+nums[i] for i in range(2,len(nums))]

    count =  len([i for i in range(1,len(sums)) if sums[i-1]<sums[i]])
    
    print(count)


if __name__ == "__main__":
    main()