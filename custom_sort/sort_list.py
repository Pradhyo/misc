import csv

with open('input4.txt', 'rb') as input_file:
	list_items = csv.reader(input_file, delimiter = ' ')
	
	with open('results.txt', 'wb') as output_file:
		sorted_list = csv.writer(output_file, delimiter = ' ')
		for each in list_items:
			sorted_list.writerow(each)
