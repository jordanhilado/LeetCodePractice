# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/

def isValidBST(self, root: Optional[TreeNode]) -> bool:
    output = []
    def inorder(node, output):
        if node is None:
            return
        inorder(node.left, output)
        output.append(node.val)
        inorder(node.right, output)
    inorder(root, output)
    for i in range(1, len(output)):
        if output[i-1] >= output[i]:
            return False
    return True