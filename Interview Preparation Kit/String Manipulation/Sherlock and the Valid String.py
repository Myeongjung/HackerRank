#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def isValid(s):
    d = Counter(s)
    d = Counter(d.values())
    key = sorted(d.keys())

    if(len(key) == 1):
        return("YES")
    elif(len(key) == 2):
        m1 = max(key)
        m2 = min(key)
        if d.get(m2) == 1:
            return "YES"
        if d.get(m1) > 1 or m1 - m2 > 1:
            return "NO"
        return "YES"
    return ("NO")
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
