# 791. Custom Sort String
# https://leetcode.com/problems/custom-sort-string/

def customSortString(self, order: str, s: str) -> str:
    ans = ""
    for i in order:
        for _ in range(s.count(i)):
            ans += i
    for j in s:
        if j not in order:
            ans += j
    return ans