#! /usr/bin/env python

fname = 'C-large-practice'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def solve(fin):
	N = int(fin.readline())
	shelf = map(int, fin.readline().split())
	alex, bob = [], []
	newshelf = []
	for i in shelf:
		if i % 2 == 1:
			alex.append(i)
		else:
			bob.append(i)
	alex.sort(reverse=True)
	bob.sort()
	for i in shelf:
		if i % 2 == 1:
			newshelf.append(alex.pop())
		else:
			newshelf.append(bob.pop())
	return ' '.join(map(str, newshelf))
			
T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
