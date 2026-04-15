from math import *
def center(K):
    mns = 10**10
    c = 0
    for t1 in K:
        sm = 0
        for t2 in K:
            sm += dist(t1[:2],t2[:2])
        if mns > sm:
            mns = sm
            c = t1
    return c

a = open('27_B_28766 (1).txt').readlines()
for i in range(len(a)):
    a[i] = a[i].replace(',','.').split()
    x,y,z = a[i]
    x = float(x)
    y = float(y)
    a[i] = x,y,z
k1 = []
k2 = []
k3 = []
for i in range(len(a)):
    x,y,z = a[i]
    if y < 15:
        k1.append(a[i])
    if 15 < y< 23:
        k2.append(a[i])
    if y > 23:
        k3.append(a[i])
c1 = center(k1)
c2 = center(k2)
c3 = center(k3)
g = []
for i in a:
    if i[2].count("Z") == 1 and i[2].count('I') == 1 and i[2].count('V') == 0:
        g.append(i)

def claster(K):
    mn = 10**10
    for t1 in K:
        for t2 in K:
            if t1 != t2:
                if t1 in g:
                    if t2 in g:
                        mn = min(dist(t1[:-1],t2[:-1]),mn)
    return mn

print(claster(k1)*10000)
print(claster(k2))
print(claster(k3)*10000)
