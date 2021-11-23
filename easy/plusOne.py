# 66. Plus One
# https://leetcode.com/problems/plus-one/

def plusOne(self, digits: List[int]) -> List[int]:
    num = ""
    ans = []
    for i in digits:
        num += str(i)
    newNum = int(num) + 1
    for k in range(len(str(newNum))):
        ans.append(str(newNum)[k])
    return ans