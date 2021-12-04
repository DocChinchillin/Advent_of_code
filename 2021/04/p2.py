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
    
    boards = np.array([np.array(xi) for xi in boards])
    
    end = 0

    for bingo_num in bingos:
        temp = np.empty_like(boards)

        for i,bord in enumerate(boards):
            temp[i] = np.where(bord == bingo_num, "-1", bord)

        boards = temp
        
        if(len(boards) == 1):
            for i in range(0,len(boards[0])):
                if np.count_nonzero(boards[0][:,i] == "-1") == len(boards[0]) or np.count_nonzero(boards[0][i,:] == "-1") == len(boards[0]):
                    end = 1
                    break
            if end:
                break
        boards = checkWin(boards)

    win = calcWin(boards[0])

    print(int(bingo_num) * win)

    

def checkWin(boards):
    temp = []
    
    for i in range(0,len(boards)):
        for j in range(0,len(boards[i])):
            if np.count_nonzero(boards[i][:,j] == "-1") == len(boards[i]) or np.count_nonzero(boards[i][j,:] == "-1") == len(boards[i]):
                temp.append(i)

    return np.delete(boards,temp,0)
            
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