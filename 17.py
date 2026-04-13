a = open('17_28762.txt').readlines()
b = []
for x in a:
    b.append(int(x))

mn = 10**10
for x in b:
    if x % 23 == 0:
        mn = min(mn, x)
print(mn)
mxs = 0
k = 0
for x in range(len(b)-1):
    if b[x] % mn == 0 or b[x+1] % mn == 0:
        k += 1
        mxs = max(mxs, b[x] + b[x+1])

print(k,mxs)