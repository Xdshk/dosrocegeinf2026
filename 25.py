def f(n):
    a=[]
    for d in range(2,n):
        if n%d==0:
            d1=d
            d2=n//d
            if d1%10==7 and d1!=7:
                a.append(d1)
            if d2 % 10 == 7 and d2 != 7:
                a.append(d2)
    return sorted(a)
k=0
for i in range(700000, 10000000):
    r=f(i)
    if len(r)>0:
        k+=1
        print(i,r[0])
