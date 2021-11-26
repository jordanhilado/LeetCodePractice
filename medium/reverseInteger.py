# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/

def reverse(self, x: int) -> int:
    temp = list(str(abs(x)))
    temp.reverse()
    ans = int(''.join(temp))
    if abs(ans) > 2**31 - 1:
        return 0
    else:
        if x > 0:
            return ans
        else:
            return -ans