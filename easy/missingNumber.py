# 268. Missing Number
# https://leetcode.com/problems/missing-number/

def missingNumber(self, nums: List[int]) -> int:
    return sum(range(len(nums) + 1 )) - sum(nums)