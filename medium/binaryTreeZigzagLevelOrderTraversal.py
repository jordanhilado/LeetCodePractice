# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []
    q = collections.deque([root])
    ans = []
    rightToLeft = False
    while q:
        n = len(q)
        level = []
        for _ in range(n):
            curr = q.popleft()
            level.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        if rightToLeft:
            ans.append(level[::-1])
        else:
            ans.append(level)
        rightToLeft = not rightToLeft
    return ans