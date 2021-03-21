#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
total = 0

for num in range(n-1, 0, -1):
    for i in range(num):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            total += 1

print("Array is sorted in {0} swaps.\nFirst Element: {1}\nLast Element: {2}"\
.format(total, a[0], a[-1]))