# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/

def subarraySum(self, nums: List[int], k: int) -> int:
    # need to account for 0 to also count k - 0
    count, sums, d, d[0] = 0, 0, {}, 1
    # loop through array to count the running count and sum
    for i in range(len(nums)):
        sums += nums[i]
        count += d.get(sums - k, 0)
        d[sums] = d.get(sums, 0) + 1
    return count