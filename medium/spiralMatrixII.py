# 59. Spiral Matrix II
# https://leetcode.com/problems/spiral-matrix-ii/

def generateMatrix(self, n: int) -> List[List[int]]:
    matrix = []
    if not n: return matrix
    matrix = [[0] * n for i in range(n)]
    # construct matrix of zeros
    # layer by layer strategy
    num, top, right, down, left = 1, 0, n - 1, n - 1, 0
    while left <= right and top <= down:
        # left to right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        # top to down
        for i in range(top, down + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        # bottom row
        for i in range(right, left - 1, -1):
            matrix[down][i] = num
            num += 1
        # down to top
        down -= 1
        for i in range(down, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    return matrix