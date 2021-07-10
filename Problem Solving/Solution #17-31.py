#17. Subarray Division
def birthday(s, d, m):
    count = 0
    for i in range(len(s)-m+1):
        if sum(s[i:i+m]) == d:
            count += 1
    return count

#18. Divisible Sum Pairs
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
                
    return count

#19. Migratory Birds
from collections import Counter

def migratoryBirds(arr):
    c = Counter(arr)
    result = freq = 0
    for key, value in sorted(c.items()):           
        if value > freq:
            result = key
            freq = value
            
    return result

#20. Day of the Programmer
def dayOfProgrammer(year):
    if year%4==0 and (year<1918 or year%400==0 or year%100!=0):
        return "12.09.%s" % year
    elif year == 1918:
        return "26.09.1918"
    return "13.09.%s" % year

#21. Bill Division
def bonAppetit(bill, k, b):
    shared = (sum(bill) - bill[k])//2
    print(b-shared if shared != b else "Bon Appetit")

#22. Drawing Book
def pageCount(n, p):
    return min(p//2,n//2-p//2) 

#23. Electronics Shop
def getMoneySpent(keyboards, drives, b):
    return max([sum([x,y]) for x in keyboards for y in drives if sum([x,y]) <= b]+[-1])

#24. Cats and a Mouse
def catAndMouse(x, y, z):
    d1 = abs(x-z)
    d2 = abs(y-z)
    
    return "Cat A" if d1 < d2 else "Cat B" if d1 > d2 else "Mouse C"

#25. Picking Numbers
from collections import Counter

def pickingNumbers(a):
    results = []
    c = Counter(a)
    for i in c:
        results.append(c[i]+max(c[i+1], c[i-1]))
    return max(results)

#26. The Hurdle Race
def hurdleRace(k, height):
    return 0 if k > max(height) else max(height)-k
	
#27. Designer PDF Viewer
def designerPdfViewer(h, word):
    height = 0
    
    height = max([h[ord(i)-ord('a')] for i in word if h[ord(i)-ord('a')]>height])

    return height * len(word)


#28. Utopian Tree
def utopianTree(n):
    return 1 if n == 0 else utopianTree(n-1) + 1 if n % 2 == 0 else 2 * utopianTree(n-1)

#29. Angry Professor
def angryProfessor(k, a):
    return 'YES' if sum(map(lambda x: x <= 0, a)) < k else 'NO'

#30. Beautiful Days at the Movies
def beautifulDays(i, j, k):
    count = 0
    for idx in range(i, j+1):
        count = count + 1 if abs(idx - int(str(idx)[::-1])) % k == 0 else count
    
    return count
	
#31. Viral Advertising
def viralAdvertising(n):
    people = 5;
    cumulative = 0;
    
    for i in range(n):
        people = people//2
        cumulative += people
        people *= 3

    return cumulative