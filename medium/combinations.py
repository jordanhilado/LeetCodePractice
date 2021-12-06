# 77. Combinations
# https://leetcode.com/problems/combinations/

def combine(self, n: int, k: int) -> List[List[int]]:
    ans = []
    
    def backtrack(remain, comb, nex):
        if remain == 0:
            ans.append(comb.copy())
        else:
            for i in range(nex, n+1):
                comb.append(i)
                backtrack(remain-1, comb, i+1)
                comb.pop()
    backtrack(k, [], 1)
    return ans