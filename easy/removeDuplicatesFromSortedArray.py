# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array

def removeDuplicates(self, nums: List[int]) -> int:
    l = 1
    for r in range(1, len(nums)):
        # new unique value
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1
    return l