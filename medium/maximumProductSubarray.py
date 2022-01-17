# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/

def maxProduct(self, nums: List[int]) -> int:
    ans = nums[0]
    curr = 1
    for num in nums:
        curr *= num
        ans = max(ans, curr)
        if curr == 0:
            curr = 1
    curr = 1
    for num in reversed(nums):
        curr *= num
        ans = max(ans, curr)
        if curr == 0:
            curr = 1
    return ans