# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/

def rob(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    def check(nums):
        i, e = 0, 0
        for j in nums:
            if e > i:
                new_e = e
            else:
                new_e = i
            i = e + j
            e = new_e
        if e > i:
            return e
        else:
            return i
    return max(check(nums[:len(nums) - 1]), check(nums[1:]))