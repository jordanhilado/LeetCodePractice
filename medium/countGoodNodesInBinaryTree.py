# 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

def goodNodes(self, root: TreeNode) -> int:
    def dfs(node, maxVal):
        if not node:
            return 0
        if node.val >= maxVal:
            good = 1
        else:
            good = 0
        maxVal = max(node.val, maxVal)
        return good + dfs(node.left, maxVal) + dfs(node.right, maxVal)
    return dfs(root, root.val)