#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    s = -1000000
    
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    n = len(arr)
    
    for i in range(2,n):
        for j in range(2, n):
            tmp = 0
            tmp = arr[i][j] + arr[i][j-1] + arr[i][j-2] + arr[i-1][j-1] + arr[i-2][j] +\
                arr[i-2][j-1] + arr[i-2][j-2]
            
            if tmp > s:
                s = tmp
                
    print(s)