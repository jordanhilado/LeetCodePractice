# 310. Minimum Height Trees
# https://leetcode.com/problems/minimum-height-trees/

def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    if n <= 2:
        return [x for x in range(n)]
    neighbors = [set() for x in range(n)]
    for start, end in edges:
        neighbors[start].add(end)
        neighbors[end].add(start)
    leaves = []
    for i in range(n):
        if len(neighbors[i]) == 1:
            leaves.append(i)
    remain = n
    while remain > 2:
        remain -= len(leaves)
        temp = []
        for leaf in leaves:
            for neighbor in neighbors[leaf]:
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    temp.append(neighbor)
        leaves = temp
    return leaves