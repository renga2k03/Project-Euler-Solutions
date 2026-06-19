t = int(input())
maxn = 0
maxm = 0
l = []
for i in range(t):
    n, m = map(int, input().split())
    l.append((n, m))
    if n > maxn:
        maxn = n
    if m > maxm:
        maxm = m
grid = [[0 for i in range(maxm)] for j in range(maxn)]
for i in range(maxn):
    grid[i][0] = 2 + i
for j in range(maxm):
    grid[0][j] = 2 + j
for i in range(1, maxn):
    for j in range(1, maxm):
        grid[i][j] = grid[i][j-1] + grid[i-1][j]
for n, m in l:
    print(grid[n-1][m-1] % (10**9 + 7))
