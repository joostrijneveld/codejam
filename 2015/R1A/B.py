#! /usr/bin/env python

from fractions import gcd
from functools import reduce

fname = 'B-small-practice'

fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')


def lcm(l):
    def _lcm(a, b):
        return a * b // gcd(a, b)
    return reduce(_lcm, l, 1)


def solve(fin):
    B, N = list(map(int, fin.readline().split()))
    M = list(map(int, fin.readline().split()))
    period = lcm(M)
    per_period = sum(period // m for m in M)
    N %= per_period
    if N == 0:
        N = per_period

    T = [0] * B
    for i in range(N-1):
        t_min = min(T)
        T = [t - t_min for t in T]
        for i, t in enumerate(T):
            if t == 0:
                T[i] = M[i]
                break

    t_min = min(T)
    for i, t in enumerate(T):
        if t == t_min:
            return i+1

T = int(fin.readline())
for i in range(1, T+1):
    fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
