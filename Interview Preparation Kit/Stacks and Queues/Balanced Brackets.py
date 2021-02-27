#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    l = []
    if len(s)%2 != 0:
        return "NO"

    for b in s:
        if b == '[' or b == '{' or b == '(':
            l.append(b)
        elif len(l) != 0:
            a = l.pop()
            if b == ')' and a == '(':
                continue
            elif b == ']' and a == '[':
                continue
            elif b == '}' and a == '{':
                continue
            else:
                return "NO"
        else:    
            return "NO"
        
    if len(l) != 0:
        return "NO"
    
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
