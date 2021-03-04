#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxCircle function below.
def maxCircle(queries):
    elems  = {} 
    groups = {} 
    results = []
    maxl = 0
    for a,b in queries:
        if a not in elems:
            groups[a] = set([a])
            elems[a] = a
        if b not in elems:
            groups[b] = set([b])
            elems[b] = b
        if elems[a] != elems[b]:
            a,b =elems[a],elems[b]
            if len(groups[b])>len(groups[a]): a,b=b,a
            groups[a] |= groups[b]
            for p in groups[b]: elems[p] = a
            del groups[b]
        maxl = max(maxl, len(groups[elems[a]]))
        results.append(maxl)
    return results
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
