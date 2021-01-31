# 103. Triangle Quest
for i in range(1,int(input())):
    print((10**(i)//9)*i)

# 104. Triangle Quest 2
for i in range(1,int(input())+1):
    print(((10**i-1)//9)**2)
	
# 105. Classes: Dealing with Complex Numbers
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, no):
        return Complex(self.real+no.real, self.imaginary+no.imaginary)
    def __sub__(self, no):
        return Complex(self.real-no.real, self.imaginary-no.imaginary)
    def __mul__(self, no):
        return Complex(self.real*no.real-self.imaginary*no.imaginary, self.real*no.imaginary+self.imaginary*no.real)
    def __truediv__(self, no):
        x = float(no.real ** 2 + no.imaginary ** 2)
        y = self * Complex(no.real, -no.imaginary)
        return Complex(y.real / x, y.imaginary / x)
    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
		
# 106. Athlete Sort
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    k = int(input())
   
    rows = sorted(arr, key=lambda x:x[k])
    for i in rows:
        print(*i)

# 107. ginortS
# 108. Validating Email Addresses With a Filter
# 109. Reduce Function
# 110. Regex Substitution
# 111. Validating Credit Card Numbers
# 112. Validating Postal Codes
# 113. Matrix Script
# 114. Words Score
# 115. Default Arguments