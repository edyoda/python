import csv

with open('input.csv') as fd:
	st = csv.reader(fd,delimiter=',')
	print st
	for row in st:
		print row

