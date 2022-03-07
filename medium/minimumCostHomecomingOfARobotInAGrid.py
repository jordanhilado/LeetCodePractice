# 2087. Minimum Cost Homecoming of a Robot in a Grid
# https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
    def getRange(left, right, arr):
        if left > right:
            right, left = left, right
        return sum((arr[i] for i in range(left, right + 1)))
    totalRowCost = getRange(startPos[0], homePos[0], rowCosts)
    totalColCost = getRange(startPos[1], homePos[1], colCosts)
    return totalRowCost + totalColCost - rowCosts[startPos[0]] - colCosts[startPos[1]]