#! /usr/bin/env python

fname = 'B-small-attempt0'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def solve(fin):
	A, B, K = map(int, fin.readline().split())
	n = 0
	for a in range(A):
		for b in range(B):
			if a & b < K:
				n += 1
	return n

T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
