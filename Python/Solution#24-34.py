#24. String Formatting
def print_formatted(n):
    results = []
    width = len("{0:b}".format(n))
    
    for i in range(1, n+1):
        d = str(i)
        o = oct(i)[2:]
        h = hex(i)[2:].upper()
        b = bin(i)[2:]

        results.append([d, o, h, b])
        
    for i in results:
        print(*(rep.rjust(width) for rep in i))
        
if __name__ == '__main__':

#25. Alphabet Rangoli
import string

def print_rangoli(s):
    alpha = string.ascii_lowercase

    tmp = []
    for i in range(s):
        c = "-".join(alpha[i:s])
        tmp.append((c[::-1]+c[1:]).center(4*s-3, "-"))
    print('\n'.join(tmp[:0:-1]+tmp))
    
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
	
#26. itertools.product()
#without product
if __name__ == '__main__':
    A = input().split()
    B = input().split()
       
    [print('({0}, {1})'.format(x,y), end=' ') for x in A for y in B]
	
	from itertools import product

#with product
if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
       
    print(*product(a, b))
	
#27. collections.Counter()
from collections import Counter

if __name__ == '__main__':
    n = int(input())
    sizes = Counter(list(map(int, input().split())))
    earned = 0

    for _ in range(int(input())):
        size, price = map(int, input().split())
        
        if sizes[size] > 0:
            sizes[size] -= 1
            earned += price
        
    print(earned)
	
#28. itertools.permutations()
from itertools import permutations

if __name__ == '__main__':
    L, n = input().split()

    for i in permutations(sorted(L),int(n)):
        print(*i, sep='')
		
#29. Polar Coordinates
from cmath import polar

if __name__ == '__main__':
    [print(i) for i in polar(complex(input()))]
	
#30. Introduction to Sets
def average(array):
    return(sum(set(array))/len(set(array)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
	
#31. DefaultDict Tutorial
from collections import defaultdict

if __name__ == '__main__':
    d = defaultdict(list)
    n,m = map(int, input().split())
    L = []
    for i in range (n):
        d[input()].append(str(i+1))
        
    for i in range (m):
        L.append(input())
    
    for i in L:
        if i in d:
            print(' '.join(d[i]))
        else:
            print(-1)
			
#32. Calendar Module
import calendar

if __name__ == '__main__' :
    m,d,y = map(int, input().split())

    print((calendar.day_name[calendar.weekday(y,m,d)].upper()))
	
#33. Exceptions
if __name__ == '__main__':
n = int(input())

for i in range(n):
	try:
		a,b = map(int, input().split())
		print(a//b)
	except BaseException as e:
		print('Error Code:', e)
		
#34. Collections.namedtuple()
from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    columns = input().split()
    students = namedtuple('student', columns)
    total = 0
    
    for i in range(n):
        v1, v2, v3, v4= input().split()
        student = students(v1,v2,v3,v4)
        total += int(student.MARKS)
        
    print(total/n)