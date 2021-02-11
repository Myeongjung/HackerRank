#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = 0
    d = {}
    for i in range(len(s)):
        for j in range(len(s) - i):
            #slice all characters
            c = ''.join(sorted(s[j:j + i + 1]))
            #count anag
            d[c] = d.get(c, 0) + 1
    for key in d:
        count += (d[key] - 1) * d[key] // 2
    return(count)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
