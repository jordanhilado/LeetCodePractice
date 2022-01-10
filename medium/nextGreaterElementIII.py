# 556. Next Greater Element III
# https://leetcode.com/problems/next-greater-element-iii/

def nextGreaterElement(self, n: int) -> int:
    # getting each digit
    nums = list(map(int, str(n)))
    # check to see if nums are in descending order
    idx = len(nums) - 2
    while idx >= 0 and nums[idx] >= nums[idx + 1]:
        idx -= 1
    if idx == -1:
        return -1
    # index of the value after idx which is less than idx's value
    idx2 = len(nums) - 1
    while nums[idx2] <= nums[idx]:
        idx2 -= 1
    # swapping and reversing
    nums[idx], nums[idx2] = nums[idx2], nums[idx]
    nums[idx + 1:] = reversed(nums[idx + 1:])
    # return the value
    res = ""
    for num in nums:
        res += str(num)
    res = int(res)
    return res if res < 2**31 else -1