# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    ans = [0]
    def dfs(root):
        if root is None:
            return -1 
        left = dfs(root.left)
        right = dfs(root.right)
        ans[0] = max(ans[0], 2 + left + right)
        
        return 1 + max(left, right)
    dfs(root)
    return ans[0]