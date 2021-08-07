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

#103. Largest Permutation
def largestPermutation(k, arr):
    a = dict(enumerate(arr))
    b = {v:k for k,v in a.items()}
    l = len(arr)
    print(a,b)
    for i in range(l):
        if k and a[i]!=l-i:
            x = a[i]
            y = b[l-i]
            a[i] = l-i
            a[y] = x
            b[x] = y
            k-=1
        yield a[i] 

#104. Sherlock and The Beast
def decentNumber(n):
    if n < 3:
        print(-1)
    elif n%3 == 0:
        print('5'*n)
    else:
        a = 5
        while (n-a > 0):        
            if ((n-a) %3 != 0):
                a += 5
            else:
                break
            
        if (n-a) >= 0:
            print('5'*(n-a), '3'*a, sep='')
        else:
            print(-1)

#105. Priyanka and Toys
def toys(w):
    w.sort()
    result = 0
    i = 0
    while i < len(w):
        r = w[i]+4
        count = 1
        for j in range(i+1, len(w)):
            if w[j] <= r:
                count+=1
            else:
                break
        i += count
        result += 1
    return result

#106. Jim and the Orders
def jimOrders(orders):
    orders = sorted(enumerate(orders,1),key=lambda x:sum(x[1]))
    
    return [i[0] for i in orders]

#107. Permuting Two Arrays
def twoArrays(k, A, B):
    A.sort()
    B.sort()
    l = len(A)
    for i in range(l):
        if A[i] + B[l-i-1] >= k:
            continue
        else:
            return "NO"
    return "YES"

#108. Lonely Integer
from collections import Counter

def lonelyinteger(a):
    c = Counter(a)
    for i, v in c.items():
        if v == 1:
            return i

#109. Maximizing XOR
def maximizingXor(l, r):
    return max([i^j for i in range(l, r+1) for j in range(l, r+1)])
	
#110. Sum vs XOR
def sumXor(n):
    count = 0
    
    while(n):
        count += 0 if n%2 else 1
        n//=2
    
    return 2**count
	
#111. Game of Stones
def gameOfStones(n):
    return "Second" if n%7 in [0,1] else "First"

#112. Tower Breakers
def towerBreakers(n, m):
    return 2 if m == 1 or n%2 == 0 else 1

#113. Misère Nim
from functools import reduce

def misereNim(s):
    if (set(s)=={1}) and n%2==1:
        return 'Second'
    elif (set(s)=={1}) and n%2==0:
        return 'First'
    elif reduce((lambda x,y:x^y),s):
        return 'First'
    else:
        return 'Second'


