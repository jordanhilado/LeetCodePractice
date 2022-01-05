# 1161. Maximum Level Sum of a Binary Tree
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    ans, q = [], [root]
    while q:
        qLen, level = len(q), []
        for i in range(qLen):
            curr = q.pop(0)
            level.append(curr.val)
            if curr.left is not None: q.append(curr.left)
            if curr.right is not None: q.append(curr.right)
        ans.append(sum(level))
    return ans.index(max(ans)) + 1