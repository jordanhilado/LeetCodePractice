# 452. Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

def findMinArrowShots(self, points: List[List[int]]) -> int:
    # sort according to the end value
    points, ctr, ptr = sorted(points, key = lambda x: x[1]), 0, float('-inf')
    for baloon in points:
        if baloon[0] > ptr:
            ctr += 1
            ptr = baloon[1]
    return ctr