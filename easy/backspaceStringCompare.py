# 844. Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/

def backspaceCompare(self, s: str, t: str) -> bool:
    def compare(string):
        stack = []
        for i in string:
            if i != "#":
                stack.append(i)
            else:
                if len(stack) != 0:
                    stack.pop()
        return stack
    return compare(s) == compare(t)