#! /usr/bin/env python

from collections import deque
import numpy

fname = 'A-large-practice'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def breakchunks(s):
	lastchunk = None
	prevx = None
	chunks = []
	for x in s:
		if x == prevx:
			lastchunk.append(x)
		else:
			lastchunk = [x]
			chunks.append(lastchunk)
		prevx = x
	return chunks
	
def solve(fin):
	N = int(fin.readline())
	words = []
	for i in range(N):
		words.append(breakchunks(fin.readline().strip()))
	moves = 0
	length = len(words[0])
	if any(length != len(w) for w in words):
		return "Fegla Won"
	for chunks in zip(*words):
		char = chunks[0][0]
		for c in chunks:
			if char != c[0]:
				return "Fegla Won"
		lengths = map(len, chunks)
		target = numpy.median(lengths)
		moves += sum(abs(l - target) for l in lengths)
	return int(moves)

T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
