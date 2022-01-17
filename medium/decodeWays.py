# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/

def numDecodings(self, s: str) -> int:
    if not s or s[0] == '0':
        return 0
    dp = [1, 1]
    for i in range(1, len(s)):
        temp = 0
        if 1 <= int(s[i]) <= 9:
            temp = dp[1]
        if 10 <= int(s[i - 1:i + 1]) <= 26:
            temp += dp[0]
        dp = [dp[1], temp]
    return dp[1]