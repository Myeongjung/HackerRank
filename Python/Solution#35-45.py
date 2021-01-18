#35. Collections.OrderedDict()
#With Regular Expression
from collections import OrderedDict
import re

if __name__ == '__main__':
    n = int(input())
    d = OrderedDict()
    for _ in range(n):
        val = input()
        item = ' '.join(re.findall('[a-zA-Z]+', val))
        price = int(''.join(re.findall('\d+', val)))
        
        if item in d:
            d[item] += price
        else:
            d[item] = price
            
    [print(*i) for i in d.items()]
	
#With rsplit
from collections import OrderedDict

if __name__ == '__main__':
    d = OrderedDict()
    for _ in range(int(input())):
        try: 
            item, price = input().rsplit(' ', 1)
        except EOFError as e: 
            print(e)
            
        if item in d:
            d[item] += int(price)
        else:
            d[item] = int(price)
            
    [print(*i) for i in d.items()]
	
#36. Symmetric Difference
if __name__ == '__main__' :
    n, L1 = (int(input()), set(input().split()))
    m, L2 = (int(input()), set(input().split()))

    result = L1.difference(L2)
    result.update(L2.difference(L1))
    print('\n'.join(sorted(result, key=int)))
	
#37. itertools.combinations()
from itertools import combinations

if __name__ == "__main__" :
    L, n = input().split()
    
    for i in range (1, int(n)+1) :
        for j in combinations(sorted(L),i):
            print(''.join(j))
	
#38. Incorrect Regex
import re

if __name__ == "__main__" :
    for _ in range(int(input())):
        try:
            re.compile(input())
        except:
            print(False)
            continue
        print(True)
	
#39. Set .add()
if __name__ == "__main__" :
    L = set()
    for _ in range(int(input())):
        L.add(input())
    print(len(L))
		
#40. Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    inputs = input().split()
    cmd = inputs[0]
    args = inputs[1:]
    
    cmd += "(" + "".join(args)+")"
    eval('s.' + cmd)
	#in one line
    #eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))
	
#41. itertools.combinations_with_replacement()
from itertools import combinations_with_replacement

L, n = input().split()

for j in combinations_with_replacement(sorted(L),int(n)):
    print(''.join(j))
	
#42. Set .union() Operation
n, L = (int(input()), set(input().split()))
m, L2 = (int(input()), set(input().split()))
    
print(len(L.union(L2)))
			
#43. Set .intersection() Operation
n, L = (int(input()), set(input().split()))
m, L2 = (int(input()), set(input().split()))
    
print(len(L.intersection(L2)))
	
#44. Set .difference() Operation
n, L = (int(input()), set(input().split()))
m, L2 = (int(input()), set(input().split()))
    
print(len(L.difference(L2)))
		
#45. Set .symmetric_difference() Operation
n, L = (int(input()), set(input().split()))
m, L2 = (int(input()), set(input().split()))
    
print(len(L.symmetric_difference(L2)))