def rFile(x):
	rd = open(x, 'r')

	temp = rd.readlines()
	for line in temp:
		line = line[:].rstrip('\n').split(', ')
		#print line
		cus = ', '.join(line)
		print str(cus)
	rd.close()

