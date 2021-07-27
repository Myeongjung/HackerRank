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
	

