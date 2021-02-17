#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    contests.sort(key=lambda x:(-x[1], -x[0]))
    result = 0
    
    for contest in contests:
        luck, important = contest
        if important == 0:
            result += luck
        elif k > 0:
            k -= 1
            result += luck
        else:
            result -= luck
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
