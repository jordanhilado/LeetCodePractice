# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root == None:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))