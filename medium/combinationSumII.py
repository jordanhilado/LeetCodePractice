# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/

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