# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    def dfs(root, l):
        st = [root]
        while st:
            current = st.pop()
            l.append(current.val)
            if current.right is not None: st.append(current.right) 
            if current.left is not None: st.append(current.left)
        return l
    l = []
    s = dfs(root, l)
    return sorted(s)[k-1]