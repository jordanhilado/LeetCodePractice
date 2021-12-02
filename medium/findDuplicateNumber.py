# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/

def findDuplicate(self, nums: List[int]) -> int:
    count = [0] * (len(nums)+1)
    print(count)
    for val in nums:
        count[val] = count[val] + 1
    print(count)
    for i in range(len(count)):
        if count[i] > 1:
            return i