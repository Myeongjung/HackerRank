#Day 7: Pearson Correlation Coefficient I
import statistics as st

def pearson(n, x, y): 
    x_mean = st.mean(x)
    x_std = (sum([(i - x_mean)**2 for i in x]) / n)**0.5
    y_mean = st.mean(y)
    y_std = (sum([(i - y_mean)**2 for i in y]) / n)**0.5

    return sum([(x[i] - x_mean) * (y[i] - y_mean) for i in range(n)]) / (n*x_std*y_std)

n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

print(round(pearson(n, x, y), 3))

#Day 7: Spearman's Rank Correlation Coefficient

import statistics as st

def spearman(n, x_r, y_r):
    return 1- (6*sum([(x_r[i] - y_r[i])**2 for i in range(n)]) / (n*(n**2-1)))

n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

x_r = [sorted(x).index(i)+1 for i in x]
y_r = [sorted(y).index(i)+1 for i in y]
    
print(round(spearman(n, x_r, y_r), 3))