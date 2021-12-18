# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root == None or root == p or root == q:
        return root
    # find p/q in left and right subtrees
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    # if p and q found in left and right subtree of this node, then this node is LCA
    if left and right:
        return root
    # return the node which returned a node from its subtree
    # such that one of its ancestors will be the LCA
    return left if left else right