t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    s = 2
    a = 1
    b = 2
    while a + b < n:
        c = a + b
        if c % 2 == 0:
            s += c
        a = b
        b = c
    print(s)
