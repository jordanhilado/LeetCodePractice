# 67. Add Binary
# https://leetcode.com/problems/add-binary/

def addBinary(self, a: str, b: str) -> str:
    num1 = int(a, 2)
    num2 = int(b, 2)
    total = num1 + num2
    return format(total, "b")