# 15. 3Sum
# https://leetcode.com/problems/3sum/

def threeSum(self, nums: List[int]) -> List[List[int]]:
    s = set()
    nums.sort()
    n = len(nums)
    for i in range(n):
        l = i + 1
        r = n - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == 0:
                s.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
            elif total > 0:
                r -= 1
            else:
                l += 1
    return [list(i) for i in s]