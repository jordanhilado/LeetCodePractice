# 1. Two Sum
# https://leetcode.com/problems/two-sum/

#################### Brute-force Solution ####################

def twoSum(self, nums: List[int], target: int) -> List[int]:
    for left in range(len(nums)):
        for right in range(left + 1, len(nums)):
            if nums[left] + nums[right] == target:
                return [left, right]

#################### Hashmap Solution ####################

def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = {}
    for i, n in enumerate(nums): 
        if n in dic:
            return [dic[n], i]
        dic[target-n] = i