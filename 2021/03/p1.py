import time

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    
    stevila = [line for line in lines]
    
    stevka_len = len(stevila)
    num_bits = len([char for char in stevila[0]])

    vsota = [0] * num_bits

    for st in stevila:
        for i,stevka in  enumerate(st):
           vsota[i] += int(stevka)

    result_ena = ""
    result_nic = ""
    for st in vsota:
        if(st > stevka_len/2):
            result_ena += "1"
            result_nic += "0"
        else:
            result_ena += "0"
            result_nic += "1"
    
    gamma = int(result_ena,2)
    epsi = int(result_nic,2)

    print(gamma * epsi) # 741950

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")