from shopMenu import rFile
from wFile import writeF
from vidMenu import menu
from end import logO
from shopDel import delF


check = True

while check != False:
	menu()
	try:
		u = int(raw_input('\n>>  '))
		if u == 0:
			logO()
			check = False
		else:
			if u == 1:
				print 'NAME:\t MOVIE:\n'
				r = 'vids.txt'
				rFile(r) #check = True
			elif u == 2:
				nP = str(raw_input('Name  : '))
				nV = str(raw_input('Movie : '))
				newCus = (nP + ', ' + nV).upper()
				wr = 'vids.txt'
				writeF(wr,newCus) #check = True
			elif u == 3:
				rmN = str(raw_input('Name   : '))
				rmV = str(raw_input('Movie  : '))
				rm = (rmN + ',' + rmV).upper()
				rm2 = (rmN + ', ' + rmV).upper()
				r = 'vids.txt'
				a = 'r'
				b = 'w'
				delF(r,a,b,rm,rm2) #check = True
	except ValueError:
		print 'Invalid input!'
