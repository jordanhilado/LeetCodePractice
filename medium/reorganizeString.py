# 767. Reorganize String
# https://leetcode.com/problems/reorganize-string/

def reorganizeString(self, s: str) -> str:
    # create dictionary of frequencies for each letter
    cnt = Counter(s)
    # create maxheap from dictionary
    heap = [(-value, key) for key, value in cnt.items()]
    heapq.heapify(heap)
    # create ans, which will be final return value if possible
    ans = []
    # until heap is empty
    while(len(heap)>1):
        # pop first two items
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        # add first two items to answer
        ans.extend([x[1],y[1]])
        # if the frequency of the first pop is greater than 1, push back the decremented value
        if x[0]<-1:
            heapq.heappush(heap,(x[0]+1,x[1]))
        # if the frequency of the second pop is greater than 1, push back the decremented value
        if y[0]<-1:
            heapq.heappush(heap,(y[0]+1,y[1]))
    if heap:
        if heap[0][0]<-1:
            return "" # case where last left element count is more than 2
        ans.append(heap[0][1])
    return "".join(ans)