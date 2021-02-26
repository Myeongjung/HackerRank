#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    p = list(sorted(set(a)))
    q = list(sorted(set(b)))
    r = list(sorted(set(c)))
    
    ai = 0
    bi = 0
    ci = 0
    
    count = 0
    
    while bi < len(q):
        while ai < len(p) and p[ai] <= q[bi]:
            ai += 1
        
        while ci < len(r) and r[ci] <= q[bi]:
            ci += 1
        
        print(ai, ci)
        count += ai * ci
        bi += 1
    
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
