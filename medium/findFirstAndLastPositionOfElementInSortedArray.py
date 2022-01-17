# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def searchRange(self, nums: List[int], target: int) -> List[int]:
    def findLeft(arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l
    def findRight(arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] <= target:
                l = m + 1
            else:
                r = m - 1
        return r
    low, high = findLeft(nums, target), findRight(nums, target)
    return (low, high) if low <= high else [-1, -1]