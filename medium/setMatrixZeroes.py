# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/

def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    mLen = len(matrix)
    r, c = set(), set()
    for row in range(mLen):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                r.add(row), c.add(col)
    for row in range(mLen):
        for col in range(len(matrix[row])):
            if row in r or col in c:
                matrix[row][col] = 0