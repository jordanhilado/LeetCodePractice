# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/

def longestOnes(self, nums: List[int], k: int) -> int:
    l, n, ans = 0, len(nums), 0
    for r in range(n):
        if nums[r] == 0:
            if k == 0:
                while nums[l] != 0:
                    l += 1
                l += 1
            else:
                k -= 1
        ans = max(ans, r - l + 1)
    return ans