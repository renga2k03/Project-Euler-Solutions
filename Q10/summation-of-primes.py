import math
t = int(input().strip())
nl = []
dic = {}
for a0 in range(t):
    n = int(input().strip())
    nl.append(n)
onl = nl.copy()
pfs = []
nl.sort()
maxn = max(nl)
no = 2
j = 0
s = []
while no <= maxn:
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
i = 0
npf = len(pfs)
while i < npf and j < t:
    if pfs[i] >= nl[j]:
        if pfs[i] == nl[j]:
            dic[nl[j]] = sum(pfs[:i+1])
        else:
            dic[nl[j]] = sum(pfs[:i])
        j += 1
    else:
        i += 1
if maxn not in pfs:
    dic[nl[-1]] = sum(pfs)
for n in onl:
    print(dic[n])
