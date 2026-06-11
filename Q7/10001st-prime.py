import math
t = int(input().strip())
cases = []
for a0 in range(t):
    n = int(input().strip())
    cases.append(n)

maxn = max(cases)
no = 2
pfs = []
while len(pfs) < maxn:
    f = 0
    for i in range(1, len(pfs)):
        if no % pfs[i] == 0:
            f = 1
            break
        if pfs[i] > int(math.sqrt(no)):
            break
    if f == 0:
        pfs.append(no)
    if no == 2:
        no += 1
    else:
        no += 2
for c in cases:
    print(pfs[c-1])
