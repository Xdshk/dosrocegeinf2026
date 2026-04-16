s = open('24_28765.txt').read()
l = 0
k = 0
mx = 0
for r in range(1, len(s)):
    if s[r - 1] == 'B' and s[r] == 'C':
        k += 1
    while k > 180:
        if s[l] == 'B' and s[l + 1] == 'C':
            k -= 1
        l += 1
    mx = max(mx, r - l + 1)

print(mx)