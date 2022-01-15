# 958. Check Completeness of a Binary Tree
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
    null_encountered = False
    q = [root]
    while q:
        curr = q.pop(0)
        if not curr: 
            null_encountered = True
            continue
        if null_encountered: return False
        q.append(curr.left)
        q.append(curr.right)
    return True