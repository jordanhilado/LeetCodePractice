# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    l = Counter(nums)
    heap = [(-value, key) for key, value in l.items()]
    heapq.heapify(heap)
    ans = []
    for _ in range(k):
        curr = heapq.heappop(heap)
        ans.append(curr[1])
    return ans