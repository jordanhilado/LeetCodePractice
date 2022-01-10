# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/

def characterReplacement(self, s: str, k: int) -> int:
    l = 0
    freq = {}
    ans = 0
    for r in range(len(s)):
        # set frequencies
        if not s[r] in freq:
            freq[s[r]] = 0
        freq[s[r]] += 1
        # calculate replacement cost: # of cells b/t left and right
        count = r - l + 1
        if count - max(freq.values()) <= k:
            ans = max(ans, count)
        else:
            freq[s[l]] -= 1
            if not freq[s[l]]:
                freq.pop(s[l])
            l += 1
    return ans