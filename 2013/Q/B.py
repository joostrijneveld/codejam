#! /usr/bin/env python

fname = 'B-large-practice'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def solve(fin):
	N, M = map(int, fin.readline().split())
	lawn = []
	rowmax = []
	colmax = []
	for i in range(N):
		row = map(int, fin.readline().split())
		rowmax.append(max(row))
		lawn.append(row)
	for col in zip(*lawn):
		colmax.append(max(col))
	for y in range(N):
		for x in range(M):
			if lawn[y][x] < min(rowmax[y], colmax[x]):
				return 'NO'
	return 'YES'

T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
