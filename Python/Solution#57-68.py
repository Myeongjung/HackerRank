#57. Check Subset
case = int(input())

for _ in range(case):
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    B = set(map(int, input().split()))
    
    if all([i in B for i in A]):
        print(True)
    else:
        print(False)
	
#58. Check Strict Superset
A = set(map(int, input().split()))
n = int(input())
flag = True

for _ in range(n):
    L = set(map(int, input().split()))

    if all([i in A for i in L]) and len(L) < len(A):
        continue
    else:
        flag = False

print(flag)
	
#59. Class 2 - Find the Torsional Angle
import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, no):
        a = self.x - no.x
        b = self.y - no.y
        c = self.z - no.z
        return Points(a,b,c)
    def dot(self, no):
        return (self.x*no.x)+(self.y*no.y)+(self.z*no.z)
    def cross(self, no):
        a = self.y*no.z - self.z*no.y
        b = self.z*no.x - self.x*no.z
        c = self.x*no.y - self.y*no.x
        return Points(a,b,c)
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
		
#60. Zipped!
student, subject = map(int, input().split())
L = []

for _ in range(subject):
    L.append(list(map(float, input().split())))
    
for i in zip(*L):
    print("{0:.01f}".format(sum(i)/subject))
	
#61. input()
x, k = map(int, input().split())
L = input()
print(eval(L) == k)
	
#62. Python Evaluation
eval(input())
			
#63. Detect Floating Point Number
import re


regex_pattern = r"^[+-]?\d*\.\d+$"

for _ in range(int(input())):
    if re.findall(regex_pattern, input()):
        print(True)
    else:
        print(False)
	
#64. Map and Lambda Function
cube = lambda x: x**3

def fibonacci(n):
    lis = [0,1]
    for i in range(2,n):
        lis.append(lis[i-2] + lis[i-1])
    return(lis[0:n])

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
		
#65. Group(), Groups() & Groupdict()
import re

re_exp = r'([a-z0-9])\1'

m = re.search(re_exp, input())
if m:
    print(m.group(1))
else:
    print(-1)

#66. Validating Roman Numerals
thousand = "(?:(M){0,3})?"
hundred  = "(?:(D?(C){0,3})|(CM)|(CD))?"
ten      = "(?:(L?(X){0,3})|(XC)|(XL))?"
unit     = "(?:(V?(I){0,3})|(IX)|(IV))?"

regex_pattern = r"^" + thousand + hundred + ten + unit + "$"

import re
print(str(bool(re.match(regex_pattern, input()))))

#67. Validating phone numbers
import re

re_exp = r"^[7-9]\d{9}$"

for _ in range(int(input())):
    print('YES' if re.match(re_exp, input()) else 'NO')
	
#68. Validating and Parsing Email Addresses
import email.utils
import re

re_exp = r"^[a-zA-Z][\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"

for _ in range(int(input())):
    n, e = email.utils.parseaddr(input())
    if re.match(re_exp, e):
        print(email.utils.formataddr((n, e)))