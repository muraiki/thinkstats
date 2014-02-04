import thinkstats
from math import sqrt

weights = [1, 1, 1, 3, 3, 591]

pmean = thinkstats.Mean(weights)
pvariance = thinkstats.Var(weights)
psd = sqrt(pvariance)

print pmean
print pvariance
print psd