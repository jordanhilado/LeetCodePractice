# 1011. Capacity To Ship Packages Within D Days
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

def shipWithinDays(self, weights: List[int], days: int) -> int:
    def possible(capacity):
        daysCount = 1
        curr = 0
        for i in weights:
            curr += i
            if curr > capacity:
                daysCount += 1
                curr = i
        return daysCount <= days
    l = max(weights)
    r = sum(weights)
    while l < r:
        m = l + (r - l) // 2
        if possible(m):
            r = m
        else:
            l = m + 1
    return r