# 100. Same Tree
# https://leetcode.com/problems/same-tree/

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # base cases
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    # recursive step
    return (self.isSameTree(p.left, q.left) and
    self.isSameTree(p.right, q.right))