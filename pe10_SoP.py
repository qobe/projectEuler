##
#The sum of the primes below 10 is 2+3+5+7 = 17
#Find the sum of all the primes below two million
##
import time
from pe3_LPF import isPrime

ceiling = 2000000

i = 3
sum = 2
t0 = time.time()
while i < ceiling:
	if isPrime(i):
		sum += i
	i += 2
t1 = time.time()
print sum
print "time: ", t1 - t0