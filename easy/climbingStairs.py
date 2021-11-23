# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

def climbStairs(self, n: int) -> int:
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        n += 1
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b