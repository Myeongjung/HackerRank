#Day 9: Multiple Linear Regression

import numpy as np

def find_B(X, Y):
    return(np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y))

m, n = map(int, input().split())
X = []
Y = []
for i in range(n):
    data = input().strip().split()
    X.append(data[:m])
    Y.append(data[m:])
q = int(input())

L = []
for _ in range(q):
    L.append(input().strip().split())
    
X = np.array(X, float)
X = np.insert(X, 0, 1, axis=1)
Y = np.array(Y, float)
X_pred = np.array(L, float)
X_pred = np.insert(X_pred, 0, 1, axis=1)

B = find_B(X,Y)

for value in X_pred.dot(B):
    print(round(float(value),2))

