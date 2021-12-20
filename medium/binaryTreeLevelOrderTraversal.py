# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return None
    q = [root]
    ans = []
    while q:
        qLen = len(q)
        level = []
        for _ in range(qLen):
            curr = q.pop(0)
            level.append(curr.val)
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        ans.append(level)
    return ans