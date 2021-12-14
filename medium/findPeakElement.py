# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/

def findPeakElement(self, nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m + 1] > nums[m]:
            l = m + 1
        else:
            r = m
    return l