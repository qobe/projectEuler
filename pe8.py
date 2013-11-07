##
#find the greatest product of five consecutive digits in the 1000-digit number
##
f = open("1000digits.txt")
series = f.read().strip()
f.close()

def multiply_list(l):
	prod = 1
	for n in l:
		prod = prod * int(n)
	return prod

def main():
	i=0
	greatest = 0
	while i < len(series)-3:
		prod = multiply_list(series[i:i+5])
		if prod > greatest:
			greatest = prod
		i+=1
	print "greatest: ", greatest
	
main()
	
if __name__ == '__main()__':
	main()