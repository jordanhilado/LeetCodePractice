# 784. Letter Case Permutation
# https://leetcode.com/problems/letter-case-permutation/

def letterCasePermutation(self, s: str) -> List[str]:
    ans = [""]
    
    for i in s:
        temp = []
        if i.isalpha():
            for j in ans:
                temp.append(j + i.upper())
                temp.append(j + i.lower())
        else:
            for j in ans:
                temp.append(j + i)
        ans = temp
        print(ans)
    return ans