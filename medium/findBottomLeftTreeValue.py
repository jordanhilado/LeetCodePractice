# 513. Find Bottom Left Tree Value
# https://leetcode.com/problems/find-bottom-left-tree-value/

def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    ans = 0
    if not root: return 0
    q = [(root, )]
    while q:
        level = []
        curr = q.pop()
        for node in curr:
            ans = node.val
            if node.right: level.append(node.right)
            if node.left: level.append(node.left)
        if level:
            q.append(level)
    return ans