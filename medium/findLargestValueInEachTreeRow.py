# 515. Find Largest Value in Each Tree Row
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    q, ans = [root], []
    while q:
        level = []
        max_node = float('-inf')
        for curr in q:
            if curr.val > max_node:
                max_node = curr.val
            if curr.left: level.append(curr.left)
            if curr.right: level.append(curr.right)
        ans.append(max_node)
        q = level
    return ans