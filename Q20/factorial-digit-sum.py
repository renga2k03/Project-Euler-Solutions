t = int(input())
tlist = []
for i in range(t):
    tlist.append(int(input()))
tsorted = list(set(tlist.copy()))
tsorted.sort()
maxn = tsorted[-1]
tsoln = {}
f = 1
tindex = 0
for i in range(maxn + 1):
    if i == 0:
        f *= 1
    else:
        f *= i
    if i == tsorted[tindex]:
        tsoln[tsorted[tindex]] = sum(list(map(int, list(str(f)))))
        tindex += 1
for i in range(t):
    print(tsoln[tlist[i]])
