# 1338. Reduce Array Size to The Half
# https://leetcode.com/problems/reduce-array-size-to-the-half/

def minSetSize(self, arr: List[int]) -> int:
    freqs = Counter(arr)
    valArr = sorted(freqs.values())[::-1]
    n, i, ctr = len(arr), 0, 0
    while ctr < n // 2:
        ctr += valArr[i]
        i += 1
    return i