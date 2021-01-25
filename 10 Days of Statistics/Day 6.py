#Day 6: The Central Limit Theorem I
import math

x, n = 9800, 49
mean, std = 205, 15

def cum_prob(mean, std, x):
    return 0.5 * (1 + math.erf( (x-mean) / (std*math.sqrt(2)) ))

mean = n * mean
std = std * n**0.5

print("{0:.04f}".format(cum_prob(mean,std, x)))

#Day 6: The Central Limit Theorem II
import math

x, n = 250, 100
mean, std = 2.4, 2

def cum_prob(mean, std, x):
    return 0.5 * (1 + math.erf( (x-mean) / (std*math.sqrt(2)) ))

mean = n * mean
std = std * n**0.5

print("{0:.04f}".format(cum_prob(mean,std, x)))

#Day 6: The Central Limit Theorem III
n, mean, std= 100, 500, 80
interval, z = 0.95, 1.96

#sd_sample = sd/ sqrt(n)
sd_sample = std / (n**0.5)
print("{0:.02f}".format(mean - sd_sample*z))
print("{0:.02f}".format(mean + sd_sample*z))
