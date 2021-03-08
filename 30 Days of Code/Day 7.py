#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    temp = []
    
    for _ in range(len(arr)):
        temp.append(arr.pop())
        
    print(*[e for e in temp], sep=' ')