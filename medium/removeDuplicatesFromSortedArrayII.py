# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

def removeDuplicates(self, nums: List[int]) -> int:
    nLen = len(nums)
    if nLen < 3:
        return nLen
    pos = 1
    for i in range(1, nLen - 1):
        if nums[i - 1] != nums[i + 1]:
            nums[pos] = nums[i]
            pos += 1
    nums[pos] = nums[-1]
    return pos + 1