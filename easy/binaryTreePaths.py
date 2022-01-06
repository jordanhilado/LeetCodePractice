# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/

def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    if not root:
        return []
    ans, stack = [], [(root, "")]
    while stack:
        node, ls = stack.pop()
        if not node.left and not node.right:
            ans.append(ls + str(node.val))
        if node.right:
            stack.append((node.right, ls + str(node.val) + "->"))
        if node.left:
            stack.append((node.left, ls + str(node.val) + "->"))
    return ans