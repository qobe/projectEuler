##
#What is the 10001st prime number? Eg 13 is the 6th prime number
##

from pe3_LPF import isPrime

def nth_prime(nth):
	counter = 1 #includes 2, start at 3
	i = 1
	while counter < nth:
		i+=2
		if isPrime(i):
			counter += 1
		
	print i
		
		