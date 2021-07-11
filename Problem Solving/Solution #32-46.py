#32. Save the Prisoner!
def saveThePrisoner(n, m, s):
    return ((s + m - 2) % n) + 1

#33. Circular Array Rotation
def circularArrayRotation(a, k, queries):
    [a.insert(0, a.pop()) for _ in range(k)]

    return [a[i] for i in queries]

#34. Sequence Equation
def permutationEquation(p):
    return [p.index(p.index(i+1)+1)+1 for i in range(len(p))]

#35. Jumping on the Clouds: Revisited
def jumpingOnClouds(c, k):
    energy = 100
    n = len(c)
    i = k % n
    energy -= c[i] * 2 + 1
    while i != 0:
        i = (i + k) % n
        energy -= c[i] * 2 + 1
        
    return energy

#36. Find Digits
def findDigits(n):
    count = 0
    for i in str(n):
        if i == '0':
            continue
        if n % int(i) == 0:
            count+=1
            
    return count

#37. Append and Delete
def appendAndDelete(s, t, k):
    numSameChars = min(len(s), len(t))
    for i in range(len(t)):
        if s[:i] != t[:i]:
            numSameChars = i-1
            break

    diff = len(s)-numSameChars + len(t)-numSameChars
    return 'Yes' if (diff <= k and diff%2 == k%2) or len(s) + len(t) < k else 'No'

#38. Sherlock and Squares
def squares(a, b):
    return math.floor(b**0.5) - math.ceil(a**0.5) + 1
	
#39. Library Fine
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    elif m1 > m2 and y1 == y2:
        return 500*(m1-m2)
    else:
        return 0 if (d1-d2) < 0 or m1-m2 < 0 or y1-y2<0 else 15*(d1-d2)

#40. Cut the sticks
def cutTheSticks(arr):
    result = []
    while len(arr) > 0:
        result.append(len(arr))
        val = min(arr)
        arr = [i - val for i in arr if i != val]
    
    return result

#41. Equalize the Array
from collections import Counter

def equalizeArray(arr):
    c = Counter(arr)
    return len(arr) - max(c.values())

#42. ACM ICPC Team
def acmTeam(topic):
    d = []
    resdic = {}
    m = 0
    for t in topic:
        temp = set()
        for i in range(len(t)):
            if t[i]=='1':
                temp.add(i)
        d.append(temp.copy())
    
    for i in range(len(d)-1):
        for j in range(i+1,len(d)):
            l = len(d[i].union(d[j]))
            m = max(m,l)
            resdic[l]=resdic.get(l,0)+1
    return [m, resdic[m]]
	
#43. Taum and B'day
def taumBday(b, w, bc, wc, z):
    return min([b*bc + w*wc, (b+w)*bc + w*z, (b+w)*wc + b*z])

#44. Modified Kaprekar Numbers
def kaprekarNumbers(p, q):
    result = []
    for i in range(p, q+1):
        sq=i**2
        d=10**len(str(i))
        l=sq//d
        r=sq%d
        
        if l+r == i:
            result.append(i)
    
    if result:
        print(*result)
    else:
        print("INVALID RANGE")

#45. Beautiful Triplets
def beautifulTriplets(d, arr):
    count = 0
    for i in arr:
        if i+d in arr and i+d+d in arr:
            count+= 1
    return count


#46. Minimum Distances
def minimumDistances(a):
    result = []
    for i in range(len(a)):
        if a[i] in a[i+1:]:
            result.append(a.index(a[i], i+1)-i)
    
    if result:
        return min(result)
    else:
        return -1
