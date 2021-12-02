def main():
    with open('input.txt') as f:
        lines = f.readlines()

    nums = [int(line.replace("\n","")) for line in lines]

    count =  len([i for i in range(1,len(nums)) if nums[i-1]<nums[i]])
    
    print(count)

if __name__ == "__main__":
    main()