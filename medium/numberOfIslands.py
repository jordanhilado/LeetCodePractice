# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

def numIslands(self, grid: List[List[str]]) -> int:
    ctr = 0
    
    def fill(grid, row, col):
        if grid[row][col] == "0":
            return
        grid[row][col] = "0"
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for x, y in dirs:
            if 0 <= row + x < len(grid) and 0 <= col + y < len(grid[row + x]):
                fill(grid, row + x, col + y)
                
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                ctr += 1
                fill(grid, i, j)
    return ctr