# 136. Single Number
# https://leetcode.com/problems/single-number/

def singleNumber(self, nums: List[int]) -> int:
    ans = []
    for i in range(len(nums)):
        if nums[i] not in ans:
            ans.append(nums[i])
        else:
            ans.remove(nums[i])
    return ans[0]