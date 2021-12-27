# 769. Max Chunks To Make Sorted
# https://leetcode.com/problems/max-chunks-to-make-sorted/

def maxChunksToSorted(self, arr: List[int]) -> int:
    max_so_far = arr[0]
    count = 0
    for i in range(len(arr)):
        if max_so_far<arr[i]:
            max_so_far = arr[i]
        if max_so_far == i:
            count+=1
    return count