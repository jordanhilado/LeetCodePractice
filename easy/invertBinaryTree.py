# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def preorder(node):
        if node is not None:
            node.left, node.right = node.right, node.left
            preorder(node.left)
            preorder(node.right)
    preorder(root)
    return root