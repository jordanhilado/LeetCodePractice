# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/

#################### Binary Search Solution ####################

def findDuplicate(self, nums: List[int]) -> int:
    nums.sort()
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] < m + 1:
            r = m - 1
        else:
            l = m + 1
    return l

#################### Counter Solution ####################

def findDuplicate(self, nums: List[int]) -> int:
    c = Counter(nums)
    for item, freq in c.items():
        if freq > 1:
            return item