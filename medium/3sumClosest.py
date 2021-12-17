# 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/

def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    ans = []
    for i in range(len(nums)):
        l, r = i + 1, len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == target:
                return target
            elif total < target:
                ans.append(total)
                l += 1
            elif total > target:
                ans.append(total)
                r -= 1
    temp = []
    for i in ans:
        temp.append(abs(target - i))
    return ans[temp.index(min(temp))]