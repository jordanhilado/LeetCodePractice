# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    ans = []
    while matrix:
        ans.extend(matrix.pop(0)) # left to right
        if matrix and matrix[0]: # top to dwon
            for row in matrix:
                ans.append(row.pop())
        if matrix: # right to left
            ans.extend(matrix.pop()[::-1])
        if matrix and matrix[0]: # bottom to up
            for row in matrix[::-1]:
                ans.append(row.pop(0))
    return ans