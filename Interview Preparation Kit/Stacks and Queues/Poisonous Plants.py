#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):
    l = []
    result = 0
    
    for plant in p:
            days = 1

            while l and l[-1][0] >= plant:
                _, d = l.pop()
                days = max(days, d + 1)
            
            if not l:
                days = 0
            
            result = max(result, days)
            l.append((plant, days))
        
    return result
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
