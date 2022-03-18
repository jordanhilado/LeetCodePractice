# 145. Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/

def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    q = [root]
    ans = []
    while q:
        curr = q.pop()
        if curr:
            ans.append(curr.val)
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
    return ans[::-1]