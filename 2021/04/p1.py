import numpy as np
import time

def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    
    bingos = lines[0].split(",")

    boards = []
    
    temp = []
    lines[0] = ""
    for line in lines:
        if line == "":
            if(len(temp)!=0):
                boards.append(temp)
                temp = []
        else:
            temp.append(line.split()) 
    
    boards=np.array([np.array(xi) for xi in boards])
    
    for bingo_num in bingos:
        temp = np.empty_like(boards)

        for i,bord in enumerate(boards):
            temp[i]=np.where(bord == bingo_num, "-1", bord)

        boards = temp
        win = checkWin(boards)

        if(win):
            break

    print(win * int(bingo_num))

def checkWin(boards):
    for i in range(0,len(boards)):
        for j in range(0,len(boards[i])):
            if np.count_nonzero(boards[i][:,j] == "-1") == len(boards[i]) or np.count_nonzero(boards[i][j,:] == "-1") == len(boards[i]):
                return calcWin(boards[i])
                
    return 0
            
def calcWin(board):
    board = np.where(board == "-1", "0", board)
    board = board.astype(int)
    vsota = sum(sum(board))

    return vsota

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")