#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    if k == len(c):
        return sum(c)
    else:
        c = sorted(c, reverse = True)
        price = 0
        customer = {}

        for i in range(len(c)):
            price += c[i] * (customer.get(i%k, 0) + 1)
            customer[i%k] = customer.get(i%k, 0) + 1
        return price   
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
