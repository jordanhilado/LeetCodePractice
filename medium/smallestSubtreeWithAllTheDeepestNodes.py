# 865. Smallest Subtree with all the Deepest Nodes
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
    def depth(node, d):
        if not node:
            return node, d
        
        left, leftDepth = depth(node.left, d + 1)
        right, rightDepth = depth(node.right, d + 1)
        
        if leftDepth > rightDepth:
            return left, leftDepth
        
        if rightDepth > leftDepth:
            return right, rightDepth
        
        return node, leftDepth
    return depth(root, 0)[0]