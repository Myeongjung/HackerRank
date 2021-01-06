#1. Say "Hello, World!" With Python
print("Hello, World!")

#2 Python If-Else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0 or n in range(6,21):
        print("Weird")
    else:
        print("Not Weird")

#3. Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print("{0} \n{1} \n{2}".format(a+b, a-b, a*b))
	
#4. Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
	#The expected result shows 11 decimal digits
    print("{0} \n{1:.11f}".format(a//b, a/b))
	
#5. Loops
if __name__ == '__main__':
    n = int(input())
	
    [print(i**2) for i in range(n)]
	
	#simple way
    #for i in range(n):
    #    print(i**2)
    
	#Arbitrary argument list
	#print(*[i**2 for i in range(n)], sep ='\n')
	
#6. Print Function
if __name__ == '__main__':
    n = int(input())
    
    [print(i, end='') for i in range(1,n+1)]
	
#7. List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])
	
#8 Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    print(sorted(set(arr))[-2])
    
    #Another solution with list
	#arr = list(map(int, input().split()))
    #print(max([i for i in arr if i != max(arr)]))