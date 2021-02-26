#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    s = 0
    for c in n:
        s += int(c)
    s *= k
    return(findSuper(str(s)))
    
def findSuper(n):
    result = 0
    if len(n) == 1:
        return n
    else:
        for c in n:
            result += int(c)
        return findSuper(str(result))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
