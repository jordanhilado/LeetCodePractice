# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/

#################### Hashmap Solution 1 ####################

def subarraySum(self, nums: List[int], k: int) -> int:
    # need to account for 0 to also count k - 0
    count, sums, d, d[0] = 0, 0, {}, 1
    # loop through array to count the running count and sum
    for i in range(len(nums)):
        sums += nums[i]
        count += d.get(sums - k, 0)
        d[sums] = d.get(sums, 0) + 1
    return count

#################### Hashmap Solution 2 ####################

def subarraySum(self, nums: List[int], k: int) -> int:
    sums = {0:1}
    count = s = 0
    for num in nums:
        s += num
        if s - k in sums:
            count += sums[s - k]
        if s in sums:
            sums[s] += 1
        else:
            sums[s] = 1
    return count