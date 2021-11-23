# 674. Longest Continuous Increasing Subsequence
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

def findLengthOfLCIS(self, nums: List[int]) -> int:
    if nums == None:
        return 0
    c = 1
    m = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            c += 1
        else:
            c = 1
        m = max(m, c)
    return m