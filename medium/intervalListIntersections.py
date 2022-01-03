# 986. Interval List Intersections
# https://leetcode.com/problems/interval-list-intersections/

def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    i, j, ans = 0, 0, []
    while i < len(firstList) and j < len(secondList):
        aStart, aEnd = firstList[i]
        bStart, bEnd = secondList[j]
        if aStart <= bEnd and bStart <= aEnd:
            ans.append([max(aStart, bStart), min(aEnd, bEnd)])
        if aEnd <= bEnd:
            i += 1
        else:
            j += 1
    return ans