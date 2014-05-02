#! /usr/bin/env python

fname = 'D-small-practice-1'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def neighbours(grid, delta, M, N, x, y):
	result = []
	if x > 0 and grid[y][x-1]:
		result.append(delta[y][x-1])
	if x < N-1 and grid[y][x+1]:
		result.append(delta[y][x+1])
	if y > 0 and grid[y-1][x]:
		result.append(delta[y-1][x])
	if y < M-1 and grid[y+1][x]:
		result.append(delta[y+1][x])
	return result

def numchildren(grid):
	n = 0
	for row in grid:
		for c in row:
			if c:
				n += 1
	return n

def solve(fin):
	M = int(fin.readline())
	N = int(fin.readline())
	grid = []
	
	for x in xrange(M):
		grid.append(map(int, fin.readline().split()))
	turns = 0
	prevgrid = None
	changed = True
	while changed:
		changed = False
		for y in xrange(M):
			for x in xrange(N):
				if grid[y][x] < 12:
					grid[y][x] = 0
		for y in xrange(M):
			for x in xrange(N):
				neigh = neighbours(grid, grid, M, N, x, y)
				if len(neigh) == 0:
					grid[y][x] = 0
		if numchildren(grid) == 0:
			return str(turns) + ' turns'
		delta = []
		for y in xrange(M):
			delta.append([[0] for y in xrange(N)])
		for y in xrange(M):
			for x in xrange(N):
				if grid[y][x]:
					neigh = neighbours(grid, delta, M, N, x, y)
					delta[y][x][0] -= 12
					share = 12/len(neigh)
					for n in neigh:
						n[0] += share
		for y in xrange(M):
			for x in xrange(N):
				if grid[y][x] and delta[y][x][0] != 0:
					grid[y][x] += delta[y][x][0]
					changed = True
		turns += 1
	return str(numchildren(grid)) + ' children will play forever'

T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
