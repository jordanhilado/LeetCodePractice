# 172. Factorial Trailing Zeroes
# https://leetcode.com/problems/factorial-trailing-zeroes/

def trailingZeroes(self, n: int) -> int:
    start = 0
    while n > 0:
        n //= 5
        start += n
    return start