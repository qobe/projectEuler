##
#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2 digit numbers is 9009 = 91 x 99
#Find the largest palindrome made from the product of two 3-digit numbers.
##

def isSym(number):
	return str(number) == str(number)[::-1]

largest_palindrome = 0
for i in xrange(100, 999):
	for j in xrange(100, 999):
		z = i*j
		if isSym(z) and z > largest_palindrome:
			largest_palindrome = z
			f1 = i
			f2 = j
print "Largest palindrome %s = %s x %s"% (largest_palindrome, f1, f2)




