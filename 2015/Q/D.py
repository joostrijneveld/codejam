#! /usr/bin/env python

fname = 'D-small-attempt1'

fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')


def solve(fin):
    X, R, C = map(int, fin.readline().split())
    if (R * C) % X != 0:
        return 'RICHARD'
    if X > max(R, C):  # piece of size 1 by X does not fit
        return 'RICHARD'
    if X >= 3 and min(R, C) < 2:
        return 'RICHARD'
    if (X, R, C) in [(4, 4, 2), (4, 2, 4)]:
        return 'RICHARD'
    return 'GABRIEL'


T = int(fin.readline())
for i in range(1, T+1):
    fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
