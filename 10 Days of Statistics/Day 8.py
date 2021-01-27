#Day 8: Least Square Regression Line
def model_predict(a, b, x):
    return (b*x + a)

def model_fit(x, y, n):
    sum_x = sum(x)
    sum_y = sum(y)
    x_pow = sum([(pow(x[i],2)) for i in range(n)])
    mul_x_y = sum([a*b for a,b in zip(x,y)])
    
    b = (n * mul_x_y - sum_x * sum_y) / (n * x_pow - pow(sum_x, 2))
    a = (sum_y / n) - b * (sum_x / n)
    
    return a, b

if __name__ == '__main__':
    n = 5
    L=[]
    for _ in range(n):
        L.append(list(map(int, input().split())))
    
    #Transpose the matrix
    x,y = zip(*L)

    a, b = model_fit(x, y, n)
    
    predict_value = 80
    
    print(round(model_predict(a, b, predict_value), 3))


#Day 8: Pearson Correlation Coefficient II

The regression line of y on x is 3x+4y+8=0, and the regression line of x on y is 4x+3y+7=0. What is the value of the Pearson correlation coefficient?

Note: If you haven't seen it already, you may find our Pearson Correlation Coefficient Tutorial helpful in answering this question.

() 1
() -1
() 3 / 4
() -4 / 3
() 4 / 3
(X) -3 / 4

==>
1. rewrite the equations
y = -3/4x - 2
x = -3/4y - 7/4

b1, b2 = -3/4

2. apply pearson
we learned p = b1* std_x / std_y

p = b1* std_x / std_y
p = b2* std_y / std_x

p^2 = b1 * b2
	   = 9/16
	   
p = 3/4

but both of the original line equations have negative slopes.
So, p = -3/4