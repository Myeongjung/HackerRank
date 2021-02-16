#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    if len(arr) == 1:
        return 0
    
    n = len(arr)//2
    m = len(arr) - n
    left = arr[:n]
    right = arr[n:]
    count = countInversions(left) + countInversions(right)
    j, k = 0, 0
    for i in range(len(arr)):
        if j <n and (k>=m or left[j]<=right[k]):
            arr[i] = left[j]
            count += k
            j += 1 
        elif k < m:
            arr[i] = right[k]
            k += 1
    return count    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
