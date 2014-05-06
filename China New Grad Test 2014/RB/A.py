#! /usr/bin/env python

fname = 'A-large-practice'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def solve(fin):
	N = int(fin.readline())
	grid = []
	for i in range(N*N):
		grid.append(fin.readline().split())
	refset = set(map(str, range(1, N*N+1)))
	for line in grid + zip(*grid):
		if refset != set(line):
			return 'No'
	for i in range(N*N):
		offy = N * (i // N)
		offx = N * (i % N)
		block = set()
		for y in range(offy, offy+N):
			for x in range(offx, offx+N):
				block.add(grid[y][x])
		if refset != block:
			return 'No'
	return 'Yes'

T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
