# 938. Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/

#################### SOLUTION 1: DFS with stack ####################

def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    q, ans = [root], 0
    while q:
        curr = q.pop()
        if low <= curr.val <= high:
            ans += curr.val
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
    return ans

#################### SOLUTION 2: Recursive, with helper function ####################

def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    def dfs(node):
        if node:
            if low <= node.val <= high:
                self.ans += node.val
            if node.val > low: dfs(node.left)
            if node.val < high: dfs(node.right)
    self.ans = 0
    dfs(root)
    return self.ans

#################### SOLUTION 3: Recursive, no helper function ####################

def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    if not root: return 0
    if root.val > high: return self.rangeSumBST(root.left, low, high)
    if root.val < low: return self.rangeSumBST(root.right, low, high)
    return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)