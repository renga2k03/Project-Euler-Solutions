t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sumsq = n * (n + 1) * (2 * n + 1) // 6
    sqsum = int((n * (n + 1) // 2) ** 2)
    print(abs(sumsq - sqsum))
