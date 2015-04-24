import string

delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum() and c != ' ')

with open('input4.txt', 'rb') as input_file:
	list_items = input_file.read().translate(None, delchars).split(' ')
	
print list_items