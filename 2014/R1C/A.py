#! /usr/bin/env python

from fractions import gcd
import bisect

fname = 'A-large'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

twopowers = [2 ** i for i in range(41)]

def solve(fin):
	P, Q = map(int, fin.readline().split('/'))
	g = gcd(P, Q)
	P, Q = P/g, Q/g
	if Q not in twopowers:
		return 'impossible'
	return bisect.bisect_left(twopowers, float(Q)/P)
	
T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
