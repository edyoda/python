'''
wr = open('wr_file','w')
for line in open('file'):
	l = line.split()
	l.sort()
	wr.write(' '.join(l))
	wr.write('\n')

'''
tot_list = []
wr = open('rev_file','w')
for line in open('file'):
	tot_list.insert(0,line.strip())


for elem in tot_list:
	wr.write(elem+'\n')
