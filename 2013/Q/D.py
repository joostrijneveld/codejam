#! /usr/bin/env python

fname = 'filename'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def solve(fin):
	return "solution"

T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
