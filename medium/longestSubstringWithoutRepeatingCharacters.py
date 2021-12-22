# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

#################### BRUTE FORCE SOLUTION ####################

def lengthOfLongestSubstring(self, s: str) -> int:
    if s == "":
        return 0
    if len(s) == 1:
        return 1
    if len(s) == 2 and s[0] != s[1]:
        return 2
    ans = []
    for j in range(len(s)):
        l = []
        for i in range(j, len(s)):
            if s[i] in l:
                ans.append(len(l))
                break
            l.append(s[i])
            if i == len(s) - 1:
                ans.append(len(l))
    print(ans)
    return max(ans)

#################### SLIDING WINDOW SOLUTION ####################

def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        ans = 0
        for r in range(len(s)):
            if s[r] not in seen:
                ans = max(ans, r - l + 1)
            else:
                if seen[s[r]] < l:
                    ans = max(ans, r - l + 1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return ans