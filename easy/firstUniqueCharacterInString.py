# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/

def firstUniqChar(self, s: str) -> int:
    s = list(s)
    c = Counter(s)
    ans = None
    for char, freq in c.items():
        if freq == 1:
            if ans == None:
                ans = s.index(char)
            else:
                ans = min(ans, s.index(char))
    return ans if ans is not None else -1