# 637. Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/

def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    ans, q = [], [root]
    while q:
        qlen, row = len(q), 0
        for i in range(qlen):
            curr = q.pop(0)
            row += curr.val
            if curr.left is not None: q.append(curr.left)
            if curr.right is not None: q.append(curr.right)
        ans.append(row/qlen)
    return ans