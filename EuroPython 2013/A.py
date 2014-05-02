#! /usr/bin/env python

import bisect

fname = 'A-small-practice-2'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def solve(fin):
	N = int(fin.readline())
	names = []
	n = 0
	for i in range(N):
		name = fin.readline()
		if bisect.bisect(names, name) < len(names):
			n += 1
		bisect.insort(names, name)
	return n
	
T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
