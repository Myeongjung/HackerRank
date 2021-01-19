#Day 0: Mean, Median, and Mode

import statistics as st
from scipy import stats

n = int(input())
L = list(map(int, input().split()))

print("{0:.01f}".format(st.mean(L)))
print("{0:.01f}".format(st.median(L)))
print(int(stats.mode(L)[0]))


#Day 0: Weighted Mean

N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))
s = 0

for i in range(N):
    s+=X[i]*W[i]
    
print(round(s/sum(W), 1))