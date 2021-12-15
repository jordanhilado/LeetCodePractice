# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/

def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    left, total, ans = 0, 0, len(nums) + 1
    for i in range(len(nums)):
        total += nums[i]
        while total >= target:
            ans = min(ans, i - left + 1)
            total -= nums[left]
            left += 1
    return ans if ans <= len(nums) else 0