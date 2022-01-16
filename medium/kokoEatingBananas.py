# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/

#################### Without Helper Function ####################

def minEatingSpeed(self, piles: List[int], h: int) -> int:
    if len(piles) == h:
        return max(piles)
    l, r = 1, max(piles)
    while l < r:
        m = l + (r - l) // 2
        hoursNeeded = 0
        for pile in piles:
            if pile < m:
                hoursNeeded += 1
            else:
                hoursNeeded += math.ceil(pile / m)
        if hoursNeeded <= h:
            r = m
        else:
            l = m + 1
    return l

#################### With Helper Function ####################

def minEatingSpeed(self, piles: List[int], h: int) -> int:
    def canFinish(k):
        hoursNeeded = 0
        for pile in piles:
            # cumulative sum
            hoursNeeded += ceil(pile / k)
        return hoursNeeded <= h
    # taking k b/w the range of 1, max(piles)
    l, r = 1, max(piles)
    while l < r:
        mid = l + (r - l) // 2
        if canFinish(mid):
            r = mid
        else:
            l = mid + 1
    return r