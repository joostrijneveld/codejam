#! /usr/bin/env python

import math
import bisect

fname = 'C-large-practice-1'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def gen_palindromes(maxlen):
	palindromes = []
	palindromes.append(range(0, 10))
	palindromes.append([0] + range(11, 100, 11))
	def gen_palindromes(L):
		palindromes.append([])
		if L % 2 == 0:
			for n in palindromes[L-1 - 2]:
				for x in range(10):
					p = n * 10 + x + x * (10 ** (L-1))
					palindromes[L-1].append(p)
		else:
			tenpower = 10 ** (L//2)
			for n in palindromes[L-1 - 1]:
				head = n // tenpower * tenpower
				tail = n % tenpower
				for x in range(10):
					p = head * 10 + tail + x * tenpower
					palindromes[L-1].append(p)
	for i in range(3, maxlen+1):
		gen_palindromes(i)
	return palindromes

def flatten_strip_leadingzero(palindromes): # GCJ does not count leading-zero
	flat = []
	for L in range(1, len(palindromes)+1):
		tenpower = 10 ** (L-1)
		for n in palindromes[L-1]:
			n2 = str(n * n)
			if n // tenpower > 0 and n2 == n2[::-1]:
				flat.append(n)
	return flat

palindromes = sorted(flatten_strip_leadingzero(gen_palindromes(7)))

def solve(fin):
	A, B = map(int, fin.readline().split())
	a, b = math.sqrt(A), math.sqrt(B)
	l = bisect.bisect_left(palindromes, a)
	r = bisect.bisect_right(palindromes, b)
	return r - l

T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
