#!/bin/python3

import math
import os
import random
import re
import sys


def minimumMoves(grid, startX, startY, goalX, goalY):
    moves = ((1,0),(-1,0), (0,1), (0,-1))
    visit = {(startX, startY)}
    q = [[startX, startY, 0]]
    while len(q)>0:
        path, q = q[0], q[1:]
        row, col, val = path
        for move in moves:
            nrow, ncol = row, col
            while True:
                nrow, ncol = nrow+move[0], ncol+move[1]
                if nrow>=0 and ncol>=0 and nrow<len(grid) and ncol<len(grid) and grid[nrow][ncol]== '.':
                    print(nrow, ncol)
                    if (nrow, ncol) == (goalX, goalY):
                        return val+1
                    else:
                        if (nrow, ncol) not in visit:
                            visit.add((nrow, ncol))
                            q += [[nrow, ncol, val+1]]
                else:
                    break
    return -1
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
