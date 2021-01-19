#46. Arrays
import numpy

def arrays(arr):
    return numpy.array(arr,float)[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

	
#47. Mod Divmod
n = int(input())
m = int(input())
div = divmod(n,m)
print('{0}\n{1}\n{2}'.format(div[0],div[1],div))
	
	
#48. Power - Mod Power
a = int(input())
b = int(input())
m = int(input())
print("{}\n{}".format(pow(a,b),pow(a,b,m)))
	
	
#49. Integers Come In All Sizes
a,b,c,d = (int(input()),int(input()),int(input()),int(input()))

print(pow(a,b)+pow(c,d))
		
		
#50. Set Mutations
n = int(input())
A = set(map(int, input().split()))
m = int(input())

for _ in range(m):
    cmd = input().split()[0]
    L = set(map(int, input().split()))
    cmd = cmd + '(L)'
    eval('A.'+cmd)

print(sum(A))
	
	
#51. The Captain's Room
from collections import Counter

size = int(input())
L = list(map(int, input().split()))

for v,c in Counter(L).items():
    if c == 1:
        print(v)
        break
	
	
#52. Any or All
n = int(input())
l = input().split()

print(all([int(i)>0 for i in l]) and any([j==j[::-1] for j in l]))

			
#53. Re.split()
regex_pattern = r"\D+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))
	
	
#54. Re.findall() & Re.finditer()
import re

consonants = '[qwrtypsdfghjklzxcvbnm]'
vowel = '[aeiou]'
regex_pattern = r'(?<='+consonants+')('+vowel+'{2,})' + consonants

print("\n".join(re.findall(regex_pattern, input(), re.I) or ['-1']))

		
#55. Re.start() & Re.end()
import re

s = input()
k = input()
pattern = re.compile(k)
m = pattern.search(s)

if not m:
    print("(-1, -1)")
    
while m:
    print("({0}, {1})".format(m.start(), m.end()-1))
    m = pattern.search(s, m.start()+1)


#56. Collections.deque()
from collections import deque

d = deque()

for _ in range(int(input())):
    inputs = input().split()
    cmd = inputs[0]
    arg = inputs[1:]
    cmd += '('+ ''.join(arg) + ')'
    eval('d.'+cmd)
    
print(*d)
