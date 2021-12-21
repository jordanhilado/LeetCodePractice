# 1822. Sign of the Product of an Array
# https://leetcode.com/problems/sign-of-the-product-of-an-array/

def arraySign(self, nums: List[int]) -> int:
    if 0 in nums:
        return 0
    n, cnt = len(nums), 0
    nums.sort()
    for i in nums:
        if i < 0:
            cnt += 1
    if cnt == 0 or cnt % 2 == 0:
        return 1
    else:
        return -1