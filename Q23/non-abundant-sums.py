import math
def factsum(n):
    s = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i == i:
                s += i
            else:
                s += (i + n // i)
    return s

t = int(input())
tlist = []
for i in range(t):
    tlist.append(int(input()))
tsorted = list(set(tlist)).copy()
tsorted.sort()
maxn = tsorted[-1]
i = 0
abundant = []
tcasesoln = {}
for n in range(maxn + 1):
    if tsorted[i] < 12:
        tcasesoln[tsorted[i]] = "NO"
        i += 1
    else:
        if factsum(n) > n:
            abundant.append(n)
        if n == tsorted[i]:
            flag = 0
            for ab in abundant:
                if (n - ab) in abundant:
                    flag = 1
                    tcasesoln[n] = "YES"
                    break
            if flag == 0:
                tcasesoln[n] = "NO"
            i += 1
for i in range(t):
    print(tcasesoln[tlist[i]])
