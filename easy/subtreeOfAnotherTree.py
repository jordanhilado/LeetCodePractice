# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/

def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def compare(node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is not None and node2 is not None:
            return ((node1.val == node2.val) and
                    compare(node1.left, node2.left) and 
                    compare(node1.right, node2.right))
        return False
    q = [root]
    while q:
        curr = q.pop()
        if compare(curr, subRoot):
            return True
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
    return False