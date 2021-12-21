# 451. Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/

def frequencySort(self, s: str) -> str:
    s = Counter(s)
    heap = [(-value, key) for key, value in s.items()]
    heapq.heapify(heap)
    ans = []
    while heap:
        curr = heapq.heappop(heap)
        for _ in range(-curr[0]):
            ans.append(curr[1])
    return "".join(ans)