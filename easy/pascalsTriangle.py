# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/

def generate(self, numRows: int) -> List[List[int]]:
    res = [[1]]
    for i in range(numRows - 1):
        temp = [0] + res[-1] + [0]
        curr = []
        for j in range(len(res[-1]) + 1):
            curr.append(temp[j] + temp[j+1])
        res.append(curr)
    return res