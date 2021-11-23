# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

def lengthOfLastWord(self, s: str) -> int:
    n = s.split()
    if n:
        return len(n[-1])
    return 0