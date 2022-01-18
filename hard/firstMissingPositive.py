# 41. First Missing Positive
# https://leetcode.com/problems/first-missing-positive/

def firstMissingPositive(self, nums: List[int]) -> int:
    # eliminate negative numbers and 0's
    for i, num in enumerate(nums):
        if num <= 0:
            nums[i] = 0
    for i, num in enumerate(nums):
        index = abs(num) - 1
        if index >= 0 and index < len(nums):
            if nums[index] == 0:
                nums[index] = -inf
            elif nums[index] > 0:
                nums[index] *= -1
    for index, num in enumerate(nums):
        if num >= 0:
            return index + 1
    return len(nums) + 1