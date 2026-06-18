import math
def primefactorize(n):
    pf = 2
    pfs = []
    c = 1
    while pf * pf <= n:
        if n % pf == 0:
            f = 0
            for i in pfs:
                if pf % i == 0:
                    f = 1
                    break
                if i > int(math.sqrt(pf)):
                    break
            if f == 0:
                expc = 0
                while n % pf == 0:
                    expc += 1
                    n = n // pf
                c *= (expc + 1)
                pfs.append(pf)
        if n > 1:
            if pf != 2:
                pf += 2
            else:
                pf += 1
    pfs.append(n)
    if n != 1:
        c *= 2
    return(c)

t = int(input())
nl = []
while t:
    n = int(input())
    nl.append(n)
    t -= 1
tr = []
onl = nl.copy()
dic = {}
nl.sort()
s = 1
i = 1
pfc = 0
j = 0
while j < len(onl):
    if s == 1:
        pfc = 1
    else:
        pfc = primefactorize(s)
    if pfc > nl[j]:
        dic[nl[j]] = s
        j += 1
    else:
        i += 1
        s += i
for n in onl:
    print(dic[n])
