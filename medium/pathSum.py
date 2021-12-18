# 113. Path Sum II
# https://leetcode.com/problems/path-sum-ii/

def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    if not root:
        return []
    paths = []
    q = [(root, [root.val])]
    while q:
        curr, val = q.pop()
        if not curr.left and not curr.right and sum(val) == targetSum:
            paths.append(val)
        if curr.left is not None: q.append((curr.left, val+[curr.left.val]))
        if curr.right is not None: q.append((curr.right, val+[curr.right.val]))
    return paths