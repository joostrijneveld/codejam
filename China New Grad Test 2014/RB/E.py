#! /usr/bin/env python

from collections import deque

fname = 'E-large-practice'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def solve(fin):
	result = ""
	comment = 0
	last_two = deque(maxlen=2)
	while True:
		c = fin.read(1)
		if not c:
			if not comment:
				result += ''.join(last_two)
			return result
		if not comment and len(last_two) == 2:
			result += last_two[0]
		last_two.append(c)
		if ''.join(last_two) == '*/' and comment:
			comment -= 1
			last_two.clear()
		elif ''.join(last_two) == '/*':
			comment += 1
			last_two.clear()
	
fout.write("Case #1:\n"+str(solve(fin)))
fout.close()
fin.close()
