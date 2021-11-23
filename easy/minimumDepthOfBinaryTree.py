# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

def minDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    if root.left == None:
        return 1 + self.minDepth(root.right)
    if root.right == None:
        return 1 + self.minDepth(root.left)
    return 1 + min(self.minDepth(root.left), self.minDepth(root.right))