# 394. Decode String
# https://leetcode.com/problems/decode-string/

def decodeString(self, s: str) -> str:
    stack, curNum, curString = [], 0, ''
    for c in s:
        if c == '[': 
            stack.append(curString)
            stack.append(curNum)
            curString = ''
            curNum = 0
        elif c == ']':
            num = stack.pop()
            prevString = stack.pop()
            curString = prevString + num*curString
        elif c.isdigit():
            curNum = curNum * 10 + int(c) # keeps track of more than 1 digit number
        else:
            curString += c
    return curString