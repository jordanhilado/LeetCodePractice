# 692. Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/

def topKFrequent(self, words: List[str], k: int) -> List[str]:
    table = {}
    for word in words:
        if word in table:
            table[word] += 1
        else:
            table[word] = 1
    # set up a max heap
    heap = []
    heapq.heapify(heap)
    for key in table:
        heapq.heappush(heap, (-table[key], key))
    # pop top k
    res = []
    for i in range(k):
        popped = heapq.heappop(heap)
        res.append(popped)
    # sort res alphabetically
    res.sort()
    newres = []
    for word in res:
        newres.append(word[1])
        print(newres)
    return newres