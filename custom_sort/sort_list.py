import string

# Characters to be removed-  all ascii except alphanumerals and whitespace
delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum() and c != ' ')

with open('input4.txt', 'rb') as input_file:
	# Build list of items after removing special characters
	list_items = input_file.read().translate(None, delchars).split(' ')
	
with open('results.txt', 'wb') as output_file:
	# Join list elements with space in between and write to output_file
	output_file.write(' '.join(list_items))