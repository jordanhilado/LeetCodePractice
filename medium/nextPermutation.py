# 31. Next Permutation
# https://leetcode.com/problems/next-permutation/

def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # find start of strictly decreasing section
    i = j = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    # if the start of the strictly decreasing section is the start,
    # then that means it is the last permutation
    if i == 0:
        nums.reverse()
        return
    # set last ascending position
    k = i - 1
    # find num in the strictly decreasing section that is next after
    # the last number in the ascending section
    while nums[j] <= nums[k]:
        j -= 1
    # swap the two and reverse
    nums[k], nums[j] = nums[j], nums[k]
    nums[k + 1:] = nums[k + 1:][::-1]