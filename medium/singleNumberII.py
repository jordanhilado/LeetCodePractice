# 137. Single Number II
# https://leetcode.com/problems/single-number-ii/

def singleNumber(self, nums: List[int]) -> int:
    s = Counter(nums)
    for key, val in s.items():
        if val == 1:
            return key