# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/

def minPathSum(self, grid: List[List[int]]) -> int:
    col = len(grid)
    row = len(grid[0])
    for i in range(1, row):
        grid[0][i] = grid[0][i] + grid[0][i - 1]
    for j in range(1, col):
        grid[j][0] = grid[j - 1][0] + grid[j][0]
    for i in range(1, col):
        for j in range(1, row):
            grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
    return grid[-1][-1]