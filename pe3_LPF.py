import math
##
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
##


#check all factors up to the square root of the input number

def main():
	input = 600851475143
	print "Largest Prime Factor of %s is %s." % (input, lpf(input))
	
def lpf(input):	
	factors = []
	for i in xrange(2, math.trunc(math.sqrt(input))):
		if input % i == 0 and isPrime(i):
			factors.append(i)
	print factors
	return factors.pop()


def isPrime(n):
	if(n == 2 or n == 5):
		result = True
	elif(n == 1 or n % 2 == 0 or n % 5 == 0):
		result = False
	else:
		i = 3
		result = True
		while i <= math.sqrt(n) and result:
			if n % i == 0:
				if i != n:
					result = False
			i += 2
			
	
	return(result)
 
if __name__ == '__main__':
	main()