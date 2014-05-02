#! /usr/bin/env python

fname = 'A-small-attempt0'

fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def solve(fin):
	r1 = int(fin.readline().split()[0])
	for i in range(1,5):
		line = fin.readline()
		if r1 == i:
			row = set(line.split())
	r2 = int(fin.readline().split()[0])
	for i in range(1,5):
		line = fin.readline()
		if r2 == i:
			row2 = set(line.split()) & row
	if len(row2) == 1:
		return next(iter(row2))
	elif len(row2) > 1:
		return "Bad magician!"
	else:
		return "Volunteer cheated!"

T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
