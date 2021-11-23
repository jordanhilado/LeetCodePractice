# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

def isPalindrome(self, s: str) -> bool:
    ans = ""
    temp = ""
    for i in s:
        if i.isalpha() == True or i.isdigit() == True:
            ans += i.lower()
    for k in range(len(ans) - 1, -1, -1):
        temp += ans[k]
    if temp == ans:
        return True
    return False