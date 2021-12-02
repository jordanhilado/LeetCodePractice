# 15. 3Sum
# https://leetcode.com/problems/3sum/

def threeSum(self, nums: List[int]) -> List[List[int]]:
    s = set()
    nums.sort()
    nLen = len(nums)
    for i in range(nLen):
        l, r = i+1, nLen-1
        while l < r:
            total = nums[i]+nums[l]+nums[r]
            if total == 0:
                s.add((nums[i],nums[l],nums[r]))
                r -= 1
                l += 1
            elif total > 0:
                r -= 1
            else:
                l += 1
    return list(s)