# Find path through maze 
# Maze is a 2D array with 1s as walls and 0s as paths

puzzle = [[0, 0, 0, 0, 0],[1, 0, 1, 1, 0],[1, 0, 0, 1, 0],[1, 1, 0, 1, 1],[1, 1, 0, 0, 0]]

for row in puzzle:
	print row

print
currenti = 0
currentj = 0
endi = 4
endj = 4

def solve(currenti, currentj, endi, endj):
	if currenti == endi and currentj == endj:
		puzzle[currenti][currentj] = 2
		return True
	if currenti not in range(5) or currentj not in range(5):
		return False
	if puzzle[currenti][currentj] in [1,2]:
		return False
	puzzle[currenti][currentj] = 2
	for i in [currenti-1, currenti+1]:
		solve(i, currentj, endi, endj)
	for j in [currentj-1, currentj+1]:
		solve(currenti, j, endi, endj)	

	
print solve(currenti,currentj,endi,endj)

for row in puzzle:
	print row

