#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
	count = 0
    i = 0
    while i < len(c) - 1 :
        if (c[i] == 0):
            i+= 1
        count+=1
        i+= 1
    return count

# Recursive Solution
    # if len(c) == 1 : return 0
    # if len(c) == 2 : return 0 if c[1]==1 else 1
    # if c[2]==1: 
    #     return 1 + jumpingOnClouds(c[1:])
    # if c[2]==0:
    #     return 1 + jumpingOnClouds(c[2:])    
	
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
