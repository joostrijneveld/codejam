#! /usr/bin/env python

fname = 'A-large-practice'

fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')


def changing_rate(m, N):
    return sum(max(0, m[i] - m[i+1]) for i in range(N-1))


def constant_rate(m, N):
    rate = max(m[i] - m[i+1] for i in range(N-1))
    return sum(min(rate, m_i) for m_i in m[:-1])


def solve(fin):
    N = int(fin.readline())
    m = list(map(int, fin.readline().split()))
    return '{} {}'.format(changing_rate(m, N), constant_rate(m, N))

T = int(fin.readline())
for i in range(1, T+1):
    fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
