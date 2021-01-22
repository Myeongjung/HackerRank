#81 Zeros and Ones
import numpy as np

args = list(map(int, input().split()))

print(np.zeros((args),dtype=int))
print(np.ones((args),dtype=int))

#82 Eye and Identity
import numpy as np

n, m = map(int, input().split())
np.set_printoptions(legacy='1.13')
print(np.eye(n,m))

#83 Array Mathematics
import numpy as np

n, m = map(int, input().split())

a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)

print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n'))

#84 Floor, Ceil and Rint
import numpy as np

a = np.array(input().split() , float)
np.set_printoptions(legacy='1.13')
print(np.floor(a), np.ceil(a), np.rint(a), sep='\n')

#85 Sum and Prod    
import numpy as np

n, m = map(int,input().split())

a = np.array([input().split() for _ in range(n)], int)

print(np.prod(np.sum(a, axis=0)))

#86 Min and Max
import numpy as np

n, m = map(int,input().split())

a = np.array([input().split() for _ in range(n)], int)

print(np.max(np.min(a, axis=1)))

#87 Mean, Var, and Std
import numpy as np

n, m = map(int,input().split())

a = np.array([input().split() for _ in range(n)], int)

print(np.mean(a, axis = 1), np.var(a, axis=0), np.around(np.std(a),11) , sep='\n')

#88 Dot and Cross    
import numpy as np

n = int(input())

a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)

print(np.dot(a,b))

#89 Inner and Outer
import numpy as np

a = np.array(input().split(), int)
b = np.array(input().split(), int)

print(np.inner(a,b), np.outer(a,b), sep='\n')

#90 Polynomials
import numpy as np

a = np.array(input().split(), float)
x = float(input())

print(np.polyval(a, x))

#91 Linear Algebra
import numpy as np

n = int(input())
a = np.array([input().split() for _ in range(n)], float)

print(np.around(np.linalg.det(a), 2))