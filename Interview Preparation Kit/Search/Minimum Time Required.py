#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    machines.sort()
    minDays = 0
    maxDays = machines[-1]*goal
    result = -1
    
    while (minDays < maxDays):
        mid = (minDays + maxDays) // 2
        unit = 0
        for machine in machines:
            unit += mid // machine

        if unit < goal :
            minDays = mid+1
        else:
            result = mid
            maxDays = mid
    
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
