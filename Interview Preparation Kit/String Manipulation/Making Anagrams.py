#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    d = {}
    count = 0
    for i in a:
        d[i] = d.get(i, 0) + 1
    for j in b:
        d[j] = d.get(j, 0) - 1
    for value in d.values():
        count += abs(value)
    return(count)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
