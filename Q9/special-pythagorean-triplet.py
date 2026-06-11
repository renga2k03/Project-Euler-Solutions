import math
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    maxprod = -1
    for c in range(n // 3, n // 2 + 1):
        prod = ((n * n - 2 * n * c) * c) // 2
        d = c * c - n * n + 2 * n * c
        if d >= 0:
            a = ((n - c) - math.sqrt(d)) // 2
            b = ((n - c) + math.sqrt(d)) // 2
            if maxprod < prod and a > 0 and b > 0 and a * a + b * b == c * c:
                maxprod = prod
    print(maxprod)
