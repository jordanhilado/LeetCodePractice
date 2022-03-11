# 260. Single Number III
# https://leetcode.com/problems/single-number-iii/

def singleNumber(self, nums: List[int]) -> List[int]:
    ans = []
    s = Counter(nums)
    for key, val in s.items():
        if val == 1:
            ans.append(key)
    return ans