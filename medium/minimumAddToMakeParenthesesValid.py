# 921. Minimum Add to Make Parentheses Valid
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

#################### SOLUTION 1: Based off of Minimum Remove to Make Parentheses Valid ####################

def minAddToMakeValid(self, s: str) -> int:
    s = list(s)
    stack, count = [], 0
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''
                count += 1
    while stack:
        s[stack.pop()] = ''
        count += 1
    return count

#################### SOLUTION 2: No stack ####################

def minAddToMakeValid(self, s: str) -> int:
    o, c = 0, 0
    for i in s:
        if i == '(':
            o += 1
        else:
            if o:
                o -= 1
            else:
                c += 1
    return o + c

#################### SOLUTION 3: With stack ####################

def minAddToMakeValid(self, s: str) -> int:
    stack = []
    for ch in s:
        if ch == '(': stack.append(ch)
        else:
            if len(stack) and stack[-1] == '(': stack.pop()
            else: stack.append(ch)
    return len(stack)