# 198. House Robber
# https://leetcode.com/problems/house-robber/

def rob(self, nums: List[int]) -> int:
    i, e = 0, 0
    for j in nums:
        if e > i:
            new_e = e
        else:
            new_e = i
        i = e + j
        e = new_e
    if e > i:
        return e
    else:
        return i