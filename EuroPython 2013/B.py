#! /usr/bin/env python

import math

fname = 'B-small-practice'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def solve(fin):
	V, D = map(int, fin.readline().split())
	return math.degrees(0.5 * math.asin(max(-1, min(D * 9.80 / (V * V), 1))))

T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
