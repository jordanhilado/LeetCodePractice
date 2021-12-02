# 2022. Convert 1D Array Into 2D Array
# https://leetcode.com/problems/convert-1d-array-into-2d-array/

def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
    if m * n != len(original):
        return []
    ans = []
    l = 0
    r = n
    for i in range(m):
        ans.append(original[l:r])
        l += n
        r += n
    return ans