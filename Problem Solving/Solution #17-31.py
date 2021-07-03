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

#22. 

#23. 

#24. 

#25. 

#26. 

#27. 

#28. 

#29. 

#30. 

#31. 
