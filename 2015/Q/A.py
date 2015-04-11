#! /usr/bin/env python

fname = 'A-large'

fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def solve(fin):
    s = map(int, fin.readline().split()[1])
    needed = 0
    clapping = 0
    for i, v in enumerate(s):
        if clapping < i:
            needed += i - clapping
            clapping = i
        clapping += v
    return needed


T = int(fin.readline())
for i in range(1,T+1):
    fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
