# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    for row in range(len(matrix)):
        if matrix[row][0] <= target <= matrix[row][-1]:
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