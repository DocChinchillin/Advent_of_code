def reduction(stevila,con):
    vsota = 0
    stevka_len = len(stevila)
    i = 0

    while len(stevila) > 1:
        vsota = 0
        temp = []

        vsota = sum([int(st[i]) for st in stevila])

        for st in stevila:
            if(con and (vsota >= stevka_len/2) == int(st[i])):
                temp += [st]
            
            if(not con and (vsota < stevka_len/2) == int(st[i])):
                temp += [st]
       
        stevila = temp
        stevka_len = len(stevila)
        i += 1

    return int(stevila[0],2)

def main():

    with open('input.txt') as f:
        lines = f.read().splitlines()
    
    st_ox = [line for line in lines]
    st_co = st_ox.copy()

    ox = reduction(st_ox,True)
    co = reduction(st_co,False)

    print(ox * co )  #903810

if __name__ == "__main__":
    main()