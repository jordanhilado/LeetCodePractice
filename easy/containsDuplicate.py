# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Discussion Post: https://leetcode.com/problems/contains-duplicate/discuss/1698064/5-Different-Approaches-w-Explanations

#################### Brute Force - TLE ####################

def containsDuplicate(self, nums: List[int]) -> bool:
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] == nums[j]: return True
    return False

#################### Pythonic - Using Counter Function ####################

def containsDuplicate(self, nums: List[int]) -> bool:
    freq = Counter(nums)
    for num, freq in freq.items():
        if freq > 1:
            return True
    return False

#################### Not Using Counter Function ####################

def containsDuplicate(self, nums: List[int]) -> bool:
    counter = {}
    for num in nums:
        if num not in counter:
            counter[num] = 0
        counter[num] += 1
    for num, freq in counter.items():
        if freq > 1:
            return True
    return False

#################### One-liner Solutions ####################

def containsDuplicate(self, nums: List[int]) -> bool:
    return False if len(set(nums)) == len(nums) else True

def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)

#################### Sorting Solution ####################

def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]: return True
    return False