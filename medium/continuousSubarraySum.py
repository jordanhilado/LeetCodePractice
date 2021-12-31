# 523. Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/

def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    d, d[0], sums = {}, -1, 0
    for i in range(len(nums)):
        sums += nums[i]
        if k != 0:
            sums = sums % k
        if sums in d:
            if i - d[sums] > 1:
                return True
        else:
            d[sums] = i
    return False