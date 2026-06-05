t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    npalin = n // 1000
    for i in range(npalin, 100, -1):
        no = i * 1000 + int(''.join(list(str(i))[::-1]))
        if no >= n:
            continue
        f = 0
        nsqr = int(math.sqrt(no))
        for i in range(100, nsqr+1):
            if no % i == 0:
                otherno = no // i
                if len(str(otherno)) == 3:
                    print(no)
                    f = 1
                    break
        if f == 1:
            break
