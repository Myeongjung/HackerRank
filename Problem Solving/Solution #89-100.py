#89. The Love-Letter Mystery
def theLoveLetterMystery(s):
    front = s[:len(s)//2]
    back = s[len(s)//2:] if len(s)%2==0 else s[(len(s)//2)+1:]
    back = back[::-1]
    count = 0
    
    for i in range(len(front)):
        count += abs(ord(front[i]) - ord(back[i]))
    return count

#90. Find the Median
def findMedian(arr):
    return sorted(arr)[len(arr)//2]

#91. Palindrome Index
def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    
    a = list(s)
    for i in range(len(a)//2):
        if a[i] != a[len(a)-1-i]:
            print(a.pop(i))
            if a == a[::-1]:
                return i
            else:
                return (len(a)-i)

#92. Anagram
from collections import Counter

def anagram(s):
    if (len(s) % 2 != 0):
        return -1;
    
    l = len(s)
    count = 0
    s1, s2 = Counter(s[:l//2]), Counter(s[l//2:])
    
    for c in s2:
        current = s2[c] - s1.get(c,0)
        if current > 0:
            count += current
    
    return count
	
#93. Making Anagrams
def makingAnagrams(s1, s2):
    count = 0
    c1 = set(s1)
    c2 = set(s2)
    
    for i in c1:
        if i in c2 and s1.count(i) != s2.count(i):
            count += abs(s1.count(i) - s2.count(i))
        elif i not in c2:
            count += s1.count(i)
            
    for i in c2:
        if i not in c1:
            count += s2.count(i)
    
    return count
	
# With Counter
from collections import Counter

def makingAnagrams(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    c1.subtract(c2)
    
    return sum(abs(x) for x in c1.values())

#94. Game of Thrones - I
def gameOfThrones(s):
    return "NO" if sum([s.count(i) % 2 for i in set(s)]) > 1 else "YES"   

#95. String Construction
def stringConstruction(s):
    return len(set(s))

#96. Ice Cream Parlor
from itertools import combinations

def icecreamParlor(m, arr):
    for i in combinations(arr, 2):
        if sum(i) == m:
            a,b = i
            a = arr.index(a)+1
            return [a, arr.index(b,a)+1]
			


