# 1110. Delete Nodes And Return Forest
# https://leetcode.com/problems/delete-nodes-and-return-forest/

def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    ans = []
    to_delete = set(to_delete)
    def helper(node):
        if not node:
            return None
        node.left = helper(node.left)
        node.right = helper(node.right)
        if node.val in to_delete:
            if node.left:
                ans.append(node.left)
            if node.right:
                ans.append(node.right)
            return None
        return node
    helper(root)
    if root.val not in to_delete:
        ans.append(root)
    return ans