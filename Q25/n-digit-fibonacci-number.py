t = int(input())
tlist = []
for i in range(t):
    tlist.append(int(input()))
tsorted = list(set(tlist)).copy()
tsorted.sort()
maxn = tsorted[-1]
n = 2
a = b = 1
tsoln = {}
i = 0
ndigits = 1
while ndigits <= maxn and i < len(tsorted):
    if tsorted[i] == ndigits:
        tsoln[tsorted[i]] = n
        i += 1
    c = a + b
    a = b
    b = c
    n += 1
    if b // 10 ** ndigits > 0:
        ndigits += 1
for t in tlist:
    print(tsoln[t])
