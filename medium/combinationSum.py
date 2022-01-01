# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    ans = []
    def dfs(target, index, path):
        if target < 0:
            return
        if target == 0:
            ans.append(path)
            return
        for i in range(index, len(candidates)):
            dfs(target - candidates[i], i, path + [candidates[i]])
    dfs(target, 0, [])
    return ans