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
	
#39. 

#40. 

#41. 

#42. 

#43. 

#44. 

#45. 

#46. 
