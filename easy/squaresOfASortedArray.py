# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/

def sortedSquares(self, nums: List[int]) -> List[int]:
    l = []
    for i in range(len(nums)):
        l.append(nums[i] * nums[i])
    return sorted(l)