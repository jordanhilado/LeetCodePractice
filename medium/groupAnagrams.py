# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    if len(strs) == 0:
        return [[""]]
    ans = {}
    for word in strs:
        temp = ''.join(sorted(word))
        if temp in ans:
            ans[temp].append(word)
        else:
            ans[temp] = [word]
    return ans.values()