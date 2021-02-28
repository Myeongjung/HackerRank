#!/bin/python3

import math
import os
import random
import re

# Complete the riddle function below.
def riddle(arr):
    n = len(arr)
    stack = []
    left = [-1 for _ in range(n)]
    right = [n for _ in range(n)]
    result = [0 for _ in range(n+1)]

    for i in range(n):
        while len(stack) and arr[stack[len(stack)-1]] >= arr[i]:
            stack.pop()

        if len(stack):
            left[i] = stack[len(stack)-1]

        stack.append(i)

    while len(stack):
        stack.pop()

    for i in range(n-1, -1, -1):
        while len(stack) and arr[stack[len(stack)-1]] >= arr[i]:
            stack.pop()

        if len(stack):
            right[i] = stack[len(stack)-1]

        stack.append(i)

    for i in range(n):
        length = right[i] - left[i] - 1;

        result[length] = max(result[length], arr[i])
    
    for i in range(n-1, 0, -1):
        result[i] = max(result[i], result[i + 1])

    return result[1:]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
