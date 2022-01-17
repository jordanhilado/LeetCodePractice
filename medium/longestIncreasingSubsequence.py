# https://leetcode.com/problems/longest-increasing-subsequence/
# 300. Longest Increasing Subsequence

#################### Dynamic Programming ####################

def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)

#################### Binary Search ####################

def lengthOfLIS(self, nums: List[int]) -> int:
    temp = [nums[0]]
    for n in nums:
        x = bisect_left(temp, n)
        if x == len(temp):
            temp.append(n)
        elif temp[x] > n:
            temp[x] = n
    return len(temp)