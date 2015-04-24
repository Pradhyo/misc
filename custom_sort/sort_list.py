#!/usr/bin/env python

import string
import sys

# Characters to be removed-  all ascii except alphanumerals and whitespace
delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum() and c != ' ')
input_file_name = sys.argv[1] # second argument from command line
output_file_name = sys.argv[2] # third argument from command line

with open(input_file_name, 'rb') as input_file:
	# Build list of items after removing special characters
	list_items = input_file.read().translate(None, delchars).split(' ')

print list_items
	
with open(output_file_name, 'wb') as output_file:
	# Join list elements with space in between and write to output_file
	output_file.write(' '.join(list_items))