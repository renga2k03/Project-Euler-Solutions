t = int(input())
for i in range(t):
    n = int(input())
    dist_lines = []
    for i in range(n):
        next_line = []
        lines = list(map(int, input().split()))
        if len(lines) == 1:
            dist_lines.append(lines)
            continue
        for j in range(len(lines)):
            if j > 0 and j < len(dist_lines[i-1]):
                next_line.append(max(dist_lines[i-1][j-1], dist_lines[i-1][j]) + lines[j])
            elif j == 0:
                next_line.append(dist_lines[i-1][j] + lines[j])
            else:
                next_line.append(dist_lines[i-1][j-1] + lines[j])
        dist_lines.append(next_line)
    print(max(dist_lines[-1]))
