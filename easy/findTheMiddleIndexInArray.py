# 1991. Find the Middle Index in Array
# https://leetcode.com/problems/find-the-middle-index-in-array/

def findMiddleIndex(self, nums: List[int]) -> int:
    leftTotal, rightTotal = 0, sum(nums)
    for index, num in enumerate(nums):
        rightTotal -= num
        if leftTotal == rightTotal:
            return index
        leftTotal += num
    return -1