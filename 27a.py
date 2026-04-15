a = open('27_A_28766 (1).txt').readlines()
for i in range(len(a)):
    a[i] = a[i].replace(',', '.').split()
    a[i][0] = float(a[i][0])
    a[i][1] = float(a[i][1])
    print(a[i])
k1 = []
k2 = []
for i in a:
    x,y,z = i
    if y > 8:
        k1.append(i)
    else:
        k2.append(i)
print(len(k1))
print(len(k2))
from math import *
def center(K):
    c = 0
    mns = 10**10
    for t1 in K:
        sm = 0
        for t2 in K:
            sm += dist(t1[:-1],t2[:-1])
        if mns > sm:
            mns = sm
            c = t1

    return c

print(center(k1))
c1 = center(k1)
g = []
for t in a:
    if t[2].count('Y') == 1 and t[2].count('III') == 1:
        g.append(t)

print(len(g))

mns = 10**10
for i in g:
    mns = min(dist(c1[:-1],i[:-1]),mns)
mx = 0
for i in g:
    mx = max(dist(c1[:-1],i[:-1]),mx)

print(mns,mx)
