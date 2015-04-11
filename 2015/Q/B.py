#! /usr/bin/env python

from collections import Counter
from copy import copy

fname = 'B-small-attempt4'

fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

memory = {}


def rec_solve(n):
    froz = frozenset(n.items())
    if froz in memory:
        return memory[froz]
    maxval = max(n)
    if maxval <= 3:
        return maxval
    n_eat = {x-1: v for x, v in n.items() if v > 0 and x > 0}
    n_options = [n_eat]
    for i in range(2, maxval):
        n_move = Counter(n)
        n_move[maxval] -= 1
        n_move.update([i, maxval-i])
        n_move = {x: v for x, v in n_move.items() if v > 0 and x > 0}
        n_options.append(n_move)
    result = 1 + min([rec_solve(n) for n in n_options])
    memory[froz] = result
    return result


def solve(fin):
    fin.readline()  # discard D
    P = Counter(map(int, fin.readline().split()))
    return rec_solve(P)


T = int(fin.readline())
for i in range(1, T+1):
    fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
