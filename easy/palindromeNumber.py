# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/

def isPalindrome(self, x: int) -> bool:
    n = str(x)
    if n[::-1] == str(x):
        return True
    else:
        return False