# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

def letterCombinations(self, digits: str) -> List[str]:
    vals = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return list(vals[digits[0]])
    ans = ['']
    for num in digits:
        curr = list()
        for letter in vals[num]:
            for com in ans:
                curr.append(com + letter)
        ans = curr
    return ans