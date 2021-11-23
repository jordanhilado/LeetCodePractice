# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/

def reverseBits(self, n: int) -> int:
    num = '{:032b}'.format(n)
    rev = num[::-1]
    return int(rev, 2)