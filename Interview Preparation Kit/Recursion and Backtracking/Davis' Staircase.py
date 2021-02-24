#!/bin/python3

import math
import os
import random
import re
import sys

cache = {}
def stepPerms(n):
    result = 0
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4
    if n not in cache:
        cache[n] = stepPerms(n-1)+stepPerms(n-2)+stepPerms(n-3)
    return cache[n]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
