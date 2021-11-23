# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    stack, res = [], []
    while root != None or stack != []:
        while root != None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res