# 169. Majority Element
# https://leetcode.com/problems/majority-element/

def majorityElement(self, nums: List[int]) -> int:
    return sorted(nums)[len(nums)//2]