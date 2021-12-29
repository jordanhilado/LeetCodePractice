# 318. Maximum Product of Word Lengths
# https://leetcode.com/problems/maximum-product-of-word-lengths/submissions/

def maxProduct(self, words: List[str]) -> int:
    ans = 0
    for i in words:
        for j in words:
            if not set(i) & set(j):
                curr = len(i) * len(j)
                if curr > ans:
                    ans = curr
    return ans