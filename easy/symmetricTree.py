# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if root == None:
        return True
    return self.isMirror(root.left, root.right)
def isMirror(self, leftroot, rightroot):
    if leftroot and rightroot:
        return leftroot.val == rightroot.val and self.isMirror(leftroot.left, rightroot.right) and self.isMirror(leftroot.right, rightroot.left)
    return leftroot == rightroot