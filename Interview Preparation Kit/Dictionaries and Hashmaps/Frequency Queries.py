#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    d = dict()
    results = []
    freq = defaultdict(int)
    
    for query in queries:
        op, value = query
        init = d.get(value, 0)
        
        if(op == 3):
            results.append(1 if freq.get(value) else 0)
        elif(op == 1):
            freq[init] -= 1
            d[value] = init + 1
            freq[d.get(value,0)] += 1
        elif(op == 2 and init):
            freq[init] -= 1
            d[value] -= 1
            freq[d.get(value,0)] += 1
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
