# 417. Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/

def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    horizontal, vertical = len(heights), len(heights[0])
    DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1))
    def dfs(i, j, visited):
        visited.add((i, j))
        for dx, dy in DIRECTIONS:
            x, y = i + dx, j + dy
            if 0 <= x < horizontal and 0 <= y < vertical and (x, y) not in visited and heights[i][j] <= heights[x][y]:
                dfs(x, y, visited)
    pacific, atlantic = set(), set()
    for i in range(horizontal):
        dfs(i, 0, pacific)
        dfs(i, vertical - 1, atlantic)
    for j in range(vertical):
        dfs(0, j, pacific)
        dfs(horizontal - 1, j, atlantic)
    return list(pacific & atlantic)