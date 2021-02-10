#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    result = [0]*(n+1)
    
    for a, b, k in queries:
        result[a-1] += k
        result[b] -= k

    maxVal = 0
    count = 0
    print(result)
    for i in result:
        count += i
        if count > maxVal:
            maxVal = count
            
    return maxVal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
