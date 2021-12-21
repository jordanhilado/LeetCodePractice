# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/

def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    def distance(x, y):
        return sqrt((x - 0)**2 + (y - 0)**2)
    heap = [(distance(x, y), [x, y]) for x, y in points]
    heapq.heapify(heap)
    ans = []
    for _ in range(k):
        curr = heapq.heappop(heap)
        ans.append(curr[1])
    return ans