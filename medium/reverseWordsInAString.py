# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/

def reverseWords(self, s: str) -> str:
    l, ans = s.split(" "), ""
    l.reverse()
    for i in range(len(l)):
        if l[i] != "":
            ans += l[i]
            ans += " "
    return ans.strip()