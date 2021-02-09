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
n = input()
l, u, e, o = '','','',''

for c in n:
    if c.isdigit() and int(c)%2 == 0:
        e += c
    elif c.islower():
        l += c
    elif c.isupper():
        u += c
    else:
        o += c

l, u, e, o = sorted(l), sorted(u), sorted(e), sorted(o)

print(''.join(l) + ''.join(u) + ''.join(o) + ''.join(e))

#Using sorted keys
#s = input()
#s = sorted(s,key = lambda x:(x.isdigit() and int(x)%2==0, x.isdigit(), x.isupper(),x.islower(),x))
#print(*(s),sep = '')

# 108. Validating Email Addresses With a Filter
import re

re_exp = r"^[\w-]+\@[0-9a-zA-Z]+\.[a-z]{1,3}$"

def fun(s):
    return re.match(re_exp, s)

# 109. Reduce Function
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y : x * y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
	
# 110. Regex Substitution
import re

def func(match):
    if "&&" in match.group():
        return("and")
    else:
        return("or")

for _ in range(int(input())):
    n = input()
    print(re.sub(r"(?<= )(&&|\|\|)(?= )", func, n))
	
# 111. Validating Credit Card Numbers
import re

re_exp = r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$"

for _ in range(int(input())):
    s = input()

    if re.match(re_exp, s) and not re.search(r"([\d])\1{3}", s.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")
		
# 112. Validating Postal Codes
regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

# 113. Matrix Script
#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

s = ""
for i in zip(*matrix):
    s += "".join(i)
    
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", s))

# 114. Words Score
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score

# 115. Default Arguments
class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    stream.__init__()
    for _ in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
