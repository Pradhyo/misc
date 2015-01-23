# Python program to check if given sudoku is valid

def valid_rows(sudoku):
	"""Check if rows of given sudoku are valid"""
	for row in sudoku:
		if set(row) != set(range(1,len(sudoku)+1)):
			return False
	return True

def check_sudoku(sudoku):
	"""Check if given sudoku is valid"""
	return valid_rows(sudoku) and valid_rows(zip(*sudoku))


correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]


incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               

    
print check_sudoku(incorrect3)

print check_sudoku(incorrect4)

print check_sudoku(incorrect5)

print check_sudoku(correct)

