##
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a^2+b^2=c^2
#There exists exactly one Pythagorean triplet for which a + b + c = 1000
#Find the product of abc
##

from pe8 import multiply_list
from pe5_SCM import define_factors


#generate triples using Euclids formula
def euclids(m, n):
	a = m**2 - n**2
	b = 2*m*n
	c = m**2 + n**2
	return [a,b,c]

def sum_list(l):
	sum = 0
	for n in l:
		sum = sum + int(n)
	return sum
	