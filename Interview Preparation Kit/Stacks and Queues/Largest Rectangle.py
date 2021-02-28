#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    result = 0
    
    if result < (min(h)*len(h)):
        result = (min(h)*len(h))
            
    index = h.index(min(h))
    
    if index != 0:
        left = largestRectangle(h[:index])
        if left > result:
            result = left
    
    if index+1 != len(h):
        right = largestRectangle(h[index+1:])
        if right > result:
            result = right
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
