grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)
    
maxprod = 0
for i in range(20):
    for j in range(20):
        up = down = left = right = 0
        if j >= 3:
            left = 1
        if j < 17:
            right = 1
        if i >= 3:
            up = 1
        if i < 17:
            down = 1
        if up:
            maxprod = max(maxprod, grid[i][j] * grid[i-1][j] * grid[i-2][j] * grid[i-3][j])
            if left:
                maxprod = max(maxprod, grid[i][j] * grid[i-1][j-1] * grid[i-2][j-2] * grid[i-3][j-3])
            elif right:
                maxprod = max(maxprod, grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3])
        if down:
            maxprod = max(maxprod, grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j])
            if left:
                maxprod = max(maxprod, grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3])
            elif right:
                maxprod = max(maxprod, grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3])
        if left:
            maxprod = max(maxprod, grid[i][j] * grid[i][j-1] * grid[i][j-2] * grid[i][j-3])
        if right:
            maxprod = max(maxprod, grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3])
          
print(maxprod)
