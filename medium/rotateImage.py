# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/

def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    mLen = len(matrix)
    for i in range(mLen):
        for j in range(i, mLen):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[i].reverse()