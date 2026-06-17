t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum3 = sum5 = sum15 = 0
    n -= 1
    if n > 2:
        l3 = n - n % 3
        n3 = (l3 - 3) // 3 + 1
        sum3 = n3 * (3 + l3) // 2
    if n > 4:
        l5 = n - n % 5
        n5 = (l5 - 5) // 5 + 1
        sum5 = n5 * (5 + l5) // 2
    if n > 14:
        l15 = n - n % 15
        n15 = (l15 - 15) // 15 + 1
        sum15 = n15 * (15 + l15) // 2
    print(sum3 + sum5 - sum15)
