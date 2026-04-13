def f(a, b, p):
    if (a + b) >= 65 and (p == 3 or p == 5):
        return True
    elif (a + b) >= 65 and (p == 2 or p == 4):
        return False
    elif (a + b) < 65 and p == 5:
        return False
    if p % 2 == 1:
        return f(a + 1, b, p + 1) and f(a * 3, b, p + 1) and f(a, b + 1, p + 1) and f(a, b * 3, p + 1)
    if p % 2 == 0:
        return f(a + 1, b, p + 1) or f(a * 3, b, p + 1) or f(a, b + 1, p + 1) or f(a, b * 3, p + 1)


for x in range(1, 101):
    if f(6, x, 1):
        print(x)


