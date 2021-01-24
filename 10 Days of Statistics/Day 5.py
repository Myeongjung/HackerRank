#Day 5: Poisson Distribution I
import math

#p(k, lambda) = lambda**k * e**-lambda / k!
def poisson_distribution(k,l):
    e = 2.71828
    return (pow(l,k) * pow(e,-l) / math.factorial(k))

k, l = 5, 2.5

print("{0:.03f}".format(poisson_distribution(k,l)))

#Day 5: Poisson Distribution II
avgA, avgB = 0.88, 1.55

costA = 160 + 40 * (avgA + pow(avgA,2))
costB = 128 + 40 * (avgB + pow(avgB,2))

print("{0:.03f}\n{1:.03f}".format(costA,costB))

#E(costA) = E(160 + 40X**2)
#		   	   = E(160) + E(40X**2)
#		   	   = 160 + 40E(X**2)
#		   	   = 160 + 40(lambda + lambda**2)

#Day 5: Normal Distribution I
import math

mean, std = 20, 2

def cum_prob(mean, std, x):
    return 0.5 * (1 + math.erf( (x-mean) / (std*math.sqrt(2)) ))

print("{0:.03f}".format(cum_prob(mean,std, 19.5)))
print("{0:.03f}".format((cum_prob(mean,std, 22)- cum_prob(mean,std, 20))))

#Day 5: Normal Distribution II
import math

mean, std = 70, 10

def cum_prob(mean, std, x):
    return 0.5 * (1 + math.erf( (x-mean) / (std*math.sqrt(2)) ))

print("{0:.02f}".format((1-cum_prob(mean,std, 80))*100))
print("{0:.02f}".format((1-cum_prob(mean,std, 60))*100))
print("{0:.02f}".format(cum_prob(mean,std, 60)*100))
