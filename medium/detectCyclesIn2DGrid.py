# 1559. Detect Cycles in 2D Grid
# https://leetcode.com/problems/detect-cycles-in-2d-grid/

#################### Brute Force Solution ####################

def containsCycle(self, grid: List[List[str]]) -> bool:
    rows = len(grid)
    cols = len(grid[0])
    visitedGlobal = set()
    # returns list of neighbors with same value as input
    def getNeighbors(row, col):
        return [(i, j) for i, j in [(row - 1, col),
                                    (row + 1, col),
                                    (row, col - 1),
                                    (row, col + 1)]
                if 0 <= i < rows and 0 <= j < cols
                and grid[i][j] == grid[row][col]]
    def dfs(row, col, value, prev, visitedLocal):
        # if cell in already visited locally, then there is cycle
        if (row, col) in visitedLocal:
            return True
        # add cell to local and global if not seen locally
        visitedLocal.add((row, col))
        visitedGlobal.add((row, col))
        # continue visiting neighbors on local visit
        # until we complete cycle or run out of neighbors to check
        for i, j in getNeighbors(row, col):
            # if the only neighbor we have is the previously visited cell, no cycle
            if not prev or prev != (i, j):
                if dfs(i, j, value, (row, col), visitedLocal):
                    return True
        return False
    # run dfs globally until we find valid cycle or run out of cells
    for r in range(rows):
        for c in range(cols):
            # if not visited globally, start local visit
            if (r, c) not in visitedGlobal:
                visitedLocal = set()
                if dfs(r, c, grid[r][c], None, visitedLocal):
                    return True
    return False