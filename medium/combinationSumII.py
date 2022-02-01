# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/

#################### Backtracking Solution ####################

def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    def dfs(nums, target, index, path, ans):
        if target <= 0:
            if target == 0:
                ans.append(path)
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            dfs(nums, target - nums[i], i + 1, path + [nums[i]], ans)
    ans = []
    dfs(sorted(candidates), target, 0, [], ans)
    return ans

#################### DP Solution ####################

def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    table = [None] + [set() for i in range(target)]
    for i in candidates:
        if i > target:
            break
        for j in range(target - i, 0, -1):
            table[i + j] |= {elt + (i,) for elt in table[j]}
        table[i].add((i,))
    return map(list, table[target])