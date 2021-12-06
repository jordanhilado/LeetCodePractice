# Permutations II
# https://leetcode.com/problems/permutations-ii/

def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    res = []
    perm = []
    count = { n:0 for n in nums }
    for n in nums:
        count[n] += 1
    def dfs():
        if len(perm) == len(nums):
            res.append(perm.copy()) # we make changes to perm
            return
        for n in count: # no duplicates
            if count[n] > 0: # enough values left
                perm.append(n)
                count[n] -= 1
                dfs()
                count[n] += 1
                perm.pop()
    dfs()
    return res 