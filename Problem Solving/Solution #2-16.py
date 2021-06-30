#2. Solve Me First
def solveMeFirst(a,b):
	return a+b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)

#3. Simple Array Sum
def simpleArraySum(ar):
    return sum(ar)

#4. Compare the Triplets
def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i, j in zip(a,b):
        if i>j:
            alice += 1
        elif j>i:
            bob += 1
    return([alice, bob])
	
#5. A Very Big Sum
def aVeryBigSum(ar):
	return sum(ar)
	
#6. Diagonal Difference
def diagonalDifference(arr):
    p_diagonal, s_diagonal = 0, 0
    for i in range(len(arr)):
        p_diagonal += arr[i][i]
        s_diagonal += arr[i][len(arr)-i-1]
    return abs(p_diagonal - s_diagonal)
	
#7. Plus Minus
def plusMinus(arr):
    result = [0,0,0]
    n = len(arr)
    for i in arr:
        if i > 0:
            result[0] += 1
        elif i < 0:
            result[1] += 1
        else:
            result[2] += 1
    print("{:.6f}\n{:.6f}\n{:.6f}".format(result[0]/n, result[1]/n, result[2]/n))
	
#8. Staircase
def staircase(n):
    print("\n".join([("#"*i).rjust(n, ' ') for i in range(1, n+1)]))
	
#9. Mini-Max Sum
def miniMaxSum(arr):
    print(sum(arr)-max(arr), sum(arr)-min(arr), sep=' ')
	
#10. Birthday Cake Candles
def birthdayCakeCandles(candles):
    highest = max(candles)
    result = 0
    for i in candles:
        if i == highest:
            result += 1
            
    return result
	
#11. Time Conversion
def timeConversion(s):
    hour_format = s[-2:]
    if hour_format == 'PM':
        return str(int(s[:2]) + 12) + s[2:-2] if s[:2] != '12' else s[:-2]
    else:
        return s[:-2] if s[:2] != '12' else '00' + s[2:-2]
		
#12. Grading Students
def gradingStudents(grades):
    result = []
    for grade in grades:
        result.append(grade) if grade%5 < 3 or grade < 38 else result.append(grade + (5- (grade%5)))
    return result
	
#13. Apple and Orange
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = [a+apple for apple in apples]
    oranges = [b+orange for orange in oranges]
    
    print(len([x for x in apples if s<=x<=t]))
    print(len([x for x in oranges if s<=x<=t]))

#14. Number Line Jumps
def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return "NO"
    return "YES" if (x2-x1)%(v1-v2) == 0 else "NO"

#15. Between Two Sets
from functools import reduce

def LCM(a, b):
    return (a*b)//math.gcd(a,b)

def getTotalX(a, b):
    lcm = reduce(LCM, a, 1)
    gcd = reduce(math.gcd, b)

    lcm_copy = lcm

    count = 0
    print(lcm, gcd)
        
    while lcm <= gcd:
        print(lcm)
        if(gcd % lcm) == 0:
            count += 1
        lcm = lcm + lcm_copy

    return count

#16. Breaking the Records
def breakingRecords(scores):
    high = low = scores[0]
    counts = [0, 0]
    
    for i in range(1,len(scores)):
        if scores[i] > high:
            counts[0] += 1
            high = scores[i]
        elif scores[i] < low:
            counts[1] += 1
            low = scores[i]
    return counts