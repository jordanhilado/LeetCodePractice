# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/

def findDuplicates(self, nums: List[int]) -> List[int]:
    ans = []
    count = [0] * (len(nums)+1)
    for val in nums:
        count[val] = count[val] + 1
    for i in range(len(count)):
        if count[i] > 1:
            ans.append(i)
    return ans