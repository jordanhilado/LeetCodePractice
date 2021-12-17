# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if inorder:
        curr = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[curr])
        root.left = self.buildTree(preorder, inorder[0:curr])
        root.right = self.buildTree(preorder, inorder[curr+1:])
        return root