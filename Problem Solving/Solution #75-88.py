#75. Caesar Cipher
def caesarCipher(s, k):
    abc = "abcdefghijklmnopqrstuvwxyz"
    pos = {c: i for i, c in enumerate(abc)}

    ciphered = []
    for c in s:
        cl = c.lower()
        if cl in abc:
            new_ind = (pos[cl] + k) % 26
            cipher_letter = abc[new_ind] if c.islower() else abc[new_ind].upper()
            ciphered.append(cipher_letter)
        else:
            ciphered.append(c)
            
    return ("".join(ciphered))

#76. Mars Exploration
def marsExploration(s):
    count = 0
    for i in range(len(s)):
        if s[i] != 'SOS'[i%3]:
            count += 1
            
    return count

#77. HackerRank in a String!
def hackerrankInString(s):
    return 'YES' if re.search(r'.*?'.join(list("hackerrank")), s) else 'NO'

#78. Pangrams
from collections import Counter

def pangrams(s):
    c = Counter(s.lower().replace(" ", ""))
    
    return "pangram" if len(c.keys()) == 26 else "not pangram"

#79. Weighted Uniform Strings
alpha = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

def weightedUniformStrings(s, queries):
    weights = set()
    ctr = 1
    for i in range(len(s)):
        weight = alpha[s[i]]
        if (i+1 != len(s) and s[i+1] == s[i]):
            ctr += 1
        else:
            ctr = 1
        weights.add(weight*ctr)
    
    return ['Yes' if q in weights else 'No' for q in queries]

#80. Separate the Numbers
def separateNumbers(s):
    n = len(s)
    for i in range(1, n//2 + 1):
        check = s[:i]
        add = int(check)
        while check in s:
            add += 1
            check += f'{add}'
            if check == s:
                break
        else:
            continue
        print('YES', s[:i])
        break
    else:
        print('NO')


#81. Smart Number
import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    if num / val == val:
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")
		
#82. XOR Strings
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res

s = input()
t = input()
print(strings_xor(s, t))

#83. Poker Nim
import functools

def pokerNim(k, c):
    return 'First' if functools.reduce(lambda x, y: x ^ y, c) else 'Second'

#84. Nimble Game
def nimbleGame(s):
    x=0
    for i in range(1,len(s)):
        if s[i]%2:
            x^=i
    return "First" if x else "Second"
	
#85. Funny String
def funnyString(s):
    diff = []
    for i in range(len(s)):
        if i+1 <= len(s)-1:
            diff.append(abs(ord(s[i]) - ord(s[i+1])))
    return "Funny" if diff == diff[::-1] else "Not Funny"

#86. Gemstones
def gemstones(arr):
	return len(set.intersection(*map(set,arr)))

#87. Beautiful Binary String
def beautifulBinaryString(b):
    return b.count('010')
	
#88. Closest Numbers
def closestNumbers(arr):
    arr.sort()
    result = []
    m = float('inf')
    for i in range(len(arr)-1):
        m = min(arr[i+1]-arr[i],m)  
    
    for i in range(len(arr)-1): 
        if arr[i+1]-arr[i] == m:
            result.append(arr[i])
            result.append(arr[i+1])
	return result