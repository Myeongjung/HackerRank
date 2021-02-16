#!/bin/python3

import math
import os
import random
import re
import sys

def findMedian(dic, idx):
    s = 0
    for i in range(200):
        freq = 0
        if i in dic:
            freq = dic[i]
        s = s + freq
        if s>=idx:
            return i
            
def activityNotifications(expenditure, d):
    dic = {}
    count = 0
    
    for i in range(len(expenditure)):
        val = expenditure[i]
        
        if i >= d:
            med=findMedian(dic, d//2 + d%2)
            print(med)
            if d % 2 == 0:
                ret = findMedian(dic, d//2+1)
                if val >= med + ret:
                    count += 1
            else:
                if val>=med*2:
                    count += 1

        if val not in dic: 
            dic[val] = 0
            
        dic[val] += 1
        
        #print i,dic
        if i>=d:
            prev = expenditure[i-d]
            dic[prev] -= dic[prev]

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
