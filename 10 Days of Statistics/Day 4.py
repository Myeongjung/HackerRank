#Day 4: Binomial Distribution I
import math

#b(x>= 3, n = 6, p = boys/boys+girls)
def binomial_distribution(x, n, p):
    return (math.factorial(n)/(math.factorial(n-x)*math.factorial(x)) * pow(p,x) * pow(1-p, n-x))

#boys:girls = 1.09:1
total, p, n = 0, 1.09/2.09, 6

for x in range(3, n+1):
    total += binomial_distribution(x, n, p)
    
print(round(total,3))

#Day 4: Binomial Distribution II
import math

def binomial_distribution(x, n, p):
    return (math.factorial(n)/(math.factorial(n-x)*math.factorial(x)) * pow(p,x) * pow(1-p, n-x))

total, p, n = 0, 0.12, 10

#1. at most 2 rejects b(x<= 2, n = 10, p = 0.88)
for x in range(3):
    total += binomial_distribution(x, n, p)

print(round(total, 3))

total = 0
#2. at least 2 rejects b(x>= 2, n = 10, p = 0.88)
for x in range(2, n+1):
    total += binomial_distribution(x, n, p)
    
print(round(total,3))

#Day 4: Geometric Distribution I
def geometric_distribution(n,p):
    return (pow((1-p), n-1)*p)

n, p = 5, 1/3

print("{0:.03f}".format(geometric_distribution(n,p)))

#Day 4: Geometric Distribution II
def geometric_distribution(n,p):
    return (pow((1-p), n-1)*p)

total, n, p = 0, 5, 1/3

for x in range(1, n+1):
    total+=geometric_distribution(x,p)
    
print("{0:.03f}".format(total))