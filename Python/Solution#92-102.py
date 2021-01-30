#92. The Minion Game

def minion_game(string):
    stuart_score = 0
    kevin_score = 0
    vowels = 'AEIOU'
    
    for i in range(len(string)):
        if s[i] in vowels:
            kevin_score += (len(string) - i)
        else:
            stuart_score += (len(string) - i)

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")
		
#93. Merge the Tools!

def merge_the_tools(string, k):
    L = []
    for i in range(0,len(string),k):
        L = string[i:k+i]
        tmp = []
        for s in L:
            if (s not in tmp):
                tmp.append(s)
                
        print(''.join(tmp))
		
#94. Time Delta
from datetime import datetime

def time_delta(t1, t2):
    time_format = '%a %d %b %Y %H:%M:%S %z'
    result = int(abs((datetime.strptime(t1, time_format) - 
                    datetime.strptime(t2, time_format)).total_seconds()))
    return (str(result))
	
#95. Find Angle MBC
import math

ab = int(input())
bc = int(input())

print(str(int(round(math.degrees(math.atan(ab/bc)),0)))+'°')

#96. No Idea!
n, m = input().split()
L = input().split()
A = set(input().split())
B = set(input().split())
print(sum([(i in A) - (i in B) for i in L]))

#97. Word Order
import collections

L = []
for _ in range(int(input())):
    L.append(input())

counter = collections.Counter(L)

print(len(counter))
[print(counter[s], end=' ') for s in counter]

#98. Compress the String!

# [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
# [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D

from itertools import groupby

s = input()

print(*[(len(list(g)), int(k)) for k, g in groupby(s)])

#99. Company Logo 
import collections

if __name__ == '__main__':
    s = sorted(input())

    counter = collections.Counter(s).most_common(3)
    
    [print(*(s, c)) for s, c in counter]
	
#100. Piling Up!
for i in range(int(input())):
    n = int(input())
    c = [int(i) for i in input().split()]
    min_c = c.index(min(c))
    left = c[:min_c]
    right = c[min_c+1:]
    if left == sorted(left, reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")
		
#101. Iterables and Iterators
import itertools as it

n = int(input())
L = input().split()
c = list(it.combinations(L, int(input())))
result = list(filter(lambda x: 'a' in x, c))

print(round(len(result)/len(c),3))

#102. Maximize It!
import itertools as it

k, m = map(int, input().split())
L = (list(map(int, input().split()))[1:] for _ in range(k))
result = map(lambda x: sum(i**2 for i in x)%m, it.product(*L))

print(max(result))