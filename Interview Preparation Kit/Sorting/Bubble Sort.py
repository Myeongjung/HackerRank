#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    count = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if (a[i] > a[j]):
                tmp = a[j]
                a[j] = a[i]
                a[i] = tmp
                count += 1
    print("Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}"\
    .format(count,min(a),max(a)))
    
if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
