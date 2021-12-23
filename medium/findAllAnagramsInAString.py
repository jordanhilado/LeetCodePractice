# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

#################### HASHMAP SOLUTION ####################

def findAnagrams(self, s: str, p: str) -> List[int]:
    if len(p) > len(s): return []
    pCount, sCount = {}, {}
    for i in range(len(p)):
        pCount[p[i]] = 1 + pCount.get(p[i], 0)
        sCount[s[i]] = 1 + sCount.get(s[i], 0)
    res = [0] if sCount == pCount else []
    l = 0
    for r in range(len(p), len(s)):
        sCount[s[r]] = 1 + sCount.get(s[r], 0)
        sCount[s[l]] -= 1
        if sCount[s[l]] == 0:
            sCount.pop(s[l])
        l += 1
        if sCount == pCount:
            res.append(l)
    return res

#################### BRUTE FORCE SOLUTION ####################

def findAnagrams(self, s: str, p: str) -> List[int]:
    sLen, pLen, freq, ans, window = len(s), len(p), Counter(p), [], None
    for i in range(sLen - pLen + 1):
        if i == 0:
            # initialize window with a beginning of s => length = length of anagram letters
            window = Counter(s[:pLen])
        else:
            # move window right; 1. remove char on left, add char on right
            window[s[i - 1]] -= 1
            window[s[i + pLen - 1]] += 1
        if len(window - freq) == 0:
            ans.append(i)
    return ans