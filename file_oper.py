wr = open('out_file','w') #opening file in write mode, if file doesn't exist create one

for l in open('in_file'):
    f = []
    ldata = l.split()
    for word in ldata:
        if len(word) < 4:
            f.append(word)
    wr.write(' '.join(f) + '\n')


    


