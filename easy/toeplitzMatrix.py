# 766. Toeplitz Matrix
# https://leetcode.com/problems/toeplitz-matrix/

def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    n = len(matrix)
    for row in range(n):
        for col in range(len(matrix[row])):
            if row > 0 and col > 0 and matrix[row][col] != matrix[row - 1][col - 1]:
                return False
    return True