##
#What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, diagnolly) in the 2020grid.txt
##
import re


def prod(l):
	p = 1
	for x in l:
		p = p * x
	return p

def setGreatest(n):
	global greatest
	if n > greatest:
		greatest = n
	
def prod_neighbors(grid, j, i):
		g = 0
		if grid[j][i] == 0:
			return 0
		#north
		if j < len(grid)-3:
			setGreatest(prod([grid[j][i], grid[j+1][i], grid[j+2][i], grid[j+3][i]]))
			#north east
			if i < len(grid[i])-3:
				setGreatest(prod([grid[j][i], grid[j+1][i+1], grid[j+2][i+2], grid[j+3][i+3]]))
			#north west
			if i >= 3:
				setGreatest(prod([grid[j][i], grid[j+1][i-1], grid[j+2][i-2], grid[j+3][i-3]]))

		#south
		if j >= 3:
			setGreatest(prod([grid[j][i], grid[j-1][i], grid[j-2][i], grid[j-3][i]]))
			#south east
			if i < len(grid[i])-3:
				setGreatest(prod([grid[j][i], grid[j-1][i+1], grid[j-2][i+2], grid[j-3][i+3]]))
			#south west
			if i >= 3:
				setGreatest(prod([grid[j][i], grid[j-1][i-1], grid[j-2][i-2], grid[j-3][i-3]]))
		#east
		if i < len(grid[i])-3:
			setGreatest(prod(grid[j][i:i+4]))
		#west
		if i >= 3:
			setGreatest(prod(grid[j][i-3:i+1]))
	

###################################################
###################################################
f = open("2020grid.txt")
series = re.sub(re.compile('\s+'),"", f.read())
f.close()

grid =[]
global greatest
greatest = 0

c = 0
for i in xrange(20):
	grid.append([])
	for j in xrange(20):
		grid[i].append(int(series[c:c+2]))
		c += 2

for j in xrange(len(grid)):
	for i in xrange(len(grid[j])):
		setGreatest(prod_neighbors(grid, j, i))
print "GREATEST: ", greatest

