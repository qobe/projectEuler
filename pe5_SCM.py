##
#project Euler problem 5: SMALLEST MULTIPLE
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
##


#any number divisible by n is also divisible by all of its factors
#20: 20, 10, 5, 4, 2, 1
#19: 19, 1
#18: 18, 9, 6, 3, 2, 1


#factorials may be useful in eliminating repeating factors
#largest multiple divided by the greatest common factor

##########just do prime factors!!!
import math
from pe3_LPF import isPrime

#performs prime factorization on given integer
def factor_primes(n):
	prime_factors = {}
	
	for f in define_factors(n):
		if isPrime(f):
			e = 0
			while n % f == 0:
				n = n / f
				e+=1
			prime_factors[f] = e
	return prime_factors

#returns a list of factors for given integer
def define_factors(n):
	factors = []
	for i in xrange(1, n+1):
		if n % i == 0:
			factors.append(i)
	return factors

def main():
	scm_primes = {}
	for n in xrange(1,21):
		p = factor_primes(n)
		#print n, p
		for k in p:
			if not k in scm_primes or p[k] > scm_primes[k]:
				scm_primes[k] = p[k]
	scm = 1
	for item in scm_primes:
		scm = scm * math.pow(item, scm_primes[item])
	print scm

	
main()
	
if __name__ == '__main()__':
	main()