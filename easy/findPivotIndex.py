# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/

def pivotIndex(self, nums: List[int]) -> int:
    leftTotal, rightTotal = 0, sum(nums)
    for index, num in enumerate(nums):
        rightTotal -= num
        if leftTotal == rightTotal:
            return index
        leftTotal += num
    return -1