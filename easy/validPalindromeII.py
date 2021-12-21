# 680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/

def validPalindrome(self, s: str) -> bool:
    def check(s, l, r, deleted):
        while l < r:
            if s[l] != s[r]:
                if deleted:
                    return False
                else:
                    return check(s, l + 1, r, True) or check(s, l, r - 1, True)
            else:
                l += 1
                r -= 1
        return True
    return check(s, 0, len(s) - 1, False)