# 240. Search a 2D Matrix II
# https://leetcode.com/problems/search-a-2d-matrix-ii/

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    for row in range(len(matrix)):
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            nums = matrix[row]
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
    return False