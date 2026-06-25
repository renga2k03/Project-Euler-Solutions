import math
def divsum(n):
    s = 1
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            if i != n // i:
                s += (i + n // i)
            else:
                s += i
    return s

t = int(input())
tlist = []
for i in range(t):
    tlist.append(int(input()))
tsorted = list(set(tlist)).copy()
tsorted.sort()
maxn = tsorted[-1]
i = 0
tcasesum = {}
amic = []
totsum = 0
for n in range(1, maxn+1):
    if n in amic:
        totsum += n
    else:
        dsum1 = divsum(n)
        dsum2 = divsum(dsum1)
        if n == dsum2 and n != dsum1:
            if n not in amic:
                amic.append(n)
                totsum += n
                amic.append(dsum1)
    if n == tsorted[i]:
        tcasesum[tsorted[i]] = totsum
        i += 1
for i in range(t):
    print(tcasesum[tlist[i]])
