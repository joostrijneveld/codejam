#! /usr/bin/env python

fname = 'A-large-practice'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

repwords = ['','double ', 'triple ', 'quadruple ', 'quintuple ',
	'sextuple ', 'septuple ', 'octuple ', 'nonuple ', 'decuple ']
numbers = ['zero', 'one', 'two', 'three', 'four',
	'five', 'six', 'seven', 'eight', 'nine']

def read_number(N):
	prevx = N[0]
	n = 1
	result = ''
	for x in N[1:]+' ':
		if x == prevx:
			n += 1
		else:
			if n <= 10:
				result += repwords[n-1] + numbers[int(prevx)] + ' '
			else:
				result += (numbers[int(prevx)] + ' ') * n
			n = 1
		prevx = x
	return result

def solve(fin):
	line = fin.readline().split()
	N = line[0]
	pattern = map(int, line[1].split('-'))
	result = ""
	start = 0
	for length in pattern:
		result += read_number(N[start:start+length])
		start += length
	return result

T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
