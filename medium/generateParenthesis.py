# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

def generateParenthesis(self, n: int) -> List[str]:
    ans = []
    def dfs(total, left, right, curr):
        if total < 0 or left < 0 or right < 0:
            return
        if left == 0 and right == 0:
            ans.append(curr)
        dfs(total + 1, left - 1, right, curr + "(")
        dfs(total - 1, left, right - 1, curr + ")")
    dfs(0, n, n, '')
    return ans