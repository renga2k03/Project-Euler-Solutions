t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    pf = 2
    pfs = []
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
                while n % pf == 0:
                    n = n // pf
                pfs.append(pf)
        if n > 1:
            if pf != 2:
                pf += 2
            else:
                pf += 1
    if n > 1:
        pf = n
    print(pf)
