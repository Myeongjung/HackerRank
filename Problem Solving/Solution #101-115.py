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


