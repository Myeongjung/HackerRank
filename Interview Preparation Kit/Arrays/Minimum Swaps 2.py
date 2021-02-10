#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    ref_arr = sorted(arr)
    d = {v: i for i,v in enumerate(arr)}
    total = 0
    
    for i,v in enumerate(arr):
        value = ref_arr[i]
        if v != value:
            idx = d[value]
            arr[idx],arr[i] = arr[i], arr[idx]
            d[v] = idx
            d[value] = i
            total += 1
            
    return total
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
