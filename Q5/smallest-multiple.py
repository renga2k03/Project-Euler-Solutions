import math
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    no = 1
    pfs = {}
    for i in range(2, n+1):
        f = 0
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                f = 1
                break
        if f == 0:
            pfs[i] = 1
        else:
            temp_i = i
            for j in pfs.keys():
                ct = 0
                while temp_i % j == 0:
                    temp_i = temp_i // j
                    ct += 1
                if pfs[j] < ct:
                    pfs[j] = ct
                if temp_i == 1:
                    break
    for nos in pfs.keys():
        no *= int(nos ** pfs[nos])
    print(no)
