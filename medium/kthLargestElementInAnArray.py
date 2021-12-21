# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

#################### BRUTE FORCE SOLUTION ####################
def findKthLargest(self, nums: List[int], k: int) -> int:
    ctr = 0
    nums.sort()
    n = nums[::-1]
    for i in n:
        ctr += 1
        if ctr == k:
            return i

#################### HEAP SOLUTION ####################
def findKthLargest(self, nums: List[int], k: int) -> int:
    heap = []
    for ele in nums:
        heapq.heappush(heap, ele)
        if len(heap) > k:
            heapq.heappop(heap)
    return heapq.heappop(heap)