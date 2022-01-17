# 139. Word Break
# https://leetcode.com/problems/word-break/

def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(len(s)):
        for j in range(i, len(s)):
            if dp[i] and s[i:j + 1] in wordDict:
                dp[j + 1] = True
    print(dp)
    return dp[-1]