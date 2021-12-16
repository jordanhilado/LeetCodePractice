# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

def maxArea(self, height: List[int]) -> int:
    size = len(height)
    l, r, maxW = 0, size - 1, size - 1
    ans = 0
    for width in range(maxW, 0, -1):
        if height[l] < height[r]:
            ans = max(ans, width * height[l])
            l += 1
        else:
            ans = max(ans, width * height[r])
            r -= 1
        print("j")
    return ans