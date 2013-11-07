##
#From the first 100 natural numbers, ubtract the sum of squares from the square of the sum
##


def ss_difference(range):

	sosq = 0
	sqos= 0

	for i in xrange(1, range+1):
		sosq += i**2
		sqos += i
	sqos = sqos**2
	print "%s - %s = %s" % (sqos, sosq, sqos-sosq)
