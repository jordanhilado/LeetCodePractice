# 1047. Remove All Adjacent Duplicates In String
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

def removeDuplicates(self, s: str) -> str:
    s, stack, n = list(s), [], len(s)
    for i in range(n):
        if not stack or (stack and s[i] != stack[-1]):
            stack.append(s[i])
        else:
            stack.pop(-1)
    return ''.join(stack)