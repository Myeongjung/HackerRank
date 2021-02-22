#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    l = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    
    for i in range(len(s1)):
        for j in range(len(s1)):
            if s1[i] == s2[j]:
                l[i+1][j+1] = l[i][j] + 1;
            else:
                l[i+1][j+1] = max(l[i+1][j], l[i][j+1])

    return l[len(s1)][len(s2)];

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
