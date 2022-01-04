# 463. Island Perimeter
# https://leetcode.com/problems/island-perimeter/

def islandPerimeter(self, grid: List[List[int]]) -> int:
    R, C, count = len(grid), len(grid[0]), 0
    for row in range(R):
        for col in range(C):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0: count += 1
                if col == 0 or grid[row][col - 1] == 0: count += 1
                if col == C - 1 or grid[row][col + 1] == 0: count += 1
                if row == R - 1 or grid[row + 1][col] == 0: count += 1
    return count