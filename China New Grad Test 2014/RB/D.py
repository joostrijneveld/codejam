#! /usr/bin/env python

import heapq

fname = 'D-large-practice'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def h(x, y, exx, exy): # manhattan distance heuristic
	return abs(exx - x) + abs(exy - y)

def succ(N, M, grid, x, y):
	result = []
	if x > 0 and grid[x-1][y] != -1:
		result.append((x-1, y))
	if x < N-1 and grid[x+1][y] != -1:
		result.append((x+1, y))
	if y > 0 and grid[x][y-1] != -1:
		result.append((x, y-1))
	if y < M-1 and grid[x][y+1] != -1:
		result.append((x, y+1))
	return result

# def printgrid(N, M, grid, best, enx, eny, exx, exy):
# 	for gcol, bcol, x in zip(grid, best, range(N)):
# 		for g, b, y in zip(gcol, bcol, range(M)):
# 			if x == exx and y == exy:
# 				print 'X',
# 			elif x == enx and y == eny:
# 				print 'E',
# 			elif g == -1:
# 				print '#',
# 			else:
# 				print '%' if b[0] != float('inf') else '.',
# 		print 
# 	print

def a_star(N, M, grid, enx, eny, exx, exy):
	best = [[(float('inf'), 0)] * M for x in range(N)]
	best[enx][eny] = (0, grid[enx][eny])
	pq = []
	heapq.heappush(pq, (0 + h(enx, eny, exx, exy), (enx, eny)))
	windist = float('inf')
	winpower = 0
	while pq:
		t, (x, y) = heapq.heappop(pq)
		d = t - h(x, y, exx, exy)
		if d == best[x][y][0]:
			if t > windist:
				break
			if y == exy and x == exx:
				if t < windist or t == windist and best[x][y][1] > winpower:
					windist = t
					winpower = best[x][y][1]
				continue
			for s in succ(N, M, grid, x, y):
				curr_d, curr_power = best[s[0]][s[1]]
				if (d + 1 < curr_d or d + 1 == curr_d and
						curr_power < best[x][y][1] + grid[s[0]][s[1]]):
					best[s[0]][s[1]] = (d + 1, best[x][y][1] + grid[s[0]][s[1]])
					heapq.heappush(pq, (d + 1 + h(s[0], s[1], exx, exy), s))
	if windist == float('inf'):
		return 'Mission Impossible.'
	# printgrid(N, M, grid, best, enx, eny, exx, exy):
	return winpower
		
def solve(fin):
	N, M = map(int, fin.readline().split())
	enx, eny, exx, exy = map(int, fin.readline().split())
	grid = []
	for y in range(N):
		grid.append(map(int, fin.readline().split()))
	return a_star(N, M, grid, enx, eny, exx, exy)
	
T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
