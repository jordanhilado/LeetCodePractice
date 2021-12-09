# 378. Kth Smallest Element in a Sorted Matrix
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    if k == 1:
        return matrix[0][0]
    l = []
    heapq.heapify(l)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            curr = matrix[i][j]
            heapq.heappush(l, matrix[i][j])
    for i in range(k-1):
        heapq.heappop(l)
    return l[0]