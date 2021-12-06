# 90. Subsets II
# https://leetcode.com/problems/subsets-ii/

def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    ans = [[]]
    nums.sort()
    return self.backtrack(0, nums, ans, [])
    
def backtrack(self, start, nums, ans, tmp):
    if start == len(nums):
        return
    for i in range(len(nums)):
        tmp.append(nums[i])
        if tmp not in ans:
            ans.append(tmp.copy())
            self.backtrack(start, nums[i+1:], ans, tmp)
        tmp.pop()
    return ans