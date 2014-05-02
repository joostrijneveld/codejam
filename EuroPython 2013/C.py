#! /usr/bin/env python

from collections import defaultdict, deque

fname = 'C-small-practice-2'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def solve(fin):
	M = int(fin.readline())
	league = defaultdict(set)
	for i in range(M):
		a, b = fin.readline().split()
		league[a].add(b)
		league[b].add(a)
	while len(league) > 0:
		queue = deque()
		queue.append(league.iterkeys().next())
		dep1, dep2 = set(), set()
		while len(queue) > 0:
			k = queue.popleft()
			if k not in league:
				continue
			v = league.pop(k)
			queue.extend(v)
			if len(dep1 & v) == 0:
				dep1.add(k)
			elif len(dep2 & v) == 0:
				dep2.add(k)
			else:
				return 'No'	
	return 'Yes'

T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
