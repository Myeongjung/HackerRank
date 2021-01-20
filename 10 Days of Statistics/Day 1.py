#Day 1: Quartiles

import statistics as st

n = int(input())
init = sorted(map(int, input().split()))
Q2 = int(st.median(init))

if n%2 == 0:
    L = init[:n//2]
    U = init[n//2:]
else:
    L = init[:init.index(Q2)]
    U = init[init.index(Q2)+1:]
    
Q1 = int(st.median(L))
Q3 = int(st.median(U))

print("{0}\n{1}\n{2}".format(Q1,Q2,Q3))


#Day 1: Interquartile Range

import statistics as st

n = int(input())
init = list(map(int, input().split()))
freq = list(map(int, input().split()))
newList = []

for i in range(n):
    tmp = init[i]
    newList += [init[i]] * freq[i]
    
newList.sort()
Q2 = int(st.median(newList))
t = len(newList)//2

if n%2 == 0:
    L = newList[:t]
    U = newList[t:]
else:
    L = newList[:t]
    U = newList[t+1:]
    
Q1 = int(st.median(L))
Q3 = int(st.median(U))

print("{0:.01f}".format(Q3 - Q1))

#Day 1: Standard Deviation

import math

n = int(input())
L = list(map(int, input().split()))
mean = sum(L)/n
total = 0
for i in range(n):
    total += pow(L[i] - mean, 2)

sd = math.sqrt(total / n)

print(round(sd,1))
