#! /usr/bin/env python

fname = 'D-large-practice'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

delta = ((0, -1), (1, 0), (0, 1), (-1, 0))
direction = ('N', 'E', 'S', 'W')
startdir = ((1, 2),
			(0, 3))

def solve(fin):
	N = int(fin.readline())
	maze = ['#'*(N+2)]
	for i in range(N):
		maze.append('#' + fin.readline().strip() + '#')
	maze.append('#'*(N+2))
	maze = zip(*maze) # (y, x) -> (x, y)
	y, x, ey, ex = map(int, fin.readline().split())
	i = 0
	moves = ""
	d = startdir[int(y > 1)][int(x > 1)]
	seen = set()
	while i < 10000:
		if (x, y, d) in seen:
			break
		if x == ex and y == ey:
			return str(i) + '\n' + str(moves)
		seen.add((x, y, d))
		left = delta[(d - 1) % 4]
		wall_left = maze[x + left[0]][y + left[1]] == '#'
		wall_front = maze[x + delta[d][0]][y + delta[d][1]] == '#'
		if wall_left and wall_front: # turn right
			d = (d + 1) % 4
			continue
		if not wall_left: # turn left, move
			d = (d - 1) % 4
		x += delta[d][0]
		y += delta[d][1]
		i += 1
		moves += direction[d]
	return "Edison ran out of energy."
		
T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
