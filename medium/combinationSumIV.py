# 377. Combination Sum IV
# https://leetcode.com/problems/combination-sum-iv/

def combinationSum4(self, nums: List[int], target: int) -> int:
    N = nums
    T = target
    dp = [0] * (T + 1)
    dp[0] = 1
    for i in range(T):
        if not dp[i]: continue
        for num in N:
            if num + i <= T: dp[i+num] += dp[i]
    return dp[T]