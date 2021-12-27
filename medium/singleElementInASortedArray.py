# 540. Single Element in a Sorted Array
# https://leetcode.com/problems/single-element-in-a-sorted-array/

def singleNonDuplicate(self, nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] == nums[m - 1]:
            if (m - 1) % 2 != 0:
                r = m - 1
            else:
                l = m + 1
        elif nums[m] == nums[m + 1]:
            if m % 2 != 0:
                r = m - 1
            else:
                l = m + 1
        else:
            return nums[m]
    return nums[l]