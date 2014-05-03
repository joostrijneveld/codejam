#! /usr/bin/env python

fname = 'A-large-practice'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def has_won(board, p):
	diag1 = ''.join([board[i][i] for i in range(4)])
	diag2 = ''.join([board[3-i][i] for i in range(4)])
	cols = [''.join(x) for x in zip(*board)]
	for seq in board + cols + [diag1, diag2]:
		if seq.replace('T', p) == p * 4:
			return True
	return False

def solve(fin):
	board = []
	for y in xrange(4):
		board.append(fin.readline().strip())
	fin.readline() # clear the empty line
	for p in ['X', 'O']:
		if has_won(board, p):
			return p + ' won'
	if '.' in [c for row in board for c in row]:
		return 'Game has not completed'
	return 'Draw'

T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
