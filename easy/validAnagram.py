# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

#################### With collections.Counter ####################

def isAnagram(self, s: str, t: str) -> bool:
    return True if Counter(s) == Counter(t) else False

#################### Without collections.Counter ####################

def isAnagram(self, s: str, t: str) -> bool:
    def counter(st):
        d = {}
        for i in st:
            if i not in d:
                d[i] = 0
            d[i] += 1
        return d
    return True if counter(s) == counter(t) else False