#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    s = [0]*n
    c = [0]*n
    for i in range(n):
            if i == 0 or s[i-1] == 1:
                s[i] = numDesending(arr, i)
            else:
                s[i] = s[i-1] - 1
            c[i] = s[i] if arr[i] <= arr[i-1] else max(s[i], c[i-1]+1)
    return sum(c)

def numDesending(arr, i):
    ret = 1
    while i + 1 < len(arr):
            if arr[i] > arr[i+1]:
                    ret += 1
                    i += 1
            else:
                    return ret
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
