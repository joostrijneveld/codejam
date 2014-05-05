#! /usr/bin/env python

from collections import defaultdict
import heapq

fname = 'E-large-practice'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def dijkstra(lifts, source, dest):
	dist = defaultdict(lambda : float("inf"))
	dist[source] = 0
	pq = []
	heapq.heappush(pq, (0, source))
	while pq:
		t, u = heapq.heappop(pq)
		if t == dist[u]: # to prevent heapremove
			if u == dest:
				return t
			for tuv, v in lifts[u]:
				alt = t + tuv
				if alt < dist[v]:
					dist[v] = alt
					heapq.heappush(pq, (alt, v))
	return -1
		
def solve(fin):
	N = int(fin.readline())
	roomcolor = []
	for i in range(N):
		roomcolor.append(fin.readline()[:-1]) # remove '\n'
		
	M = int(fin.readline())
	minlifts = dict()
	for i in range(M):
		a, b, t = map(int, fin.readline().split())
		A, B = roomcolor[a-1], roomcolor[b-1]
		if (A, B) not in minlifts or minlifts[(A, B)] > t:
			minlifts[(A, B)] = t
	lifts = defaultdict(list)
	for (A, B), t in minlifts.iteritems():
		heapq.heappush(lifts[A], (t, B))
	
	S = int(fin.readline())
	times = []
	for i in range(S):
		p, q = map(int, fin.readline().split())
		P, Q = roomcolor[p-1], roomcolor[q-1]
		times.append(dijkstra(lifts, P, Q))
	return "\n".join(map(str, times))

T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+":\n"+str(solve(fin))+"\n")
fout.close()
fin.close()
