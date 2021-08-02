#101. Maximum Perimeter Triangle
from itertools import combinations

def istriangle(x):
    l = sorted(x)
    return True if l[0] + l[1] > l[2] else False

def maximumPerimeterTriangle(sticks):
    c = combinations(sticks, 3)
    result, m = [], 0
    for i in c:
        if istriangle(i) and sum(i)>m:
            result = sorted(i)
            m = sum(i)
            
    if result:
        return result
    else:
        return [-1]

#102. Beautiful Pairs
def beautifulPairs(A, B):
    count = 0
    for a in A:
        if a in B:
            B.remove(a)
            count+=1
    
    if count < len(A):
        return count + 1
    else:
        return count - 1

