# 43. Multiply Strings
# https://leetcode.com/problems/multiply-strings/

def multiply(self, num1: str, num2: str) -> str:
    ans = 0
    firstCarry = 1
    for i in num1[::-1]:
        secondCarry = 1
        for j in num2[::-1]:
            ans += int(i) * int(j) * firstCarry * secondCarry
            secondCarry *= 10
        firstCarry *= 10
    return str(ans)