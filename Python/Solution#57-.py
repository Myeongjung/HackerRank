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
		
#65. 


#66.