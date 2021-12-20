# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/

def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    right = self.rightSideView(root.right)
    left = self.rightSideView(root.left)
    return [root.val] + right + left[len(right):]