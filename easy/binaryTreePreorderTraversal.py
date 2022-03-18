# 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/

def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    q = [root]
    ans = []
    while q:
        curr = q.pop()
        if curr:
            ans.append(curr.val)
            if curr.right: q.append(curr.right)
            if curr.left: q.append(curr.left)
    return ans