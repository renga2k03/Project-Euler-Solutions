t = int(input().strip())
for a0 in range(t):
    n,k = list(map(int, input().strip().split(' ')))
    num = input().strip()
    l = list(str(num))
    maxprod = 0
    for i in range(len(l) - k):
        win = l[i:i+k]
        prod = 1
        for j in win:
            prod *= int(j)
        if maxprod < prod:
            maxprod = prod
    print(maxprod)
