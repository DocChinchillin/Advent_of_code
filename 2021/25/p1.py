import time
import numpy as np
from numpy.core.numeric import count_nonzero

def main():
    with open('input') as f:
       lines = np.array(f.read().splitlines())

    sizey = lines.shape[0]
    sizex = len(lines[0])
    mat = np.empty((sizey,sizex),dtype=object)
    for i,string in enumerate(lines):
        mat[i] = list(string)

    moved = 1
    steps = 0
    while moved:
        steps +=1
        moved = 0

        can_move = find_moves(sizey, sizex, mat,'>')
        kord = np.where(can_move==1)
        move(sizey,sizex, mat, kord,'>')
        moved = count_nonzero(kord)

        can_move = find_moves(sizey, sizex, mat,'v')
        kord = np.where(can_move==1)
        move(sizey,sizex, mat, kord,'v')
        moved += count_nonzero(kord)


    print(steps)

def move(sizey,sizex, mat, kord,smer):
    lokacije = zip(kord[0],kord[1])
    for a,b in lokacije:
        if smer == 'v':
            if a + 1 < sizey:
                mat[a+1][b] = 'v'
            else:
                mat[0][b] = 'v'
        else:
            if b + 1 < sizex:
                mat[a][b+1] = '>'
            else:
                mat[a][0] = '>'
        mat[a][b] = '.'

def find_moves(sizey, sizex, mat,smer):
    can_move = np.zeros_like(mat)
    for i in range(sizey):
        for j in range(sizex):
            if mat[i][j] == smer:
                if smer == ">":
                    if j + 1 < sizex:
                        if mat[i][j+1] == '.':
                            can_move[i][j] = 1
                    elif mat[i][0] == '.':
                        can_move[i][j] = 1

                elif i + 1 < sizey:
                    if mat[i+1][j] == '.':
                        can_move[i][j] = 1
                elif mat[0][j] == '.':
                    can_move[i][j] = 1
    return can_move
        



if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Time is : {end - start}') 