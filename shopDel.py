def delF(x,y,z,rv1,rv2):
	r = open(x,y)
	reading = r.readlines()
	r.close()

	w = open(x,z)
	for line in reading:
		if line == rv1 or line == rv2:
			pass
		else:
			w.write(line)
	w.truncate()
	w.close()