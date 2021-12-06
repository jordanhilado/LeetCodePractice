# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

def longestConsecutive(self, nums: List[int]) -> int:
    if nums == []:
        return 0
    nums.sort()
    left, ctr, ans, nLen = 0, 1, set(), len(nums)
    for i in range(1, nLen):
        if nums[left] == nums[i]:
            left += 1
        elif nums[left] + 1 == nums[i]:
            ctr += 1
            left += 1
        elif nums[left] + 1 != nums[i]:
            ans.add(ctr)
            ctr = 1
            left += 1
    ans.add(ctr)
    return max(ans)