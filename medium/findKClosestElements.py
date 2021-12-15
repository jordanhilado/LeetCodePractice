# 658. Find K Closest Elements
# https://leetcode.com/problems/find-k-closest-elements/

def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    left, right = 0, len(arr) - k
    while left < right:
        mid = (left + right) // 2
        midVal = arr[mid]
        print(left, mid, right)
        if x - arr[mid+k] <= midVal - x:
            right = mid
        else:
            left = mid + 1
    return arr[left:left+k]