# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/

def myAtoi(self, s: str) -> int:
    MAX_INT = 2 ** 31 - 1
    MIN_INT = -2 ** 31
    i = res = 0
    negative = 1
    # whitespace
    while i < len(s) and s[i] == ' ':
        i += 1
    # +/- symbol
    if i < len(s) and s[i] == '-':
        i += 1
        negative = -1
    elif i < len(s) and s[i] == '+':
        i += 1
    # check 0-9
    checker = set('0123456789')
    while i < len(s) and s[i] in checker:
        res = res * 10 + int(s[i])
        i += 1
    # check boundaries
    res = res * negative
    if res < 0:
        return max(res, MIN_INT)
    return min(res, MAX_INT)