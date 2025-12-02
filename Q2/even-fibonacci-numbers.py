t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum = 2
    a = 1
    b = 2
    while a + b < n:
        c = a + b
        if c % 2 == 0:
            sum += c
        a = b
        b = c
    print(sum)
