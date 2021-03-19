class Calculator():
    def power(self, n, p):
        if n < 0 or p < 0:
            raise MyError()
        return n**p
    
class MyError(Exception):
    def __str__(self):
        return "n and p should be non-negative"

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   