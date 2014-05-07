#! /usr/bin/env python

fname = 'A-large-practice'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def binsearch(low, high, fn, t): # finds highest x such that x <= t
	if abs(high - low) <= 1:
		return high if fn(high) <= t else low
	mid = (high + low) // 2
	if fn(mid) <= t:
		return binsearch(mid, high, fn, t)
	else:
		return binsearch(low, mid, fn, t)

def solve(fin):
	r, t = map(int, fin.readline().split())
	return binsearch(0, 10 ** 18,
		lambda i: (2 * r - 3) * i + 2 * i * (i + 1), t)
		
def solve_small(fin):
	r, t = map(int, fin.readline().split())
	painted = 0
	i = 0
	while painted <= t:
		i += 1
		# painted += 2 * r + 4 * i - 3
		painted = (2 * r - 3) * i + 4 * (i * (i + 1) / 2)
	return i-1

T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
